#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;
const int eps = 1e-6;
int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int Case;
	scanf("%d", &Case);
	for (int c = 1; c <= Case; c++) {
		int x, s, r, t, n, empty;
		vector<pair<int, int> > CI;
		scanf("%d%d%d%d%d", &x, &s, &r, &t, &n);
		empty = x;
		for (int i = 0; i < n; i++) {
			int low, high, speed;
			scanf("%d%d%d", &low, &high, &speed);
			empty -= (high - low);
			CI.push_back(make_pair(speed, high - low));
		}
		sort(CI.begin(), CI.end());
		double tt = t;
		double ans;
		if (empty < tt * r) {
			ans = empty * 1.0 / r;
			tt -= empty * 1.0 / r;
		}
		else {
			ans = (empty - tt * r) / s + tt;
			tt = 0;
		}
		for (int i = 0; i < CI.size(); i++) {
			if (tt < eps) {
				ans += CI[i].second * 1.0 / (CI[i].first + s);
			}
			else {
				if (CI[i].second < tt * (CI[i].first + r)) {
					ans += CI[i].second * 1.0 / (CI[i].first + r);
					tt -= CI[i].second * 1.0 / (CI[i].first + r);
				}
				else {
					ans += (CI[i].second- tt * (CI[i].first + r)) / (CI[i].first + s) + tt;
					tt = 0;
				}
			}
		}
		printf("Case #%d: %lf\n", c, ans);
	}
}