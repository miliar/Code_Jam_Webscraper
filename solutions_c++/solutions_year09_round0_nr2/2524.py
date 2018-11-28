#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

void getSink(int x, int y, int w, int h, int **cells, char **basin, int &index)
{
    int newx = x, newy = y, lastalt = cells[y][x];

   if (basin[y][x] != ' ')  
      return;

   if (y != 0)        {
       if ((cells[y-1][x] < cells[y][x]) && cells[y-1][x] < lastalt)    {

           newx = x;
           newy = y-1;
           lastalt = cells[newy][newx];
       }
   }
   
   if (x != 0)        {
       if ((cells[y][x-1] < cells[y][x]) && cells[y][x-1] < lastalt)    {
           
           newx = x-1;
           newy = y;
           lastalt = cells[newy][newx];
       }
   } 
   
   if (x != (w-1))         {
       if ((cells[y][x+1] < cells[y][x]) && cells[y][x+1] < lastalt)    {
           
           newx = x+1;
           newy = y;
           lastalt = cells[newy][newx];
       }
   }
    
   if (y != (h-1)) {
      if ((cells[y+1][x] < cells[y][x]) && cells[y+1][x] < lastalt)    {
           
           newx = x;
           newy = y+1;
           lastalt = cells[newy][newx];
      }
   } 
       
   if (x == newx && y == newy) {
          if (basin[newy][newx] == ' ')
                basin[y][x] = (char)(96 + ++index);
   }
   else {
          getSink(newx, newy, w, h, cells, basin, index);
          basin[y][x] = basin[newy][newx];
   }
}

void readLines(ifstream &myfile, int count, int w, int **cells, char **basin)
{
     string line;
     int lastf, index, found;
     
     for (int i=0; i<count; i++)     {

         getline (myfile,line);
         cells[i] = new int[w];
         basin[i] = new char[w];
         
         lastf = 0;
         index = 0;
         lastf = 0;
         
         while(true) {
                     
             found = line.find(' ', lastf);
             if (found == string::npos)  {

                cells[i][index] = atoi(line.substr(lastf,line.length()-lastf).c_str());
                basin[i][index] = ' ';
         
                index++;
                break;
            }
            else {
                cells[i][index] = atoi(line.substr(lastf, found-lastf).c_str());
                basin[i][index] = ' ';
         
                index++;
                lastf = found + 1;
            }
         }
     }
}

void handleCase(ifstream &myfile)
{
     ofstream outfile("c:\\temp\\output.txt");
     string line;
     int **cells, index = 0;
     char **basin;
     int t, h, w, j;
     
     if (outfile.is_open()) {
          
          getline (myfile,line);
          t = atoi(line.c_str());
     
          for (int i=0; i<t; i++) {
              getline (myfile,line);
              j = line.find_first_of(" ");
     
              h = atoi(line.substr(0, j).c_str());
              w = atoi(line.substr(j).c_str());
     
              cells = new int*[h];
              basin = new char*[h];
              
              readLines(myfile, h, w, cells, basin);
              
              index = 0;
              outfile<<"Case #"<<i+1<<":"<<endl;
              
              for(int i=0; i<w; i++) {
                  for(int j=0; j<h; j++) {
                      getSink(i,j, w, h, cells, basin, index);    
                    }
              }        
              
              for(int i=0; i<h; i++) {
                  for(int j=0; j<w; j++) {
                      outfile<<basin[i][j];
                      if (j!=w-1) 
                         outfile<<" ";      
                  }
                  outfile<<endl;
              }        
         }
         
         outfile.close();
     }
     
     else cout << "Unable to open out file";
}

int main(int argc, char *argv[])
{
  ifstream myfile ("c:\\temp\\input.txt");
  
  if (myfile.is_open())
  {
    while (! myfile.eof() )
          handleCase(myfile);              

    myfile.close();
  }

  else cout << "Unable to open in file"; 

  system("PAUSE");
  return EXIT_SUCCESS;
}
