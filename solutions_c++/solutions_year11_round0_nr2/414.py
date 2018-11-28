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

char T[256][256];
bool A[256][256];
char seq[256];
int cnt[256];
vector<char> res;

void addElement(char elem) {
	int resSz = sz(res);
	if (resSz == 0) {
		res.pb(elem);
		++cnt[elem];
	} else {
		char last = res[resSz-1];
		char tr = T[last][elem];
		if (tr != 0) {
			--cnt[last];
			res.pop_back();
			addElement(tr);
			//++cnt[tr];
			//res[resSz-1] = tr;
		} else {
			bool ok = true;
			FOR(j,0,resSz)
			{
				if (A[res[j]][elem])
				{
					fill(cnt, 0);
					res.clear();
					ok = false;
					break;
				}
			}
			if (ok) {
				++cnt[elem];
				res.pb(elem);
			}
		}
	}
}


int main()
{
	freopen("in-B.txt", "r", stdin);
	freopen("out-B.txt", "w", stdout);
	clock_t startTime = clock();

	int Cases;
	scanf("%d", &Cases);
	FOR(Case,0,Cases)
	{
		printf("Case #%d: ", Case+1);
		fprintf(stderr, "Case #%d: ", Case+1);

		fill(T, 0);
		fill(A, 0);
		fill(cnt, 0);
		res.clear();
		
		scanf("%d ", &M);
		FOR(i,0,M) 
		{
			char a,b,c;
			scanf("%c%c%c ", &a, &b, &c);
			T[a][b] = T[b][a] = c; 
		}

		scanf("%d ", &K);
		FOR(i,0,K) 
		{
			char a,b;
			scanf("%c%c ", &a, &b);
			A[a][b] = A[b][a] = true; 
		}

		scanf("%d ", &N);
		gets(seq);

		FOR(i,0,N){
			addElement(seq[i]);
		}

		printf("[");
		fprintf(stderr, "[");

		FOR(i,0,sz(res)) {
			if (i != 0)
			{
				printf(", ");
				fprintf(stderr, ", ");
			}
			printf("%c", res[i]);
			fprintf(stderr, "%c", res[i]);
		}

		printf("]\n");
		fprintf(stderr, "]\n");
	}

	clock_t endTime = clock();
	fprintf(stderr, "\nTime: %.3lf\n", double(endTime-startTime)/CLOCKS_PER_SEC);
	return 0;
} 
