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
#define pi 3.1415926535897932
#define ll long long
#define ld long double

using namespace std;

struct item{
	int b, e, w;
};

bool cmp(const item& a, const item& b){
	return a.w < b.w;
}

item a[3010];
int x, s, r, t, n;

ld f(ld t1, int b, int e, int w){
	if (b == e) return t1;
	if (t1 - t > 0.00000000001)
		return t1 + 1.0 * (e - b) / (1.0 * (s + w)); 
	ld t2 = t1 + 1.0 * (e - b) / (1.0 * (r + w));
	if (t2 - t < -0.00000000001) return t2;
	else return t + 1.0 * (e - b - (t - t1) * (r + w)) / (1.0 * (s + w));//b + (t - t1) * (r + w)
}

int main(){
#ifndef ONLINE_JUDGE
	freopen ("input.txt","rt",stdin);
	freopen ("output.txt","wt",stdout);
#endif
	int t2;
	cin >> t2;
	forn(qqq, t2){
		cin >> x >> s >> r >> t >> n;
		int n1 = n;
		forn(i, n)
			scanf("%d %d %d", &a[i].b, &a[i].e, &a[i].w);
		if (a[0].b > 0){
			a[n].b = 0;
			a[n].e = a[0].b;
			a[n ++].w = 0;
		}
		forn(i, n1 - 1)
			if (a[i].e < a[i + 1].b){
				a[n].b = a[i].e;
				a[n].e = a[i + 1].b;
				a[n ++].w = 0;
			}
		if (a[n1 - 1].e < x){
			a[n].b = a[n1 - 1].e;
			a[n].e = x;
			a[n ++].w = 0;
		}
		sort(a, a + n, cmp);
		//reverse(a, a + n);
		a[0].e = a[0].e - a[0].b;
		a[0].b = 0;
		for (int i = 1; i < n; i ++){
			int b1 = a[i].b;
			a[i].b = a[i - 1].e;
			a[i].e = a[i].b + (a[i].e - b1);
		}	
		int tek = 0;
		ld t1 = 0;
		for (int i = 0; i < n; i ++){
			if (tek < a[i].b){
				t1 = f(t1, tek, a[i].b, 0);
				tek = a[i].b;
			}
			t1 = f(t1, a[i].b, a[i].e, a[i].w);
			tek = a[i].e;
		}
		t1 = f(t1, a[n - 1].e, x, 0);
		printf ("Case #%d: %0.15f\n", qqq + 1, t1);
	}
	return 0;
}