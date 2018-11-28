#include <iostream>
#include <vector>
#include <cassert>
using namespace std;

const int inf=0x10000000;

int solve(int pos, int dep, int sft, int n, vector<int> &v, vector<vector<int> > &q)
{
  bool need=false;
  for (int i=pos; i<pos+n; i++){
    if (v[i]>0){
      need=true;
      break;
    }
  }
  if (!need) return 0;
  if (n==1) return inf;

  //cout<<q[dep][sft]<<endl;
  for (int i=pos; i<pos+n; i++) v[i]--;
  int ret1=q[dep][sft]+solve(pos, dep+1, sft*2, n/2, v, q)+solve(pos+n/2, dep+1, sft*2+1, n/2, v, q);
  for (int i=pos; i<pos+n; i++) v[i]++;
  int ret2=solve(pos, dep+1, sft*2, n/2, v, q)+solve(pos+n/2, dep+1, sft*2+1, n/2, v, q);
  //cout<<ret1<<", "<<ret2<<endl;

  return min(inf, min(ret1, ret2));
}

int main()
{
  int cases; cin>>cases;
  for (int c=1; c<=cases; c++){
    int p; cin>>p;
    vector<int> v(1<<p);
    vector<vector<int> > q(p, vector<int>(1<<p));
    for (int i=0; i<(1<<p); i++){
      cin>>v[i];
      v[i]=p-v[i];
    }
    for (int i=0; i<p; i++){
      for (int j=0; j<(1<<(p-i-1)); j++){
	cin>>q[p-i-1][j];
      }
    }
    int ans=solve(0, 0, 0, 1<<p, v, q);
    assert(ans!=inf);
    cout<<"Case #"<<c<<": "<<ans<<endl;
  }
  return 0;
}
