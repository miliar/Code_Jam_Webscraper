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
#include <cstring>
#include <climits>
using namespace std;

#define SQR(x)  ((x) * (x) )

void solve(int problem_no)
{
	int n;
	cin >> n;
	vector<string> m(n);
	set<vector<string> > s;
	queue<pair<vector<string>, int> > q;
	for (int i = 0; i < n; ++i) {
		cin >> m[i];
	}
	s.insert(m);
	q.push(make_pair(m, 0) );
	while (!q.empty() ) {
		pair<vector<string>, int> p = q.front();
		q.pop();
		vector<string> x = p.first;
		int mv = p.second;
		bool is_ok = true;
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				if (j > i && x[i][j] == '1') is_ok = false;
			}
		}
		if (is_ok) {
			printf("Case #%d: %d\n", problem_no, mv);
			return;
		}
		for (int i = 0; i < n - 1; ++i) {
			swap(x[i], x[i + 1]);
			if (s.find(x) == s.end() ) {
				s.insert(x);
				q.push(make_pair(x, mv + 1) );
			}
			swap(x[i], x[i + 1]);
		}
	}
	
	
	return;
}
		
int main()
{
	int n;
	cin >> n;
	
	for (int i = 1; i <= n; ++i) {
		if (i % 100 == 0) {
			cerr << "SOLVE " << i << "/" << n << endl;
		}
		solve(i);
	}
	
	return 0;
}

