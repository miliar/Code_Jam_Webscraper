#include<iostream>
#include<vector>
#include<algorithm>
#include<math.h>
#include<string>
#include<iomanip>
#define beginT int _T; cin>>_T; for(int _t=1;_t<=_T;_t++)
#define printT(_ans) cout<<"Case #"<<_t<<": "<<_ans<<endl
using namespace std;

int main()
{
   beginT
   {
         int r,c,b=0;
         cin>>r>>c;
         char g[r][c];
         for(int i=0;i<r;i++)
         {
                 for(int j=0;j<c;j++)
                 {
                      cin>>g[i][j];
                      if(g[i][j]=='#')
                                      b++;
                 }
         } 
         printT("");
         if(b==0)
         {
                 for(int i=0;i<r;i++)
                 {
                         for(int j=0;j<c;j++)
                         {
                                 cout<<g[i][j];
                         }
                         cout<<endl;
                 }
         }      
         else if((b%4)!=0)
         {
                 cout<<"Impossible"<<endl;
         }
         else
         {
             bool v[r][c];
             for(int i=0;i<r;i++)
                     for(int j=0;j<c;j++)
                             v[i][j]=0;
             for(int i=0;i<r;i++)
             {
                     for(int j=0;j<c;j++)
                     {
                             if(v[i][j]==1) continue;
                             if(g[i][j]=='#' && g[i+1][j]=='#' && g[i][j+1]=='#' && g[i+1][j+1]=='#')
                             {
                                             g[i][j]=g[i+1][j+1]='/';
                                             g[i+1][j]=g[i][j+1]='\\';
                                             v[i][j]=v[i+1][j]=v[i][j+1]=v[i+1][j+1]=1;
                                             b-=4;
                             }
                     }
             }
             if(b!=0)
                     cout<<"Impossible"<<endl;
             else
             {
                 for(int i=0;i<r;i++)
                 {
                         for(int j=0;j<c;j++)
                         {
                                 cout<<g[i][j];
                         }
                         cout<<endl;
                 }                    
             }
         }
   }
   return 0;
}
