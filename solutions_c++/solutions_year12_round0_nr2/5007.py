#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
 
using namespace std;
 
#define FOR(i,a,b) for(__typeof(b) i=(a);i!=(b);i++)
#define REP(i,n) FOR(i,0,n)
#define ALL(a) a.begin(),a.end()
#define EACH(i,a) FOR(i,a.begin(),a.end())
#define PB push_back
#define iss istringstream
#define SZ(a) (int)a.size()
#define CLEAR(a) memset(a,0,sizeof(a))
#define ll long long
 
 const int MAXN = 105;
 
 int mem[MAXN];
 int dp[MAXN];
 
int T, N, S, p;
 
int main() {
	cin >> T;
	for(int t = 1 ; t <= T ; t++) {
		cin >> N;
		cin >> S;
		cin >> p;
		for(int i = 0 ; i < N ; i++) {cin >> mem[i];}
		int ans = 0;
		int left = S;
		for(int i = 0 ; i < N ; i++) {
			int m = mem[i] / 3;
			if ((mem[i] % 3) != 0) {m++;}
			if (m >= p) {ans++;continue;}
			
			if (left == 0) {continue;}
			if ((mem[i] % 3) == 0) {
				if ((mem[i] /3) + 1 >= p && mem[i] != 0) {
					left--;
					ans++;
					continue;
				}
			}	else if ((mem[i] %3) == 2) {
				if ((mem[i] / 3) + 2 >= p) {
					left--;
					ans++;
					continue;
				}
			}
		}
		cout << "Case #" << t << ": " << ans << endl;
	}



	return 0;
}
