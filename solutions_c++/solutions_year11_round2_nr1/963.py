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
int N, M, K;
#define MAX 111
char a[MAX][MAX];
double WP[MAX];
double OWP[MAX];
double OOWP[MAX];

double calcWP(int team)
{
	int wins = 0;
	int loses = 0;
	FOR(i,0,N)
	{
		if (a[team][i] == '.')
			continue;
		if (a[team][i] == '1')
			++wins;
		if (a[team][i] == '0')
			++loses;
	}
	return (0.0 + wins)/(wins + loses);
}

double calcOWP(int team)
{
	int cnt=0;
	double sumOWP = 0.0;
	FOR(i,0,N)
	{
		if (a[team][i] == '.')
			continue;

		int wins=0;
		int loses=0;
		FOR(j,0,N)
		{
			if(j==team || a[i][j] == '.')
				continue;
			if(a[i][j] == '1')
				++wins;
			else
				++loses;
		}

		++cnt;
		sumOWP += wins / (wins + loses + 0.0);
	}
	return sumOWP / cnt;
}

double calcOOWP(int team)
{
	int cnt=0;
	double sum = 0.0;
	FOR(i,0,N)
	{
		if (a[team][i] == '.')
			continue;
		++cnt;
		sum += OWP[i];
	}
	return sum / cnt;
}
int main()
{
	freopen("inA.txt", "r", stdin);
	freopen("outA.txt", "w", stdout);
	clock_t startTime = clock();

	int Cases;
	scanf("%d", &Cases);
	FOR(Case,0,Cases)
	{
		printf("Case #%d:\n", Case+1);
		fprintf(stderr, "Case #%d:\n", Case+1);

		scanf("%d\n", &N);
		FOR(i,0,N)
			gets(a[i]);

		FOR(i,0,N)
			WP[i] = calcWP(i);
		FOR(i,0,N)
			OWP[i] = calcOWP(i);
		FOR(i,0,N)
			OOWP[i] = calcOOWP(i);

		FOR(i,0,N)
		{
			printf("%.12lf\n", 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i]);
			fprintf(stderr, "%.12lf\n", 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i]);
		}
	}

	clock_t endTime = clock();
	fprintf(stderr, "\nTime: %.3lf\n", double(endTime-startTime)/CLOCKS_PER_SEC);
	return 0;
} 
