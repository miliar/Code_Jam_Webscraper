/*
uva :
author : rafsan
algo :
*/

#include<iostream>
#include<vector>
#include<map>
#include<algorithm>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cstring>
#include<queue>
#include<fstream>
#include<sstream>
#include<stack>
#include<list>
#include<deque>
#include<bitset>
#include<utility>
#include<climits>
#include<iomanip>
#include<ctime>
#include<complex>
using namespace std;


#define FOR(i,a,b) for (int i=(a);i<(b);i++)
#define RFOR(i,a,b) for (int i=(b)-1;i>=(a);i--)
#define REP(i,n) for (int i=0;i<(n);i++)
#define RREP(i,n) for (int i=(n)-1;i>=0;i--)

#define inf INT_MAX/3
#define pb push_back
#define MP make_pair
#define all(a) (a).begin(),(a).end()
#define SET(a,c) memset(a,c,sizeof a)
#define CLR(a) memset(a,0,sizeof a)
#define pii pair<int,int>
#define pcc pair<char,char>
#define pic pair<int,char>
#define pci pair<char,int>
#define VS vector<string>
#define VI vector<int>
#define debug(x) cout<<#x<<": "<<x<<endl
#define MIN(a,b) (a>b?b:a)
#define MAX(a,b) (a>b?a:b)
#define pi 2*acos(0.0)
#define INFILE() freopen("in0.txt","r",stdin)
#define OUTFILE()freopen("out0.txt","w",stdout)
#define in scanf
#define out printf
#define ll long long
#define ull unsigned long long
#define eps 1e-9
#define mod 1000000007
struct nod
{
    int mx;
    bool issur;
}zz;
vector<nod>g[35];
int a[105];
int surp[105];
int notsurp[105];
void precal()
{
    for(int i=0;i<=10;i++)
    for(int j=i;j<=i+2;j++)
    if(j<=10)
    for(int k=i;k<=i+2;k++)
    {

        if(k<=10)
        {
           // cout<<i<<" "<<j<<" "<<k<<endl;
        zz.issur=false;
        if(abs(i-j)==2||abs(k-i)==2||abs(k-j)==2)zz.issur=true;
        zz.mx=max(i,max(j,k));
        g[i+j+k].pb(zz);
        }
    }
  // FOR(i,0,31){cout<<i<<":\n";
   // FOR(j,0,g[i].size())cout<<g[i][j].mx<<" "<<g[i][j].issur<<endl;}
}
int N,S,p;
int ans;
bool mark[105][105];
void DFS(int pos,int sur,int cost)
{
    //if(pos<=N&&sur==S)
    ans=max(ans,cost);
    if(pos>=N)return;
    if(mark[pos][sur])return ;
    if(sur<S&&surp[a[pos]])DFS(pos+1,sur+1,cost+1);
    if(notsurp[a[pos]])DFS(pos+1,sur,cost+1);
    DFS(pos+1,sur,cost);
}
int main()
{
    freopen("B-small-attempt4.in","r",stdin);
    freopen("B-small-attempt4.out","w",stdout);
    precal();
    int ks;
    cin>>ks;
    FOR(cas,1,ks+1)
    {
        cin>>N>>S>>p;
        FOR(i,0,N)cin>>a[i];
        FOR(i,0,N)surp[a[i]]=notsurp[a[i]]=0;
        FOR(i,0,N)
        FOR(j,0,g[a[i]].size())
        {
            if(g[a[i]][j].issur&&g[a[i]][j].mx>=p)surp[a[i]]=1;
            else if(!g[a[i]][j].issur&&g[a[i]][j].mx>=p)notsurp[a[i]]=1;
        }
        CLR(mark);
        ans=0;
        DFS(0,0,0);
        cout<<"Case #"<<cas<<": "<<ans<<endl;
    }
return 0;
}
