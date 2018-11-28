#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<algorithm>
#include<map>
using namespace std;


int const maxS = 1000;
int n, s, q;
string a[maxS];
map<string, bool> memo;
int main()
{
	freopen("1.in", "r", stdin);
	freopen("1.out", "w", stdout);
	cin >> n;
	for (int cases(0); cases != n; ++cases) {
		cin >> s;
		getline(cin, a[0]);
		for (int i(0); i < s; ++i) getline(cin, a[i]);
		cin >> q;
		string tem;
		getline(cin, tem);
		int tot = 0, ans = 0;
		memo.clear();
		for (int i(0); i < q; ++i) {
			getline(cin, tem);
			if (memo.find(tem) == memo.end()) {
				memo[tem] = 1;
				++tot;
				if (tot == s) {
					++ans;
					tot = 1;
					memo.clear();
					memo[tem] = 1;
				}
			}
		}
		printf("Case #%d: %d\n", cases + 1, ans);
	}
}
