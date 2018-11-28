#include<iostream>
#include<algorithm>
#define ll long long
#define MAXN 1024
using namespace std;
ll T,R,K,N,A[MAXN];
void solve()
{
  ll i,nxt[MAXN],sp[MAXN];
  ll last=0,cr=0;
  ll rnd=0,sz=0;
  ll ans=0;
  for(i=0;i<N;++i)nxt[i]=-1;
  for(i=0;i<N;++i)sp[i]=0;
  i=0;
  while(1)
  {
    cr+=A[i];++sz;
    if(cr>K||sz>N)
    {
      ++rnd;
      nxt[last]=i;
      sp[last]=cr-A[i];
      ans+=(ll)cr-(ll)A[i];
      cr=0;sz=0;
      last=i;
      if(nxt[i]!=-1)break;
      continue;
    }
    if(rnd==R)break;
    i=(i+1)%N;
  }
  R-=rnd;
  ll it=0,j=i;
  ll cyc=0;
  while(1)
  {
    cyc+=sp[j];
    j=nxt[j];
    ++it;
    if(i==j)break;
  }
  ans+=(ll)(R/it)*(ll)cyc;
  R%=it;
  while(R)
  {
    ans+=(ll)sp[i];
    i=nxt[i];
    --R;
  }
  cout<<ans<<'\n';
}
int main()
{
  ll i,tc;
  cin>>T;
  for(tc=1;tc<=T;++tc)
  {
    cin>>R>>K>>N;
    for(i=0;i<N;++i)cin>>A[i];
    cout<<"Case #"<<tc<<": ";
    solve();
  }
  return 0;
}