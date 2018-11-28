#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <math.h>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <vector>
#pragma comment (linker, "/STACK:256000000")
using namespace std;
const int maxn = 210;
int x[maxn];
int y[maxn];
int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int i,j,n,t,q;
	cin >> t;
	char ch;
	for (q=1;q<=t;++q) {
		vector <int> to[2];
		vector <int> num[2];
		cin >> n;
		int last[2]={1,1};
		for (i=1;i<=n;++i) {
			cin >> ch >> y[i];
			if (ch=='O')
				x[i] = 0;
			else x[i] = 1;
		}
		i = 1;
		int cnt, req, ans = 0, prev = 0;
		while (i <= n) {
			j = i;
			req = max(0, abs(y[j] - last[x[j]]) - prev);
			cnt = req + 1;
			last[x[j]] = y[j];
			while (j < n && x[j]==x[j+1]) {
				cnt += abs(y[j+1] - last[x[j]]) + 1;
				last[x[j]] = y[j+1];
				++j;
			}
			prev = cnt;
			ans += cnt;
			i = j + 1;
		}
		printf("Case #%d: %d\n",q,ans);
	}


	
	return 0;
}