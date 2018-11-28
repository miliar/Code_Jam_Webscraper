#include <iostream>
using namespace std;

int main()
{
 int t,r,c,temp = 1,flag;
 cin>>t;
 while(temp <= t)
 {
            cin>>r>>c;
            char a[r][c];
            for(int i = 0; i < r; i++)
                    for(int j = 0; j < c; j++)
                            cin>>a[i][j];
           
           flag = 1;
           for(int i = 0; i < r; i++)
           {
                   for(int j = 0; j < c; j++)
                   {
                           if(a[i][j] == '#' )
                           {
                                      if(a[i][j+1] == '#' && a[i+1][j] == '#' && a[i+1][j+1]== '#')
                                      {
                                                   a[i][j] = '/';
                                                   a[i][j+1] = '\\';
                                                   a[i+1][j] = '\\';
                                                   a[i+1][j+1] = '/';                   
                                      }
                                      else
                                       {   
                                           flag = 0;                   
                                           break;
                                       }
                           }
                   }
                   if(flag == 0)
                           break;
           }     
           cout<<"Case #"<<temp<<":"<<endl;
           temp++;
           if(flag)
           {
                   for(int i = 0; i < r; i++)
                    {
                                  for(int j = 0; j < c; j++)
                                          cout<<a[i][j];
                                  cout<<endl;
                    }  
           }
           else
               cout<<"Impossible"<<endl;
}

return 0;
} 
