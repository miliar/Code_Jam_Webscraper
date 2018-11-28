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

void calc(int no)
{
	int ns, nq;
	int i, j;
	string x;
	map<string, int> me;
	int ans = 0;
	
	cin >> ns;
	for (i = 0; i < ns; i++) {
		getline(cin, x);
		if (x.size() == 0 || x[0] == 13) getline(cin, x);
		me[x] = i;
	}
	cin >> nq;
	int q[nq];
	for (i = 0; i < nq; i++) {
		getline(cin, x);
		if (x.size() == 0 || x[0] == 13) getline(cin, x);
		q[i] = me[x];
	}
	
	int pos;
	int max_pos;
	for (pos = 0; pos < nq; ) {
		max_pos = pos;
		for (i = 0; i < ns; i++) {
			for (j = pos; j < nq && q[j] != i; j++) ;
			if (max_pos < j) max_pos = j;
		}
		pos = max_pos;
		ans++;
	}
	if (ans == 0) ans = 1;
	
	printf("Case #%d: %d\n", no, ans - 1);
	
	return;
}

int main()
{
	int n;
	int i;
	
	cin >> n;
	
	for (i = 0; i < n; i++) {
		calc(i + 1);
	}
	
	return 0;
}
