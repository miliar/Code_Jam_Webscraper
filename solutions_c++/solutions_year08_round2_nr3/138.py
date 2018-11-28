#define _CRT_SECURE_NO_DEPRECATE 
#include <string> 
#include <vector> 
#include <map> 
#include <list> 
#include <set> 
#include <queue> 
#include <iostream> 
#include <sstream> 
#include <stack> 
#include <deque> 
#include <cmath> 
#include <memory.h> 
#include <cstdlib> 
#include <cstdio> 
#include <cctype> 
#include <algorithm> 
#include <utility> 
using namespace std; 
typedef vector<int> vi; 
typedef vector<string> vs; 
typedef pair<int,int> pii; 
typedef long long ll; 
typedef istringstream iss;
#define FOR(i,f,n) for(int i=f; i<n; ++i) 
#define sz(a) ((int)a.size()) 
#define fill(w,v) memset(w,v,sizeof(w)) 
#define pb push_back 
#define all(a) a.begin(),a.end()
#define mp make_pair 
#define inf 1000000000 
#define X first
#define Y second
template<class T> inline T gcd(T a, T b){T t; while (a && b) t = a, a = b%a, b = t; return a+b; }
template<class T> inline T power(T a, int p) {T r = T(1); while (p) { if (p&1) r = r*a; a = a*a; p >>= 1; } return r; }
template<class T> T extgcd(T a, T b, T& x, T& y) { if (b==0) return x=1, y=0, a; T x1, y1, g; g = extgcd(b, a%b, x1, y1); x = y1; y = x1 - a/b*y1; return g; }

//struct Summator
//{
//	int a[1000001];
//	int N;
//
//	int prev(int x)
//	{
//		return x & (x-1);
//	}
//	int next(int x)
//	{
//		return (x<<1) - (x&(x-1));
//	}
//
//	int findSum(int l, int r)
//	{
//		int sum=0;
//		int x=r;
//		while (x>0)
//		{
//			sum += a[x];
//			x = prev(x);
//		}
//		x = l-1;
//		while (x>0) 
//		{
//			sum -= a[x];
//			x = prev(x);
//		}
//		return sum;
//	}
//
//	void modify(int p, int v)
//	{
//		int x = p;
//		while (x<=N)
//		{
//			a[x] += v;
//			x = next(x);
//		}
//	}
//};
//Summator s;
int N, M, K;

int a[1000001];
int find(int p, int fp)
{
	for (int i=fp; ; ++i)
	{
		if (i>=K) i-=K;
		if (!a[i])
		{
			--p;
			if (!p) return i;
		}
	}
}
/*
int Find(int p, int fp)
{
	int l=fp, r=fp+K-1;
	while (l < r)
	{
		int m = (l+r)/2;
		int sum;
		if (m > K)
		{
			sum = s.findSum(fp, K) + s.findSum(1, m-K);
		}
		else
		{
			sum = s.findSum(fp, m);
		}

		//if (sum == p) return m%K + 1;
		if (sum < p)
		{
			l = m+1;
		}
		else
		{
			r = m;
		}
	}
	if (r > K) return l-K; else return l;
}
*/

void solve()
{
//	s.N = K;
//	FOR(i,1,K+1) s.modify(i,1);
	//int p=1;
	//FOR(k,1,K+1)
	//{
	//	int pp = Find(k, p);
	//	a[pp] = k;
	//	s.modify(pp,-1);
	//	p = pp+1;
	//	if (p>K) p-=K;
	//}
	fill(a,0);
	int p=0;
	FOR(k,1,K+1)
	{
		int pp = find(k, p);
		a[pp] = k;
		p = (pp+1)%K;
	}
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif 

	int Q;
	scanf("%d", &Q);
	FOR(q,0,Q)
	{
		scanf("%d%d", &K, &N);
		solve();

		printf("Case #%d:", q+1);
		FOR(i,0,N)
		{
			int t;
			scanf("%d", &t);
			printf(" %d", a[t-1]);
		}
		printf("\n");
	}

	return 0;
} 
