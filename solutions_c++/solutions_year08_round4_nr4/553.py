#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <queue>
#include <map>
#include <set>
using namespace std;

vector<vector<int> > p(6);

void make_p(int i, vector<int> k, vector<int> l) {
	int j;
	vector<int> m;
	
	if (l.size() == i) {
		for (j = 0; j < i; j++) {
			p[i].push_back(l[j]);
			//printf("%d, ", l[j]);
		}
		//printf("\n");
		return;
	}
	
	for (j = 0; j < i; j++) {
		if (k[j] == 0) {
			k[j] = 1;
			m = l;
			m.push_back(j);
			make_p(i, k, m);
			k[j] = 0;
		}
	}
	
	return;
}

void calc(int no)
{
	int k;
	int min_ans = INT_MAX;
	int i, j;
	string x, y;
	
	cin >> k;
	cin >> x;
	
	for (i = 0; i < p[k].size(); i += k) {
		y = x;
		for (j = 0; j < x.size(); j++) {
			int n = j - (j % k);
			y[j] = x[n + p[k][i + j % k] ];
		}
		int ans = 1;
		for (j = 1; j < y.size(); j++) {
			if (y[j] != y[j - 1]) ans++;
		}
		//cout << y << "-" << ans << endl;
		if (min_ans > ans) min_ans = ans;
	}
	
	printf("Case #%d: %d\n", no, min_ans);
	
	return;
}

int main()
{
	int n;
	int i, j;
	
	cin >> n;
	
	vector<int> k, l;
	
	for (i = 2; i < 6; i++) {
		k.clear();
		k.resize(i, 0);
		l.clear();
		make_p(i, k, l);
	}
	
	for (i = 0; i < n; i++) {
		calc(i + 1);
	}
	
	return 0;
}
