#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream in("A-large.in");
    ofstream out("output.txt");
    int t,n;
    in>>n;char arr[50][50];
    for(int i=0;i<n;i++)
    {
            out<<"Case #"<<i+1<<": "<<endl;
            int row,col;
            in>>row>>col;
            bool flag = true;
            for(int j=0; j<row; j++)
             in>>arr[j];
            
            for(int j=0; j<row && flag; j++)
            {
                for(int k=0; k<col && flag; k++)
                {
                   if(arr[j][k] == '#')
                   {
                       if(arr[j][k+1] == '#' && arr[j+1][k] == '#' && arr[j+1][k+1] == '#')
                        {
                           arr[j][k] = '/';
                           arr[j][k+1] = '\\';
                           arr[j+1][k] = '\\';
                           arr[j+1][k+1] = '/';           
                        }          
                        else if(arr[j][k] == '#')
                         flag = false;
                   }     
                }    
            }
            if(flag == false)
              out<<"Impossible"<<endl;
              
            else
            {
               for(int j=0; j<row; j++)
               {
                for(int k=0; k<col; k++) 
                  out<<arr[j][k];
                out<<endl;  
                }
            }      
            
    }
    
    
    system("pause");    
    return 0;
}
