#include <iostream>
#include <vector>
#include <cstdio>
#include <cmath>
using namespace std;
#define f first
#define s second
#define mp make_pair
#define pb push_back
#define ll long long
vector <pair<char,int> > a;
int make(const vector <pair<char,int> >& p)
{
  int ans=0,doA=0,doB=0,stayA=1,stayB=1;
  for(int i=0;i<p.size();i++)
  {
    if (p[i].f=='B')
    {
      if (doA>=fabs(p[i].s*1.0-stayB)+1)ans++,doB++,stayB=p[i].s;
      else ans+=fabs(p[i].s*1.0-stayB)+1-doA,doB+=fabs(p[i].s*1.0-stayB)+1-doA,stayB=p[i].s;
      doA=0;
    } else 
    {
      if (doB>=fabs(p[i].s*1.0-stayA)+1)ans++,doA++,stayA=p[i].s;
      else ans+=fabs(p[i].s*1.0-stayA)+1-doB,doA+=fabs(p[i].s*1.0-stayA)+1-doB,stayA=p[i].s;
      doB=0;
    }
  }
  a.clear();
  return ans;
}
int main()
{
  freopen("A-large.in","r",stdin);
  freopen("output.txt","w",stdout);
  int t,n;
  cin>>t;
  for(int i=0;i<t;i++)
  {
    char x;
    int wh;
    cin>>n;
    for(int j=0;j<n;j++)cin>>x>>wh,a.pb(mp(x,wh));
    int mov=make(a);
    cout<<"Case #"<<i+1<<": "<<mov<<endl;
  }
  return 0;
}
/*
was=next_permutation(a.begin(),a.end());
*/