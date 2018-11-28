#include <iostream>
#include <stdio.h>
using namespace std;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int p,k,n,i,j,t;
    char m[100][100];
    bool ok;
    cin>>t;
    for (p=1; p<=t; p++)
    {
    cin>>n>>k;
    ok=true;
    for(i=1; i<=n; i++)
    for (j=1; j<=k; j++)
    cin>>m[i][j];
    for (i=1; i<n; i++)
    for (j=1; j<k; j++)
    if (m[i][j]=='#'&&m[i+1][j]=='#'&&m[i][j+1]=='#'&&m[i+1][j+1]=='#')
    {
        m[i][j]='/'; m[i+1][j+1]='/';
        m[i][j+1]='\\'; m[i+1][j]='\\';
    }
    for (i=1; i<=n; i++)
    for (j=1; j<=k; j++)
    if (m[i][j]=='#')
    ok=false;
    cout<<"Case #"<<p<<":"<<endl;
    if (!ok) cout<<"Impossible"<<endl;
    else
    {
        for (i=1; i<=n; i++)
        {
            for (j=1; j<=k; j++)
            cout<<m[i][j];
            cout<<endl;
        }
    }


    }
    return 0;
}
