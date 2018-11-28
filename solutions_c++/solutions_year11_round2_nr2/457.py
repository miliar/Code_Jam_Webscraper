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
using namespace std;

int C, D;

bool check(vector<int> &pos)
{
	for (int i = 0; i < pos.size() - 1; ++i) {
		if (pos[i] + D > pos[i + 1]) return false;
	}
	return true;
}
int solve()
{
	vector<int> pos;
	pos.clear();
	
	for (int i = 0; i < C; ++i) {
		int p, v;
		cin >> p >> v;
		p *= 2;
		for (int j = 0; j < v; ++j) pos.push_back(p);
	}
	
	int N = pos.size();
	sort(pos.begin(), pos.end() );
	int ans = 0;
	while (!check(pos) ) {
		vector<bool> move(N, false);
		++ans;
		--pos[0];
		for (int i = 1; i < N; ++i) {
			if (pos[i] - pos[i - 1] > D) --pos[i];
			else if (pos[i] - pos[i - 1] == D) ;
			else ++pos[i];
		}
	}
	return ans;
}

int main()
{
	int T;
	
	cin >> T;
	
	for (int i = 0; i < T; ++i) {
		cin >> C >> D;
		D *= 2;
		int ans = solve();
		printf("Case #%d: %.1f\n", i + 1, (double) ans / 2.0f);
	}
	return 0;
}