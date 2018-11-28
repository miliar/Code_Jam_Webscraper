#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

void print_ans(vector<int> &ans)
{
	for (int i = 0; i < ans.size(); ++i) {
		if (i) cout << ", ";
		cout << (char) (ans[i] + 'A');
	}
	return;
}
void solve()
{
	int C, D, N;
	string x;
	vector<int> ans;
	int c[26][26];
	int d[26][26];
	memset(c, 0xFF, sizeof(c) );
	memset(d, 0x00, sizeof(d) );
	
	cin >> C;
	for (int i = 0; i < C; ++i) {
		cin >> x;
		int a = x[0] - 'A';
		int b = x[1] - 'A';
		int cc = x[2] - 'A';
		c[a][b] = c[b][a] = cc;
	}
	
	cin >> D;
	for (int i = 0; i < D; ++i) {
		cin >> x;
		int a = x[0] - 'A';
		int b = x[1] - 'A';
		d[a][b] = d[b][a] = 1;
	}
	
	cin >> N;
	cin >> x;
	for (int i = 0; i < x.size(); ++i) {
		ans.push_back(x[i] - 'A');
		while (true) {
			//print_ans(ans);
			//cout << endl;
			if (ans.size() <= 1) break;
			int a = ans[ans.size() - 1];
			int b = ans[ans.size() - 2];
			if (c[a][b] >= 0) {
				ans.pop_back();
				ans.pop_back();
				ans.push_back(c[a][b]);
				continue;
			}
			break;
		}
		for (int j = 0; j + 1 < ans.size(); ++j) {
			for (int k = j + 1; k < ans.size(); ++k) {
				if (d[ans[j]][ans[k]] == 1) ans.clear();
			}
		}
	}
	for (int i = 0; i < ans.size(); ++i) {
		if (i) cout << ", ";
		cout << (char) (ans[i] + 'A');
	}
	return;
}

int main()
{
	int T;
	
	cin >> T;
	
	for (int i = 0; i < T; ++i) {
		cout << "Case #" << i + 1 << ": [";
		solve();
		cout << "]" << endl;
	}
	return 0;
}