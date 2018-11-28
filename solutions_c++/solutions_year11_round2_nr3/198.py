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

vector<int> ans;
int N, M;

vector<vector<int> > shape;

void divide(int x, int y)
{
	vector<vector<int> > sh2(shape);
	
	shape.clear();
	for (int i = 0; i < sh2.size(); ++i) {
		if (find(sh2[i].begin(), sh2[i].end(), x) == sh2[i].end() || find(sh2[i].begin(), sh2[i].end(), y) == sh2[i].end() ) {
			shape.push_back(sh2[i]);
			continue;
		}
		vector<int> s1, s2;
		bool found = false;
		for (int j = 0; j < sh2[i].size(); ++j) {
			if (sh2[i][j] == x || sh2[i][j] == y) {
				s1.push_back(sh2[i][j]);
				s2.push_back(sh2[i][j]);
				found = !found;
			} else if (found) s2.push_back(sh2[i][j]);
			else s1.push_back(sh2[i][j]);
		}
		sort(s1.begin(), s1.end() );
		sort(s2.begin(), s2.end() );
		shape.push_back(s1);
		shape.push_back(s2);
	}
	
	return;
}

bool get_next(vector<int> &l, int n)
{
	for (int i = l.size() - 1; i > 0; --i) {
		if (l[i] < n) {
			++l[i];
			return true;
		} else l[i] = 1;
	}
	return false;
}

bool check(vector<int> &l, int n)
{
	//cout << "CHECK : ";
	//for (int i = 0; i < l.size(); ++i) cout << l[i];
	//cout << " - " << n << endl;
	
	for (int i = 0; i < shape.size(); ++i) {
		vector<bool> ok(n, false);
		for (int j = 0; j < shape[i].size(); ++j) {
			ok[l[shape[i][j]] - 1] = true;
		}
		if (count(ok.begin(), ok.end(), true) != n) return false;
	}
	//cout << "CHECK - OK" << endl;
	ans = l;
	return true;
}
int solve()
{
	vector<int> x(M), y(M);
	for (int i = 0; i < M; ++i) cin >> x[i];
	for (int i = 0; i < M; ++i) cin >> y[i];
	
	shape.clear();
	vector<int> sh(N);
	for (int i = 0; i < N; ++i) sh[i] = i;
	shape.push_back(sh);
	for (int i = 0; i < M; ++i) {
		divide(x[i] - 1, y[i] - 1);
	}
	
	ans.resize(N, 1);
	int ansC = 1;
	
	int maxans = N;
	for (int i = 0; i < shape.size(); ++i) maxans = min(maxans, (int) shape[i].size() );
	
	for (int i = 2; i <= maxans; ++i) {
		vector<int> l(N, 1);
		while (get_next(l, i) ) {
			if (check(l, i) ) {
				ansC = i;
				break;
			}
		}
	}
	
	return ansC;
}

int main()
{
	int T;
	
	cin >> T;
	
	for (int i = 0; i < T; ++i) {
		cin >> N >> M;
		ans.clear();
		int ret = solve();
		printf("Case #%d: %d\n", i + 1, ret);
		for (int i = 0; i < ans.size(); ++i) {
			if (i) cout << " ";
			cout << ans[i];
		}
		cout << endl;
	}
	return 0;
}