#define _CRT_SECURE_NO_DEPRECATE 
#include <string> 
#include <vector> 
#include <map> 
#include <set> 
#include <queue> 
#include <iostream> 
#include <sstream> 
#include <deque> 
#include <cmath> 
#include <memory.h> 
#include <algorithm> 
using namespace std; 

typedef vector<int> vi; 
typedef vector<string> vs; 
typedef pair<int,int> pii; 
typedef long long ll; 
#define fill(w,v) memset(w,v,sizeof(w)) 
#define FOR(i,f,n) for(int i=f; i<n; ++i) 
#define pb push_back 
#define mp make_pair 
#define sz(a) ((int)a.size()) 
#define all(a) a.begin(),a.end()
#define inf 1000000000 

ll A[1101];
ll B[1101];
ll X, Y, Z;
int n, m;
void gen()
{
	FOR(i,0,n)
	{
		B[i] = A[i%m];
		A[i%m] = (X * A[i%m] + Y * (i + 1)) % Z;
	}
}
ll MOD = 1000000007LL;
ll mem[1111];
ll F(int p)
{
	ll &r = mem[p];
	if (r != -1) return r;
	r = 1;
	if (p == 0) return r=1;
	for (int i=p-1; i>=0; --i)
	{
		if (B[i] < B[p])
		{
			r += F(i);
			r %= MOD;
		}
	}
	return r;
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int Tasks;
	scanf("%d", &Tasks);
	FOR(task,0,Tasks)
	{
		scanf("%d%d%lld%lld%lld", &n, &m, &X, &Y, &Z);
		FOR(i,0,m)
		{
			scanf("%lld", &A[i]);
		}
		gen();
		B[n] = MOD;
		fill(mem,-1);

		ll res=F(n);
		printf("Case #%d: %lld\n", task+1, res-1);
	}
	return 0;
} 
