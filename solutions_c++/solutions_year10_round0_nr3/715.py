#include <vector>
#include <iostream>
using namespace std;

vector<int> gs; 
vector<int> used;
typedef long long ll;
vector<ll> cost;

ll ride (int R, int k,int pos,int depth,ll cost_now,bool fst) {
  if (depth>=R) return cost_now;
  if (used[pos]>=0 && fst) {
    int cyc = depth - used[pos];
    ll cyc_cost = cost_now - cost[pos];
    int skip = (R - depth) / cyc;
    return ride(R,k,pos,depth+cyc*skip,cost_now + skip * cyc_cost,false);
  }

  used[pos] = depth;
  cost[pos] = cost_now;
  
  int rider = 0, pos_next;
  for (int i = 0; i < gs.size();++i)  {
    int j = (pos+i) % gs.size();
    pos_next = j;
    if (rider + gs[j] > k) break;
    rider += gs[j]; 
  }
  return ride(R,k,pos_next,depth+1,rider+cost_now,fst);
}

int main () {
  int nc; cin >> nc;
  for (int ic = 0; ic < nc; ++ic) {
    int ans = 0;
    int R,k,N; cin >> R >> k >> N;
    gs = vector<int>(N);
    used = vector<int>(N,-1);
    cost = vector<ll>(N,0);
    for (int i = 0; i < N; ++i ) {
      cin >> gs[i];
    }
    cout << "Case #" << 1+ic << ": " << ride(R,k,0,0,0,true) << endl;
  }
}
