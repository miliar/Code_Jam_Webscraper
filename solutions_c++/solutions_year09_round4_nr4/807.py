#ifdef LOCAL
#pragma warning(disable:4786)
#define ll __int64
#define FORMATLL "%I64d" 
#else
#define ll long long
#define FORMATLL "%lld"
#endif
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <list>
#include <complex>
#include <cstdio>
#include <string>
#include <stack>
#include <cctype>
#include <cassert>
#include <vector>
#include <cmath>
#include <ctime>
#include <cstring>
#include <functional>
#include <cstdlib>
#include <queue>
using namespace std;
#define trav(it,cont) for(it=(cont).begin(); it!=(cont).end(); ++it)
#define forn(i,n) for(i=0;(i)<(n);++i)
#define clr(a) memset(a,0,(sizeof a));
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))
using namespace std;

// template here

// template end

// global variable
int n;
typedef double T;
struct Pt
{
	T x, y, r;
	void scan(){scanf("%lf%lf%lf", &x, &y, &r);}
}pt[100];
Pt operator-(Pt a, Pt b)
{
	Pt c;
	c.x = a.x - b.x;
	c.y = a.y - b.y;
	return c;
}
T dot(Pt a, Pt b){return a.x * b.x + a.y * b.y;}
// global end


char input()
{
	int i, j, lv;
	scanf("%d", &n);
	forn(i,n){
		pt[i].scan();
	}
	
	return 1;
}

T solve( Pt c, Pt a, Pt b)
{
	T r = (sqrt(dot(a-b, a-b))+a.r + b.r)/2;
	r = MAX(r,c.r);
	return r;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("c:/out.txt", "w", stdout);
	
	int i, j, k, ca, ica, lv;
	scanf("%d", &ca);
	
	forn(ica,ca){
		input();

		T ans = 1e10;
		ans = MIN(ans,solve(pt[0],pt[1],pt[2]));
		ans = MIN(ans,solve(pt[1],pt[0],pt[2]));
		ans = MIN(ans,solve(pt[2],pt[1],pt[0]));
		printf("Case #%d: %.10lf\n", ica+1, ans);
		
	}
	return 0;
}
