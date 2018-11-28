#include <cstdlib>
#include <cstring>
#include <memory>
#include <cstdio>
#include <fstream>
#include <iostream>
#include <cmath>
#include <string>
#include <sstream>
#include <stack>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

#define DEBUG_FLAG 1
#if DEBUG_FLAG
#define dbg(...) cerr << #__VA_ARGS__ << ": " << __VA_ARGS__ << endl
#define cdbg(...) cerr << __VA_ARGS__ << endl
#else
#define debug(r)
#define dbg(...)
#endif


int main() {
	string fname = "A-small-attempt2";
	freopen((fname+".in").c_str(), "r", stdin);
	freopen((fname+".out").c_str(), "w", stdout);
	int T;
	scanf("%d", &T);
    string t[] = {"OFF","ON"};
    string s;
	for (int c = 1; c <= T; ++c) {
		int n, k;
		scanf("%d%d", &n, &k);
        int l=1<<n;
        k = k%l;
		if (k == l-1) {
            s = t[1];
        } else {
            s = t[0];
        }
        printf("Case #%d: %s\n", c, s.c_str());
	}
    
	return 0;
}

