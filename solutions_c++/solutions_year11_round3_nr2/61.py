#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/STACK:16777216")
#include <ctime>
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
template<class T> inline T Floor(T a, T b) { if (b<0) a=-a, b=-b; if (a<0) return (a-b+1)/b; return a/b; }
template<class T> inline T Ceil(T a, T b) { if (b<0) a=-a, b=-b; if (a<0) return a/b; return (a+b-1)/b; }

#define MAX 1111111

ll t;
int L, C, N;
ll a[MAX];

ll calc(int l, int st)
{
	if (st >= N)
		return 0;
	if (l <= 0)
		return 0;

	sort(a+st, a+N);
	reverse(a+st, a+N);

	ll sum=0;
	for (int i=0; i+st<N && i<l; ++i)
	{
		sum += a[st+i];
	}
	return sum/2;
}

int main()
{
	freopen("inB.txt", "r", stdin);
	freopen("outB.txt", "w", stdout);
	clock_t startTime = clock();

	int Cases;
	scanf("%d", &Cases);
	FOR(Case,0,Cases)
	{
		printf("Case #%d: ", Case+1);
		fprintf(stderr, "Case #%d: ", Case+1);

		scanf("%d%lld%d%d", &L, &t, &N, &C);
		//t *= 2;
		FOR(i,0,C)
		{
			scanf("%lld", &a[i]);
			a[i] *= 2;
		}
		FOR(i,C,N)
			a[i] = a[i-C];
		ll T=0;
		FOR(i,0,N)
			T += a[i];

		ll fullTime=0;
		FOR(i, 0, N)
		{
			fullTime += a[i];
		}
		ll curTime = 0;
		int station=-1;
		FOR(i, 0, N)
		{
			if (curTime + a[i] > t)
			{
				station = i;
				break;
			}
			curTime += a[i];
		}
		if (station == -1 )
		{
			printf("%lld\n", fullTime);
			fprintf(stderr, "%lld\n", fullTime);
		}
		else
		{
			ll deltaT = t - curTime;
			ll res1 = L > 0 ? (fullTime - (a[station] - deltaT)/2 - calc(L-1,station+1)) : fullTime;
			ll res2 = L > 0 ? (fullTime - calc(L, station+1)) : fullTime;

			printf("%lld\n", min(res1,res2));
			fprintf(stderr, "%lld\n", min(res1, res2));
		}
	}

	clock_t endTime = clock();
	fprintf(stderr, "\nTime: %.3lf\n", double(endTime-startTime)/CLOCKS_PER_SEC);
	return 0;
} 
