#include <iostream>
#include <cstdio>
using namespace std;
int T,t,i,j,k,n,m;
char a[60][60];
bool flag;
bool drawred(int x, int y)
{
    if (!(x+1<n&&y+1<m)) return false;
    if (!(a[x][y]=='#'&&a[x][y+1]=='#'&&a[x+1][y]=='#'&&a[x+1][y+1]=='#')) return false;
    a[x][y]='/';
    a[x][y+1]='\\';
    a[x+1][y]='\\';
    a[x+1][y+1]='/';
    return true;
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>T;
    for (t=1; t<=T; t++)
    {
        cin>>n>>m;
        for (i=0; i<n;i++)
         for (j=0; j<m;j++)
          cin>>a[i][j];
          flag=true;
        for (i=0;i<n;i++)
         for (j=0; j<m; j++)
         {
             if (a[i][j]=='#')
              if (!drawred(i,j))
              {
               flag=false;
                break;
              }
         }
         cout<<"Case #"<<t<<":"<<endl;
         if (!flag) cout<<"Impossible"<<endl;
          else
         for (i=0; i<n;i++)
         {
          for (j=0; j<m;j++)
           cout<<a[i][j];
          cout<<endl;
         }
    }
    return 0;
}
