#pragma comment(linker, "/STACK:64000000")
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cassert>
#include <ctime>
#include <deque>

#define forn(i, n) for (int i = 0; i < int(n); i ++)
#define ford(i, n) for (int i = int(n) - 1; i >= 0; i --)
#define mp make_pair
#define pb push_back
#define x first
#define y second
#define pi 3.1415926535897932
#define ll long long
#define ld long double

using namespace std;

bool pr[1010];
int kol[1010];
int st[1010];
vector <int> a;

int main(){
#ifndef ONLINE_JUDGE
	freopen ("input.txt","rt",stdin);
	freopen ("output.txt","wt",stdout);
#endif
	for (int i = 2; i < 1010; i ++)
		if (!pr[i]){
			for (int j = 2 * i; j < 1010; j += i)
				pr[j] = true;
			a.pb(i);
		}
	for (int i = 2; i < 1010; i ++)
		kol[i] = kol[i - 1] + !pr[i];
	int t1;
	cin >> t1;
	forn(qqq, t1){
		int n;
		memset(st, 0, sizeof(st));
		cin >> n;
		if (n == 1){
			printf ("Case #%d: %d\n", qqq + 1, 0);
			continue;
		}
		int minn = kol[n], maxx = 1;
		for (int i = 2; i <= n; i ++){
			int k = i;
			bool q1 = false;
			for (int j = 0; j < a.size() && a[j] <= k; j ++){
				int kol1 = 0;
				while ((k % a[j]) == 0){
					k /= a[j];
					kol1 ++;
				}
				if (kol1 > st[a[j]]){
					q1 = true;
					st[a[j]] = kol1;
				}
			}
			if (q1) maxx ++;
		}
		printf ("Case #%d: %d\n", qqq + 1, maxx - minn);
	}
	return 0;
}