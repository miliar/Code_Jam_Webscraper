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
#define MAX 100001
int x[MAX], y[MAX];

void gen(int N, int A, int B, int C, int D, int x0, int y0, int M)
{
	ll X=x0, Y=y0;
	FOR(i,0,N)
	{
		x[i] = X;
		y[i] = Y;
		X = (A*X + B) % M;
		Y = (C*Y + D) % M;
	}
}

bool ok(int i, int j, int k)
{
	ll xx = x[i];
	xx += x[j];
	xx += x[k];
	if (xx % 3) return false;
	xx = y[i];
	xx += y[j];
	xx += y[k];
	if (xx % 3) return false;
	return true;
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
		int N, A, B, C, D, x0, y0, M;
		scanf("%d%d%d%d%d%d%d%d", &N, &A, &B, &C, &D, &x0, &y0, &M);
		gen(N, A, B, C, D, x0, y0, M);

		int ost[3][3];
		fill(ost,0);
		FOR(i,0,N)
		{
			++ost[x[i]%3][y[i]%3];
		}

		ll res=0;
		FOR(i,0,3)
		FOR(I,0,3)
		FOR(j,0,3)
		FOR(J,0,3)
		FOR(k,0,3)
		FOR(K,0,3)
		{
			if ((i+j+k)%3 || (I+J+K)%3) continue;

			int ii = i*3+I;
			int jj = j*3+J;
			int kk = k*3+K;
			if (ii == jj && jj == kk)
			{
				ll N = ost[i][I];
				res += N*(N-1)*(N-2);
			}
			else if (ii != jj && jj != kk && ii != kk)
			{
				ll N = ost[i][I];
				N *= ost[j][J];
				N *= ost[k][K];
				res += N;
			}
			else if (ii == jj)
			{
				ll N = ost[i][I];
				res += N*(N-1)*ost[k][K];
			}
			else if (jj == kk)
			{
				ll N = ost[j][J];
				res += N*(N-1)*ost[i][I];
			}
			else if (ii == kk)
			{
				ll N = ost[i][I];
				res += N*(N-1)*ost[j][J];
			}
		}
		

		//int cnt=0;
		//FOR(i,0,N)
		//	FOR(j,i+1,N)
		//		FOR(k,j+1,N)
		//{
		//	if (ok(i,j,k))
		//		++cnt;
		//}

		//printf("Case #%d: %d\n", q+1, cnt);
		res /= 6;
		printf("Case #%d: %lld\n", q+1, res);
	}

	return 0;
} 
