#define _CRT_SECURE_NO_DEPRECATE
#define _ASSERTE

#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <ctime>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define fore(i, a, b) for(int i = a; i < (int)(b); ++i)
#define pii pair<int,int>
#define pb push_back
#define mp make_pair
#define all(a) a.begin,a.end()
#define ll long long
#define EPS 1e-14
#define delta 1e-9

pii a[2000];

bool cmp1(pii a, pii b) {
	return a.first * a.second < b.first * b.second;
}

int main(){
	
#ifndef ONLINE_JUDGE
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	int tt;
	cin >> tt;
	forn(t, tt) {
		int n;
		cin >> n;
		forn(i, n) {
			cin >> a[i].first;
		}
		forn(i, n) {
			cin >> a[i].second;
			a[i].first *= a[i].second;
			a[i].second = -i;
		}
		sort(a, a + n);
		reverse(a, a + n);
	
	
		cout << "Case #" << (t + 1) << ": ";
		forn(i, n)
			cout << -a[i].second << " ";
		puts("");
	}

	return 0;
}
