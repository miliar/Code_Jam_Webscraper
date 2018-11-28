#include <cstdlib>
#include <iostream>
#include <ios>
#include <fstream>
#include <string>

using namespace std;
 
int getFlowDir(int alt[101][101],int x, int y)
{
                      // 0 is the cell itself (sink)
                      // 1 is north
                      // 2 is west
                      // 3 is east
                      // 4 is south
     int a[5];
     a[0] = alt[x][y];
     a[1] = alt[x][y-1];
     a[2] = alt[x-1][y];
     a[3] = alt[x+1][y];
     a[4] = alt[x][y+1];
     int i=0;
     int cur = 0;
     while(i<5)
         { 
               //cout << "\t\t["<<i<<"]="<<a[i] <<" =? ["<<cur<<"]="<< a[cur]<<endl;
               if (!(
                       (i==1 && y==0) ||
                       (i == 2 && x==0)
                     )
                   )
               if (a[i] > a[cur]) cur = i;
               i++;
         } 
     //cout << "\t["<<x<<"]["<<y<<"] -> "<<cur<<endl;
     return cur;
        
}
 
void connectSources(int alt[101][101],char labels[101][101],int x, int y)
{
     int cur = alt[x][y];
     int x_os[5],y_os[5],a[5];
     
     x_os[1] = 0;
     x_os[2] = -1;
     x_os[3] = 1;
     x_os[4] = 0;
     
     y_os[1] = -1;
     y_os[2] = 0;
     y_os[3] = 0;
     y_os[4] = 1;
     
     a[1] = alt[x][y-1];
     a[2] = alt[x-1][y];
     a[3] = alt[x+1][y];
     a[4] = alt[x][y+1];
     int i;
     for (i=1;i<5;i++)
         if (a[i] < cur)
            {if ( (5-getFlowDir(alt,x + x_os[i],y+y_os[i])) == i and labels[x +x_os[i]][y+y_os[i]] == ' ')
                {
                                      labels[x +x_os[i]][y+y_os[i]] = labels[x][y];
                                      connectSources(alt,labels,x+x_os[i],y+y_os[i]);
                }
                  }
     
}

char nextLabel(bool reset = false)//tested: ok
{
       static char cur_label = '0';
       if (reset)  cur_label = '0'-1;
       return cur_label++;
}

void replace_label(char labels[101][101],char match,char replace,int width,int height)
{
     int x,y;
     for (y=0;y<height;y++)
      for(x=0;x<width;x++)
         if (labels[x][y] == match)
             labels[x][y] = replace;
}

int main(int argc, char *argv[])
{

//file
    // Datei öffnen
    ifstream in_file("B-small-attempt1.in", ios::in|ios::binary);
    if (!in_file) // Fehler beim ™ffnen der Datei
    {
     cerr << "\nFehler beim Öffnen der Datei ";
     exit(1);
    }
    
    int cid,h,i,j,x,y=0;
    int case_count;
    int case_width;
    int case_height;
    char labels[101][101];
//PREPARATION
    in_file>>case_count;
//EXECUTION
    for (cid=1;cid<case_count;cid++)
        {
        int altitudes[101][101];
        
    //cout<<case_count;
        
        //clear altitudes
        for (y=0;y<102;y++)
            for (x=0;x<102;x++)
                altitudes[x][y] = 0;
        
        //clear labels
        for (y=0;y<102;y++)
            for (x=0;x<102;x++)
                labels[x][y] = ' ';
        //case
        nextLabel(true);
        //read size
        in_file>>case_height>>case_width;
            
        cout<<"Case #"<<cid<<":"<<endl;
        

        //read altitudes
        for (y=0;y<case_height;y++)
            for (x=0;x<case_width;x++)
             {
                in_file>>altitudes[x][y];   
                altitudes[x][y] = 10001 - altitudes[x][y];
             }
        
        /*for (y=0;y<case_height;y++)
            {
            for (x=0;x<case_width;x++)
                cout<<altitudes[x][y]<<" ";
            cout <<endl;
           }
        cout<<endl; */        
        //find sinks and label them
        for (y=0;y<case_height;y++)
            for (x=0;x<case_width;x++)
                    {   
                        int flowdir = getFlowDir(altitudes,x,y);
                        if (flowdir == 0) 
                           {// cell is a sink
                               labels[x][y] = nextLabel();
                               //cout<<"sink: "<<x<<y<<labels[x][y]<<endl;
                               connectSources(altitudes,labels,x,y);
                            }
                    }
        //correct labels
        char letter = 'a'-1;
        char last = '0';
        for (y=0;y<case_height;y++)
            for (x=0;x<case_width;x++)
                {
                 if (letter != labels[x][y] and labels[x][y]  < 'a')
                    { if (last=letter)letter++;
                     if (letter != labels[x][y])
                          replace_label(labels, labels[x][y],letter,case_width,case_height);
                          }
                 last = letter;
                     
                 }
                         
        //echo labels
        for (y=0;y<case_height;y++)
            {
            for (x=0;x<case_width;x++)
                cout<<labels[x][y]<<" ";                    
            cout <<endl;
            }
            
                    
        //system("PAUSE");
            }
    return EXIT_SUCCESS;
}


//     printf  ("%04i %04i %04i\n", letter_count, word_count, case_count );

