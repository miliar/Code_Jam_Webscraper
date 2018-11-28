/*
ID: gupan881
PROG: A
LANG: C++
*/
#include <iostream>
#include <sstream>
#include <cstring>
#include <string>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <bitset>
#include <vector>
#include <stack>
#include <list>
#include <utility>
#include <queue>
#include <set>
#include <map>
using namespace std;
#define MP make_pair
typedef pair<int,int> PII;
int main() 
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int i,j,k,cs;
	cin >> cs;
	for(k = 1; k <= cs; k++) {
		int x,r,s,n;
		double t;
		vector<PII> v;
		cin >> x>>s>>r>>t>>n;
		int len = 0;
		r -= s;
		for(i = 0; i < n; i++) {
			int b, e, w;
			cin >> b >> e >> w;
			v.push_back(MP(w+s,e-b));
			len += e-b;
		}
		v.push_back(MP(s,x-len));
		sort(v.begin(), v.end());
		v.push_back(MP(100000,0));
		int pre = 0;
		vector<PII> v2;
		for(i = 0; i < v.size(); i++) {
			if(i == 0 || v[i].first == v[i-1].first)
				pre += v[i].second;
			else {
				v2.push_back(MP(v[i-1].first,pre));
				pre = v[i].second;
			}
		}
		int l = v2.size();
		double ans = 0;
		for(i = 0; i < l; i++) {
			if(t == 0) {
				ans += v2[i].second*1.0/v2[i].first;
				continue;
			}
			double tt = v2[i].second*1.0/(v2[i].first+r);
			if(tt < t) {
				ans += tt;
				t -= tt;
			} else {
				ans += t;
				ans += (v2[i].second*1.0-t*(r+v2[i].first))/v2[i].first;
				t = 0;
			}
		}
		printf("Case #%d: %lf\n", k, ans);
	}
	return 0;
}
