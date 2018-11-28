#include <iostream>
#include <string>
#include <map> 
#include <math.h>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <set>
#include <queue>
#include <sstream>


using namespace std;

#define sqr(x) ((x)*(x))
#define ll long long

int gcd(int a, int b) {
	while (b) b^=a^=b^=a%=b;
	return a;
}

const int maxn=100100;

int n;
pair<int,pair<int,int>> a[maxn];

bool cmp(pair<int,pair<int,int>> &a, pair<int,pair<int,int>> &b) {
	return a.first > b.first || a.first==b.first && a.second<b.second;
}

void solve(int test) {
	cout << "Case #" << test << ": ";
	cin >> n;
	for (int i=0; i<n; i++) 
		cin >> a[i].second.second;
	for (int i=0; i<n; i++) 
		cin >> a[i].first;
	for (int i=0; i<n; i++)
		a[i].second.first=i;
	sort(a,a+n,cmp);
	for (int i=0; i<n; i++)
		cout << a[i].second.first << " ";
	cout << endl;
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int tests;
	cin >> tests;
	for (int test=1; test<=tests; test++) {
		solve(test);
	}


	return 0;
}