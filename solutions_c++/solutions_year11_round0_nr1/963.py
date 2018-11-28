#include <cstdio>
#include <vector>
#include <map>
#include <iostream>
using namespace std;
#define pb push_back
typedef vector<int> vint;
typedef pair<int, int> pii;
#define mp make_pair

void solve(int test) {
    printf("Case #%d: ", test);
    int N;
    cin >> N;
    int xO = 1, xB = 1;
    vector<pii> V;
    for(int i = 0; i < N; ++i) {
	char s[2];
	int b;
	scanf("%s %d", s, &b);
	V.pb(mp((int)*s, b));
    }
    int pO = 0, pB = 0;
    while(pO < V.size() && V[pO].first != 'O') {
	pO++;
    }
    while(pB < V.size() && V[pB].first != 'B') {
	pB++;
    }
    for(int t = 0; ; ++t) {
	if(pO == V.size() && pB == V.size()) {
	    printf("%d\n", t);
	    return;
	}
	bool click = false;
	if(pO < V.size()) {
	    if(V[pO].second == xO && pO < pB) {
		click = true;
		pO++;
		while(pO < V.size() && V[pO].first != 'O') {
		    pO++;
		}
	    }
	    else if(xO < V[pO].second) {
		xO++;
	    }
	    else if(xO > V[pO].second) {
		xO--;
	    }
	}
	if(pB < V.size()) {
	    if(!click && V[pB].second == xB && pB < pO) {
		pB++;
		while(pB < V.size() && V[pB].first != 'B') {
		    pB++;
		}
	    }
	    else if(xB < V[pB].second) {
		xB++;
	    }
	    else if(xB > V[pB].second) {
		xB--;
	    }
	}
    }
}


int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int t;
  scanf("%d", &t);
  for(int i = 1; i <= t; ++i) {
    solve(i);
  }
  return 0;
}
