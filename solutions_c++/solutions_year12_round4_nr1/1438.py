#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <set>
#include <map>
using namespace std;

int N;
vector<int> D, L;
int G;
map<pair<int, int>, bool> memo;

bool rec(int p, int h)
{
	if (memo.find(make_pair(p, h)) != memo.end() ) return memo[make_pair(p, h)];
	
	bool ret = false;
	int x = min(D[h] + D[h] - p, D[h] + L[h]);
	if (x >= G) {
		memo[make_pair(p, h)] = true;
		//printf("rec(%d,%d) = true\n", p, h);
		return true;
	}
	for (int i = h + 1; i < N; ++i) {
		if (D[i] > x) break;
		if (rec(D[h], i) == true) {
			ret = true;
			//printf("rec(%d,%d) = true\n", p, h);
			break;
		}
	}
	
	memo[make_pair(p, h)] = ret;
	return ret;
}

void solve(int case_no)
{
	
	cin >> N;
	D.resize(N);
	L.resize(N);
	memo.clear();
	
	for (int i = 0; i < N; ++i) {
		cin >> D[i] >> L[i];
	}
	cin >> G;
	
	if (rec(0, 0) ) cout << "YES" << endl;
	else cout << "NO" << endl;
	return;
}

int main()
{
	int T;
	
	cin >> T;
	
	for (int i = 1; i <= T; ++i) {
		printf("Case #%d: ", i);
		solve(i);
	}
	
	return 0;
}
