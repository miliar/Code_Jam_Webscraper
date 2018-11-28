#include<iostream>
#include<cstring>
#define m 60
using namespace std;
int main()
{
    int t,r,c,i,j,x,flag;
    char a[m][m];
    for(i=0;i<m;i++)
                for(j=0;j<m;j++)
                a[i][j]='\0';
    cin>>t;
    x=1;
    while(t--)
    {
           flag=0;
              cin>>r>>c;
              for(i=0;i<r;i++)
                for(j=0;j<c;j++)
                cin>>a[i][j];
     for(i=0;i<r;i++)
      {
        for(j=0;j<c;j++)
         {
          if(a[i][j]=='#')
           {
              a[i][j]='/';
              if(a[i][j+1]=='#' && a[i+1][j]=='#' && a[i+1][j+1]=='#')
                {
                   a[i][j+1]='\\';
                  a[i+1][j]='\\';
                   a[i+1][j+1]='/' ;
                }
                else
                {flag=1;break;}     
           }
          }
          if(flag)break;
      }
      if(flag)
      cout<<"Case #"<<x++<<":\n"<<"Impossible";
      else
      {
          cout<<"Case #"<<x++<<":\n";
                for(i=0;i<r;i++)
                {     for(j=0;j<c;j++)
                      cout<<a[i][j];
                      cout<<endl;
                }
       }
       cout<<endl;
    
    }
   
   
   
  // system("pause");
   return 0;
}
