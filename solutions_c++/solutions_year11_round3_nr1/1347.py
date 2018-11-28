#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>

using namespace std;

int main()
{
    int T;
    int count =1;
    ifstream in("A-large.in");
    ofstream out("output.txt");
    in>>T;
    //cout<<T<<endl;
    while(T > 0)
    {
          int row,col;
          in>>row;
          in>>col;
          int count_blue = 0; 
          bool itCan = true;
          //cout<<row<<" "<<col<<endl;
          char **arr;
          arr = new char*[row];
          for(int i=0; i<row; i++)
          {
              arr[i] = new char[col];        
          } 
          for(int i=0; i<row; i++)
          {
                  for(int j=0; j<col; j++)
                  {
                          in>>arr[i][j];
                          if(arr[i][j]=='#')
                          count_blue++;
                          //cout<<arr[i][j]<<endl;        
                  }        
          }
          //cout<<count_blue<<endl;
          if(count_blue%4 == 0)
          {
                 for(int i=0; i<row; i++)
                 {
                         for(int j=0; j<col; j++)
                         {
                                 if(arr[i][j] == '#')
                                 {
                                      if((i+1)<row && (j+1)<col && arr[i+1][j]=='#' && arr[i][j+1]=='#' && arr[i+1][j+1]== '#')
                                      {
                                           arr[i][j] = '/';
                                           arr[i+1][j] = '\\';
                                           arr[i][j+1] = '\\';
                                           arr[i+1][j+1] = '/';                     
                                      }
                                      else
                                      {
                                          itCan = false;
                                          break;
                                      }
                                 }        
                         } 
                         if(itCan == false)
                         {
                             break;         
                         }       
                 }             
          }
          else
          {
              itCan = false;
              
          }
          
          if(itCan==false)
          {
               out<<"Case #"<<count<<":"<<endl;
               out<<"Impossible"<<endl;                
          }
          else
          {
              out<<"Case #"<<count<<":"<<endl;
              for(int i=0; i<row; i++)
              {
                  for(int j=0; j<col; j++)
                  {
                       out<<arr[i][j];        
                  }
                  out<<endl;        
              }
          }
            
          T--;
          count++;
    }   
    
    in.close();
    out.close();

    system("pause");
    return 0;    
}

