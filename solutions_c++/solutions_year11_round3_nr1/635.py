#include<iostream>
using namespace std;
int main()
{
    freopen("C:\\Users\\Administrator\\Desktop\\A-large.in","r",stdin);
    freopen("C:\\Users\\Administrator\\Desktop\\out","w",stdout);
    int T;
    cin>>T;
    int i;
    for(i=0;i<T;i++)
    {
         int r,c;
         char a[100][100];
         memset(a,0,sizeof(a));
         cin>>r>>c;
         int j,k;
         for(j=0;j<r;j++)
             for(k=0;k<c;k++)
                cin>>a[j][k];
         cout<<"Case #"<<i+1<<":"<<endl;
         bool sign = true;
         for(j=0;j<r;j++)
         {
             for(k=0;k<c;k++)
             {
                  if(a[j][k] == '#')
                  {
                      if(a[j][k+1]=='#'&&a[j+1][k]=='#'&&a[j+1][k+1]=='#')
                      {
                          a[j][k]='/';
                          a[j][k+1]='\\';
                          a[j+1][k]='\\';
                          a[j+1][k+1]='/';
                      }
                      else
                      {
                      cout<<"Impossible"<<endl;
                      sign=false;
                      break;
                      }
                  }
                  
                  
             }
             if(sign==false)
                    break;
             }
         if(sign)
         {
             for(j=0;j<r;j++)
             {
               for(k=0;k<c;k++)
                  cout<<a[j][k];
               cout<<endl;
             }
         }
             
    }
  //  system("pause");
    return 0;
}
