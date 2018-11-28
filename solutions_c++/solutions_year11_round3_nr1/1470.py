#include <sstream>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
char a[200][200],b[200][200];
int main()
{
    int test ,i,n,j,m,k,t,ind1,ind2,tcase=1;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    cin>>test;
    while(test--)
    {
        cin>>n>>m;
        for(i=0;i<n;i++)
        {
         cin>>a[i];
        }
         t=0;

         for(i=0;i<n;i++)
         {
            k=0;
            for(j=0;j<m;j++)
            {
                if(a[i][j]=='0')continue;
                if(a[i][j]=='.')
                {
                    b[i][j]='.';
                    continue;
                }
                if(a[i][j]=='#')
                {
                    k++;
                    if(a[i][j+1]=='#'&&(j+1)<m)
                    k++;
                    if(a[i+1][j]=='#'&&(i+1)<n)
                    k++;
                    if(a[i+1][j+1]=='#'&&(i+1)<n &&(j+1)<m)
                    k++;
                }
                //cout<<k<<endl;
                if(k==4)
                {
                    b[i][j]='/';
                    a[i][j]='0';
                    b[i][j+1]='\\';
                    a[i][j+1]='0';
                    b[i+1][j]='\\';
                    a[i+1][j]='0';
                    b[i+1][j+1]='/';
                    a[i+1][j+1]='0';
                    k=0;
                }
                else
                {
                    t=1;
                    k=0;
                    break;
                }

           }
           b[i][j]=NULL;
         }
            cout<<"Case #"<<tcase++<<":"<<endl;
            if(t==1)
            {
                cout<<"Impossible"<<endl;
            }
            else
            {
                for(i=0;i<n;i++)
                cout<<b[i]<<endl;
            }
           // for(i=0;i<n;i++)
            //  b[i]='/0';

    }
    return 0;
}
