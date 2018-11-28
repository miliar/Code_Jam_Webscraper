#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
const int maxn=5000+10;
const int maxm=15+10;
int n,m,t,a[maxn][maxm],ans;
bool g[maxm][26];
string s;
void init()
{
    for (int i=0;i<n;i++)
    {
        cin >>s;
        for (int j=0;j<m;j++)
            a[i][j]=s[j]-'a';
    }
}
void solve()
{
    memset(g,0,sizeof(g));
    cin >>s;
    int t=0,i=0;
    while (i<s.size())
    {
        if (s[i]=='(')
        {
            while (s[++i]!=')')
                g[t][s[i]-'a']=true;
            t++;
        }
        else
            g[t++][s[i]-'a']=true;
        i++;
    }
    ans=0;
    if (t!=m)
        return;
    for (int i=0;i<n;i++)
    {
        bool flag=true;
        for (int j=0;j<m;j++)
            if (!g[j][a[i][j]])
            {
                flag=false;
                break;
            }
        if (flag)
            ans++;
    }
}
int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    cin >>m>>n>>t;
    init();
    for (int i=1;i<=t;i++)
    {
        solve();
        printf("Case #%d: %d\n",i,ans);
    }
    return 0;
}
