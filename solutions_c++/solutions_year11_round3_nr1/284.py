#include <iostream>
#include <cstdio>

using namespace std;

char a[200][200],res[200][200];

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t,q,r,c,i,j,kb,kr;
    cin>>t;
    for (q=0;q<t;q++)
    {
        cin>>r>>c;
        kb=0;
        kr=0;
        for (i=0;i<200;i++)
          for (j=0;j<200;j++)
            res[i][j]='.';
        for (i=0;i<r;i++)
          for (j=0;j<c;j++)
          {
            cin>>a[i][j];
            if (a[i][j]=='#')
              kb++;
          }
        for (i=0;i<r;i++)
          for (j=0;j<c;j++)
            if (a[i][j]=='#' && res[i][j]=='.')
            {
                res[i][j]='/';
                res[i+1][j]='\\';
                res[i][j+1]='\\';
                res[i+1][j+1]='/';
                kr+=4;
            }
       printf("Case #%d:\n",q+1);
       if (kr!=kb)
         cout<<"Impossible"<<endl;
       else
       {
           for (i=0;i<r;i++)
           {
               for (j=0;j<c;j++)
                 cout<<res[i][j];
               cout<<endl;
           }
       }
    }
    return 0;
}
