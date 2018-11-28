#include <iostream>
#include <vector>
using namespace std;
#define f first
#define s second
#define mp make_pair
#define pb push_back
#define ll long long
vector <ll> a;
ll solve(const vector <ll>& p)
{
  ll sum=0,mini=1000005,xr=0;
  for(int i=0;i<p.size();i++)
  {
    xr^=p[i];
    sum+=p[i];
    mini=min(mini,p[i]);
  }
  a.clear();
  if (xr==0)return sum-mini;
  return -1;
}
int main()
{
  ll t,n,k,x;
  //freopen("C-large.in","r",stdin);
  //freopen("output.txt","w",stdout);
  cin>>t;
  for(int i=0;i<t;i++)
  {
    cin>>k;
    for(int j=0;j<k;j++)cin>>x,a.pb(x);
    ll ans=solve(a);
    cout<<"Case #"<<i+1<<": ";
    if (ans==-1)cout<<"NO\n"; 
    else cout<<ans<<endl;
  }
  return 0;
}