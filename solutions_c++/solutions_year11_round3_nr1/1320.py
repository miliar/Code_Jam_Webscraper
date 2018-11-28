#include<iostream>
using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
   int t,r,c,p;
   char arr[50][50];
   cin>>t;
   for(int q=1;q<=t;q++)
   {
           cin>>r>>c;
           for(int i=0;i<r;i++)
            for(int j=0;j<c;j++)
              cin>>arr[i][j];
           p=0;
           for(int i=0;i<r;i++)
           {
                   for(int j=0;j<c;j++)
                   {
                           if(arr[i][j]=='#')
                           {
                                             if(i==r-1 || j==c-1)
                                             {p=1;
                                              break;
                                             }
                                             if(arr[i+1][j]=='#' && arr[i+1][j+1]=='#' && arr[i][j+1]=='#')
                                             {
                                                                 arr[i][j]='/';
                                                                 arr[i][j+1]='\\';
                                                                 arr[i+1][j]='\\';
                                                                 arr[i+1][j+1]='/';
                                             }
                                             else
                                               p=1;
                           }
                   }
           }
           cout<<"Case #"<<q<<":"<<endl;
           if(p==1)
            cout<<"Impossible"<<endl;
           else
           {for(int i=0;i<r;i++)
            {
                    for(int j=0;j<c;j++)
                       cout<<arr[i][j];
                    cout<<endl;
            }
           } 
   }
   return 0;
}                                                      
