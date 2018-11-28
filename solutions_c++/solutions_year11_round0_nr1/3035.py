#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
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
#include <ctime>
 
#define forn(i,n) for (int i = 0; i < (int)(n); i++)
#define forv(i,a) for (int i = 0; i < a.size(); i++)
#define sz size()
#define mp make_pair
#define pb push_back
#define VI vector< int >
#define PII pair< int, int>
#define inf (100000000)
#define all(a) a.begin(),a.end()
#define have(msk, i) (!!((1<<(i)) & msk))
#define pi 3.1415926535897932384626433832795
#define sqr(a) ((a) * (a))
#define eps 1e-9
using namespace std;

void solve(int testNumber) {
	int n;
	string u;
	int v;
	vector< PII > seq;

	scanf("%d", &n);

	forn(i, n) {
		cin >> u >> v;
		int q = u  == "O";
		seq.push_back(mp(q, v));
	}
	int last_move_time[2] = {0,0};
	int cur_pos[2] = {1, 1};
	int cur_time = 0;

	forn(i, n) {
		int len = abs(cur_pos[seq[i].first] - seq[i].second);
		cur_time += max(len - (cur_time - last_move_time[seq[i].first]), 0)+1;
		cur_pos[seq[i].first] = seq[i].second;
		last_move_time[seq[i].first] = cur_time;
	}

	printf("Case #%d: %d\n", testNumber, cur_time);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int t;
	scanf("%d", &t);

	forn(i, t) {
		solve(i+1);
	}

	return 0;
}
