#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define sz(a) int((a).size())
#define all(X) (X).begin(), (X).end()
typedef vector<int> vi;
typedef vector<string> vs;
typedef long long ll;

vector<int> vv[100];
vector<int> v;
int ret;
int n;

void dfs(int cur, int nv)
{
	if (cur == n) {
		int minn = 0x7FFFFFFF;
		for (int i = 0; i < nv; ++i) {
			minn = min(minn, sz(vv[i]));
		}
		if (minn == 0x7FFFFFFF) {
			minn = 0;
		}
		ret = max(ret, minn);
	}
	else {
		vv[nv].push_back(v[cur]);
		dfs(cur + 1, nv + 1);
		vv[nv].pop_back();
		for (int i = 0; i < nv; ++i) {
			if (vv[i].back() + 1 == v[cur]) {
				vv[i].push_back(v[cur]);
				dfs(cur + 1, nv);
				vv[i].pop_back();
			}
		}
	}
}

int run()
{
	scanf("%d", &n);
	/*v.clear();
	for (int i = 0; i < n; ++i) {
		int num;
		scanf("%d", &num);
		v.push_back(num);
		vv[i].clear();
	}
	sort(all(v));
	ret = 0;
	dfs(0, 0);
	return ret;*/
	map<int, int> mp;
	for (int i = 0; i < n; ++i) {
		int num;
		scanf("%d", &num);
		++mp[num];
	}

	int ret = 0x7FFFFFFF;
	while (!mp.empty()) {
		int len = 0;
		int last = 0;
		int lastct = 0;
		for (map<int, int>::iterator mi = mp.begin(); mi != mp.end(); ++mi) {
			if (mi == mp.begin()) {
				last = mi->first;
				++len;
				mi->second -= 1;
				lastct = mi->second;
			}
			else {
				if (mi->first != last + 1) {
					break;
				}
				else {
					if (mi->second <= lastct) {
						break;
					}
					++last;
					++len;
					mi->second -= 1;
					lastct = mi->second;
				}
			}
		}
		ret = min(ret, len);
		map<int, int> next;
		for (map<int, int>::iterator mi = mp.begin(); mi != mp.end(); ++mi) {
			if (mi->second != 0) {
				next[mi->first] = mi->second;
			}
		}
		mp = next;
	}
	if (ret == 0x7FFFFFFF) ret = 0;
	return ret;
}

int main()
{
	freopen("B4.in", "r", stdin);
	freopen("B4.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		printf("Case #%d: %d\n", i, run());
	}
	return 0;
}