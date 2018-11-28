#include <iostream>
#include <algorithm>
#include <string>
#include <map>
using namespace std;
#define MAXN 110
#define MAXM 1010
map<string,int> names;
int n,m;
int queries[MAXM];

int f[MAXM][MAXN];
int ans;

int t;
int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    cin>>t;
    for (int i=1;i<=t && cout<<"Case #"<<i<<": ";i++)
    {
        int i,j,k;
        names.clear();
        cin>>n;
        cin.ignore(0x7FFFFFFF,'\n');
        for (i=0;i<n;i++)
        {
            char line[1000];
            gets(line);
            names[line]=i;
        }
        cin>>m;
        cin.ignore(0x7FFFFFFF,'\n');
        for (i=1;i<=m;i++)
        {
            char line[1000];
            gets(line);
            if (names.find(line)==names.end())
            {
                i--;
                m--;
                continue;
            }
            queries[i]=names[line];
        }
        memset(f[0],0,sizeof(f[0]));
        for (i=1;i<=m;i++)
        for (j=0;j<n;j++)
        {
            if (queries[i]==j) f[i][j]=-1;
            else
            {
                f[i][j]=-1;
                for (k=0;k<n;k++)
                if (f[i-1][k]!=-1)
                {
                    if (f[i][j]==-1) f[i][j]=0x7FFFFFFF;
                    f[i][j]=min(f[i][j],f[i-1][k]+(((int)(j==k))^1));
                }
            }
        }
        ans=0x7FFFFFFF;
        for (i=0;i<n;i++)
        if (f[m][i]!=-1) ans=min(ans,f[m][i]);
        cout<<ans<<endl;
    }
    return 0;
}
