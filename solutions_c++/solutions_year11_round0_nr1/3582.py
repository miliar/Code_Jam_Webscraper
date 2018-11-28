#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <utility>
#include <limits>
#include <complex>
#include <string>
#include <vector>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <list>
#include <bitset>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int uint;
typedef pair<int,int> pii;
typedef vector<int> vint;
typedef set<int> sint;
typedef long double ld;

#define rep(i, a, b) for(int i=(a); i<(b); ++i)
#define clr(a, v) memset((a), (v), sizeof(a))
#define sz(a) ((int)(a).size())
#define all(a) (a).begin(), (a).end()

int const inf = 0x7f7f7f7f;
ll const llinf = 0x7f7f7f7f7f7f7f7fll;
ld const eps = 1e-9;

void frr(){	freopen("test.in", "r", stdin); }

template<typename T> inline bool setmin(T &a, T const &b) { if(b < a) { a = b; return true; } else return false; }
template<typename T> inline bool setmax(T &a, T const &b) { if(a < b) { a = b; return true; } else return false; }

template<typename A, typename B> inline A& _0(pair<A, B> &p) { return p.first; }
template<typename A, typename B> inline B& _1(pair<A, B> &p) { return p.second; }
template<typename A> inline A _0(complex<A> &z) { return z.real(); }
template<typename A> inline A _1(complex<A> &z) { return z.imag(); }
template<typename A> inline A& _0(A *p) { return p[0]; }
template<typename A> inline A& _1(A *p) { return p[1]; }

int const max_n = 128;
int dist[max_n][max_n][max_n];
int robot[max_n], button[max_n];

int test_case = 0;

queue<int> q;
void transit(int robot_0, int robot_1, int press, int new_dist)
{
	if (1 <= robot_0 && robot_0 <= 100 && 1 <= robot_1 && robot_1 <= 100 && dist[robot_0][robot_1][press] == -1) {
		dist[robot_0][robot_1][press] = new_dist;
		q.push(robot_0);
		q.push(robot_1);
		q.push(press);
	}
}

void solve_case()
{
	++ test_case;
	int n; scanf("%d", &n); 
	rep (i, 0, n) {
		char r;
		int b;
		scanf(" %c %d", &r, &b);
		robot[i] = (r == 'O') ? 0 : 1;
		button[i] = b;
	}

	clr(dist, -1);
	while(!q.empty()) q.pop();

	int robot_0 = 1, robot_1 = 1, press = 0, curr_dist = 0;
	transit(robot_0, robot_1, press, curr_dist);

	while (!q.empty()) {
		robot_0 = q.front(); q.pop();
		robot_1 = q.front(); q.pop();
		press = q.front(); q.pop();
		curr_dist = dist[robot_0][robot_1][press];

		if (press == n) {
			break;
		}

		if (robot[press] == 0 && robot_0 == button[press]) {
			transit (robot_0, robot_1, 1 + press, 1 + curr_dist);
			transit (robot_0, robot_1 + 1, 1 + press, 1 + curr_dist);
			transit (robot_0, robot_1 - 1, 1 + press, 1 + curr_dist);
		}
		
		if (robot[press] == 1 && robot_1 == button[press]) {
			transit (robot_0, robot_1, 1 + press, 1 + curr_dist);
			transit (robot_0 + 1, robot_1, 1 + press, 1 + curr_dist);
			transit (robot_0 - 1, robot_1, 1 + press, 1 + curr_dist);
		}

		transit (robot_0 - 1, robot_1 - 1, press, 1 + curr_dist);
		transit (robot_0 - 1, robot_1 + 0, press, 1 + curr_dist);
		transit (robot_0 - 1, robot_1 + 1, press, 1 + curr_dist);
		transit (robot_0 + 0, robot_1 - 1, press, 1 + curr_dist);
		transit (robot_0 + 0, robot_1 + 1, press, 1 + curr_dist);
		transit (robot_0 + 1, robot_1 - 1, press, 1 + curr_dist);
		transit (robot_0 + 1, robot_1 + 0, press, 1 + curr_dist);
		transit (robot_0 + 1, robot_1 + 1, press, 1 + curr_dist);
	}

	printf("Case #%d: %d\n", test_case, dist[robot_0][robot_1][press]);
}

int main()
{
	//frr();
	int t; scanf("%d", &t);
	while(t--) solve_case();
	return 0;
}
