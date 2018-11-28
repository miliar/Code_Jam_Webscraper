#include <iostream>
#include <cstring>
#include <vector>
#include <cstdio>
using namespace std;
#define f first
#define s second
#define mp make_pair
#define pb push_back
#define ll long long
#define INF 1<<30
#define PI 3.1415926535897932
#define EPS 1e-9
#define sqr(x) ((x)*(x))
#define SZ 10
vector <int> g[10],ans,room[105],e,bgn,end;
bool diag[SZ][SZ],yes;
int n,m,beg,use[SZ],c=0;
bool eq(int i)
{
  sort(e.begin(),e.end());
  for(int j=0;j<room[i].size();j++)
    if (e[j]!=room[i][j])return false;
  return true;
}
void find(int v,int pr)
{
  cout<<v<<endl;
  if (yes)return;
  if (v==beg && use[beg]==c)
  {
    if (e.size()<=2)return;
    for(int i=0;i<e.size();i++)
      for(int j=i+2;i==0 && j!=e.size()-1 || i!=0 && i!=j%e.size()+1;j++)
        if (diag[e[i]][e[(j%e.size())]])return;
    //for(int p=1;p<=c;p++)
      //if (eq(p))return;
    for(int i=0;i<e.size();i++)room[c].pb(e[i]);
    sort(room[c].begin(),room[c].end());
    //cout<<endl<<endl;
    yes=true;
    e.clear();
    return;
  } else if (use[v]==c)return;
  e.pb(v);
  use[v]=c;
  for(int i=0;i<g[v].size() && !yes;i++)
    if (g[v][i]!=pr)find(g[v][i],v);

  if (!yes)
  {
    use[v]=0;
    e.pop_back();
    cout<<"out "<<v<<endl;
  }
}
void solve()
{
  for(int i=0;i<n;i++)
    if (!use[i])
    {
      beg=i;
      yes=false;
      c++;
      for(int p=0;p<n;p++)use[p]=0;
      find(i,-1);
      if (yes)i--;
      cout<<endl<<endl;
    }
  //for(int i=0;i<g[0].size();i++)cout<<g[0][i]<<" ";
  //cout<<endl;
  for(int i=1;i<=c;i++)
  {
    cout<<"room #"<<i<<": ";
    for(int j=0;j<room[i].size();j++)cout<<room[i][j]<<" ";
    cout<<endl;
  }
  //....
  for(int i=0;i<n;i++)g[i].clear();
  c=0;
}
int main()
{
  int t;
  cin>>t;
  for(int r=0;r<t;r++)
  {
    cin>>n>>m;
    int x,y;
    for(int i=0;i<n-1;i++)g[i].pb(i+1),g[i+1].pb(i);
    g[n-1].pb(0);
    g[0].pb(n-1);
    bgn.resize(n);
    end.resize(n);
    for(int i=0;i<m;i++)cin>>bgn[i];
    for(int i=0;i<m;i++)cin>>end[i];
    for(int i=0;i<m;i++)
    {
      diag[bgn[i]-1][end[i]-1]=diag[end[i]-1][bgn[i]-1]=true;
      g[bgn[i]-1].pb(end[i]-1);
      g[end[i]-1].pb(bgn[i]-1);
    }
    solve();
    //...
  }
  return 0;
}