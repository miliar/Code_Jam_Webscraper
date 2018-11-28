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
#define MAXPCNT 1000
#define MAXP 10001
int pr[MAXPCNT];
bool pp[MAXP];
int pcnt;
void genprimes(int M)
{
	FOR(i,2,M)
	{
		if (!pp[i])
		{
			pr[pcnt++] = i;
			for (int j=i+i; j<M; j+=i)
				pp[j] = true;
		}
	}
}

int r[MAXP];
int p[MAXP];
int find(int a)
{
	if (p[a] == -1) return a; else return a = find(p[a]);
}
void Union(int a, int b)
{
	int x = find(a);
	int y = find(b);
	if (x != y)
	{
		if (r[x] > r[y])
		{
			p[y] = x;
		}
		else
		{
			p[x] = y;
			if (r[x] == r[y])
				++r[y];
		}
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
	genprimes(1001);

	FOR(q,0,Q)
	{
		fill(p,-1);
		fill(r,0);
		ll A, B, P;
		scanf("%lld%lld%lld", &A, &B, &P);
		int i;
		for (i=0; i<pcnt; ++i)
		{
			if (pr[i]>=P) break;
		}
	
		for(;i<pcnt; ++i)
		{
			int tcnt=0;
			FOR(j,A,B+1)
			{
				if (j % pr[i]) continue;
				FOR(k,j+1,B+1)
				{
					if (k % pr[i] == 0)
					{
						Union(j,k);
					}
				}
			}
		}
		int res=0;
		FOR(i,A,B+1)
		{
			if (p[i] == -1) ++res;
		}
		printf("Case #%d: %d\n", q+1, res);
	}

	return 0;
} 
