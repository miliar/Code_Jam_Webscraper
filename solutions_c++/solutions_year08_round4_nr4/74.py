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

int N, L, K;
char s[55000];
char sp[55000];
int perm[20];

void do_perm(int i)
{
	for (int j=0; j<K; ++j)
	{
		sp[j] = s[perm[j]];
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
		scanf("%d\n%s\n", &K, s);
		L = strlen(s);
		FOR(i,0,K) perm[i] = i;
		int mn=inf;
		do
		{
			for (int i=0; i<L; i+=K)
			{
				for (int j=0; j<K; ++j)
				{
					sp[i+j] = s[i+perm[j]];
				}
			}
			mn = min(mn, unique(sp, sp+L)-sp);
		}
		while (next_permutation(perm, perm+K));
		printf("Case #%d: %d\n", q+1, mn);
	}
	return 0;
} 
