#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <cassert>

using namespace std;

#define Forf(i,f,n) for(int i=(f);i<(n);++i)
#define For(i,n) for(int i=0;i<(n);++i)
#define foreach(it,m) for(typeof((m).begin()) it = (m).begin();it!=(m).end();++it) 

typedef pair<int,int> PII;

int M;


PII compute_and(const vector<PII> &dp, int i) {
  int v = dp[2*i].second + dp[2*i+1].second;
  if (v>M) v = M;
  PII ans;
  ans.second = v;
  
  v = min( dp[2*i].second + dp[2*i+1].first,
	   min(dp[2*i].first + dp[2*i+1].first,
	       dp[2*i].first + dp[2*i+1].second) );
  if (v>M) v = M;
  ans.first = v;
  return ans;
}

PII compute_or(const vector<PII> &dp, int i) {
  int v = dp[2*i].first + dp[2*i+1].first;
  if (v>M) v = M;
  PII ans;
  ans.first = v;
  
  v = min( dp[2*i].second + dp[2*i+1].first,
	   min(dp[2*i].second + dp[2*i+1].second,
	       dp[2*i].first + dp[2*i+1].second) );
  if (v>M) v = M;
  ans.second = v;
  return ans;
}

void debug(const vector<PII> &gates, const vector<PII> &dp) {
  Forf(i, 1, gates.size()) {
    cout << gates[i].first << "," << gates[i].second << " ";
  }
  cerr << endl << endl;

  Forf(i, 1, dp.size()) {
    cout << dp[i].first << "," << dp[i].second << " ";
  }
}

  
void solveit() {
  int V;
  cin >> M >> V;
  vector<PII> gates(M+1);
  
  int ng = (M-1)/2;
  int nl = (M+1)/2;
  Forf(i,1,ng+1) {
    int g, c;
    cin >> g >> c;
    assert(g>=0 and g<=1
	   and c>=0 and c<=1);
    gates[i] = PII(g, c);
  }

  Forf(i,ng+1,ng+nl+1) {
    PII p;
    cin >> p.first;
    gates[i] = p;
  }

  vector<PII> dp(gates.size(), PII(M, M));
  for(int i = ng+nl; i>=1; --i) {
    if (i>=ng+1) {
      if (gates[i].first==0) dp[i].first = 0;
      else dp[i].second = 0;
    }
    else {
      if (gates[i].second==0) {
	if (gates[i].first==0) dp[i] = compute_or(dp, i);
	else dp[i] = compute_and(dp, i);
      }
      else {
	PII por, pand;
	por = compute_or(dp, i);
	pand = compute_and(dp, i);


	//	if (i==3) {
	//  cerr << por.first << " " << por.second << endl;
	//  cerr << pand.first << " " << pand.second << endl;
	//}

	if (gates[i].first==0) {pand.first++; pand.second++;}
	else {por.first++; por.second++;}

	dp[i].first = min(pand.first, min( por.first, M));
	dp[i].second = min(pand.second, min( por.second, M));
      }
    }
  }

  //  debug(gates, dp);

  int val = (V==0)?dp[1].first:dp[1].second;
  if (val<M) {
    cout << val << endl;
  } else {
    cout << "IMPOSSIBLE" << endl;
  }
}


int main() {
  int N;
  cin >> N;
  For(c,N) {
    cout << "Case #" << (c+1) << ": ";
    solveit();
  }
}
