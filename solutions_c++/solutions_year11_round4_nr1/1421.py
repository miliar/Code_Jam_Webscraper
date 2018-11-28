#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

struct W
{
  int b, e, w;
};

double dp[1000001];
int prev[1000001];
int speed[1000001];

int main()
{
  int T;
  
  cin >> T;

  for (int cas = 1; cas <= T; cas++) {
    int X, S, R, T, N;
    cin >> X >> S >> R >> T >> N;
    
    set<int> pos;
    vector<W> ws;
    for (int i = 0; i < N; i++) {
      int b, e, w;
      cin >> b >> e >> w;

      pos.insert(b);
      pos.insert(e);

      W z = {b,e,w};
      ws.push_back(z);
    }

    pos.insert(0);
    pos.insert(X);

    for (int i = 0; i < 1000001; i++) dp[i] = 10000001.0;
    dp[0] = 0.0;
    prev[0] = -1;

    for (set<int>::iterator pi = pos.begin(); pi != pos.end(); ++pi) {
      int x = *pi;
      for (size_t i = 0; i < ws.size(); i++) {
	if (ws[i].b == x) {
	  int y = ws[i].e;
	  double t = dp[x] + (double)(y - x) / (ws[i].w + S);
	  if (dp[y] > t) {
	    dp[y] = t;
	    prev[y] = ws[i].b;
	    speed[y] = ws[i].w + S;
	  }
	}
	if (ws[i].b > x) {
	  int y = ws[i].b;
	  double t = dp[x] + (double)(ws[i].b - x) / S;
	  if (dp[y] > t) {
	    dp[y] = t;
	    prev[y] = x;
	    speed[y] = S;
	  }
	}
      }
      double t = dp[x] + (double)(X - x) / S;
      if (dp[X] > t) {
	dp[X] = t;
	prev[X] = x;
	speed[X] = S;
      }
    }
    map<int, int> route;
    for (int x = X; prev[x] >= 0; x = prev[x]) {
      route[speed[x]] += x - prev[x];
    }

    double rest = T;
    double tot = 0;
    for (map<int, int>::iterator i = route.begin(); i != route.end(); ++i) {
      double sp = i->first;
      int len = i->second;
      double rsp = sp + R - S;
      //cout << sp << ", " << len << ", " << rsp << endl;
      if (len / rsp >= rest) {
	tot += rest + (len - rsp * rest) / sp;
	rest = 0;
      } else {
	tot += len / rsp;
	rest -= len / rsp;
      }
      //cout << tot << ", " << rest  << endl;
    }

    cout.precision(10);
    cout << "Case #" << cas << ": " << tot << endl;
  }

  return 0;
}
