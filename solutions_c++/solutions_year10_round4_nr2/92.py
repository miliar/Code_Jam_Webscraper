#include <iostream>
#include <string>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;

typedef long long ll;

int prices[1100];
int m[1100];
int p;
int q;


ll costs[2200][12];

ll addcost(ll x, ll y) {
  if (x == -2 || y == -2) {
    return -2;
  }
  return x + y;
}

ll mincost(ll x, ll y) {
  if (x == -2) {
    return y;
  }
  if (y == -2) {
    return x;
  }
  if (x < y) {
    return x;
  }
  return y;
}
	      

ll subtreeCost(int node, int holes) {
  // 1  23  4567 (8 teams)
  if (node >= q) {
    // team entry node
    if (holes > m[node - q]) {
      return -2;
    } else {
      return 0;
    }
  }
  if (costs[node][holes] != -1) {
    return costs[node][holes];
  }

  ll prefillcost = addcost(subtreeCost(node*2, holes), subtreeCost(node*2+1, holes));
  ll fillcost = addcost(prefillcost, prices[node]);
  ll opencost = addcost(subtreeCost(node*2, holes+1), subtreeCost(node*2+1, holes+1));

  ll mcost = mincost(fillcost, opencost);
  costs[node][holes] = mcost;

  return mcost;
}

int main() {
  int t;
  cin >> t;
  for (int casenum = 1; casenum <= t; ++casenum) {
    cin >> p;
    q = (1 << p);

    
    for (int i = 0; i < q; ++i) {
      cin >> m[i];
    }

    int foo = p;
    while (--foo >= 0) {
      int n = (1 << foo);
      for (int i = 0; i < n; ++ i) {
	int node = n + i;
	for (int j = 0; j < 12; ++j) {
	  costs[node][j] = -1;
	}
	cin >> prices[node];
      }
    }
    


    // ok

    // each first round team pair indistinguishable

    // how much does a subtree cost if its future has N holes?

    // 0 <= N <= 10

    ll cst = subtreeCost(1, 0);


    cout << "Case #" << casenum << ": ";
    cout << cst;
    cout << endl;
  }
}
