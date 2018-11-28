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
char a[105][105];
vector <double> wp,owp,oowp;
vector <pair<int,int> > e;
int main()
{
  freopen("A-large.in","r",stdin);
  freopen("output.txt","w",stdout);
  int t,n;
  cin>>t;
  for(int r=0;r<t;r++)
  {
    cin>>n;
    for(int i=0;i<n;i++)
      for(int j=0;j<n;j++)cin>>a[i][j];
    wp.resize(n);
    owp.resize(n);
    oowp.resize(n);
    e.resize(n);
    for(int i=0;i<n;i++)
    {
      int win=0,all=0;
      for(int j=0;j<n;j++)
      {
        if (a[i][j]=='0' || a[i][j]=='1')all++;
        if (a[i][j]=='1') win++;
      }
      wp[i]=win*1.0/all;
      e[i]=mp(win,all);
    }
    for(int i=0;i<n;i++)
    {
      double swp=0;
      int all=0;
      for(int j=0;j<n;j++)
      {
        if (a[i][j]=='0' || a[i][j]=='1')all++;
        if (a[j][i]=='1')swp+=(e[j].f-1)*1.0/(e[j].s-1);
        else if (a[j][i]=='0')swp+=e[j].f*1.0/(e[j].s-1);
        //if (a[i][j]=='0' || a[i][j]=='1')swp+=wp[j];
      }
      owp[i]=swp/all;
    }
    for(int i=0;i<n;i++)
    {
      double sowp=0;
      int all=0;
      for(int j=0;j<n;j++)
      {
        if (a[i][j]=='0' || a[i][j]=='1')all++;
        if (a[i][j]=='0' || a[i][j]=='1')sowp+=owp[j];
      }
      oowp[i]=sowp/all;
    }
    cout<<"Case #"<<r+1<<":\n";
    for(int i=0;i<n;i++)printf("%.12f\n",0.25*wp[i] + 0.50*owp[i] + 0.25*oowp[i]);
    wp.clear();
    owp.clear();
    oowp.clear();
    e.clear();
  }
  return 0;
}