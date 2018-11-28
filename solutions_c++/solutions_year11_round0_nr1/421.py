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

int mem[111][111][111];
int seqB[111];
int seqR[111];

int solve() {
	fill(mem, -1);

	priority_queue<pair<int, pair<int, pii> > > q;

	q.push(mp(0, mp(0, mp(0, 0))));
	while (!q.empty()) 
	{
		int curRes = -q.top().first;
		int oPos = q.top().Y.X;
		int bPos = q.top().Y.Y.X;
		int seqPos = q.top().Y.Y.Y;
		q.pop();

		if (mem[oPos][bPos][seqPos] >= 0 && mem[oPos][bPos][seqPos] < curRes)
			continue;
		mem[oPos][bPos][seqPos] = curRes;

		if (seqPos == N)
			break;

		int pos[2] = {oPos, bPos};

		FOR(oAction,-1,3) 
		{
			FOR(bAction,-1,3) 
			{
				if (oAction == 2 && bAction == 2)
					continue;
				if (oAction == 0 && bAction == 0)
					continue;

				int oPosNew = oPos;
				int bPosNew = bPos;
				int seqPosNew = seqPos;

				if (oAction == 2) 
				{
					if (seqR[seqPos] == 0 && seqB[seqPos] == oPos) 
					{
						seqPosNew = seqPos + 1;
					} 
					else
					{
						oPosNew = -1;
					}
				}
				else 
				{
					oPosNew = oPos + oAction;
				}

				if (bAction == 2) 
				{
					if (seqR[seqPos] == 1 && seqB[seqPos] == bPos) 
					{
						seqPosNew = seqPos + 1;
					} 
					else
					{
						bPosNew = -1;
					}
				}
				else 
				{
					bPosNew = bPos + bAction;
				}

				if (oPosNew < 0 || oPosNew >= 100 || bPosNew < 0 || bPosNew >= 100)
					continue;

				if (mem[oPosNew][bPosNew][seqPosNew] < 0 || mem[oPosNew][bPosNew][seqPosNew] > curRes+1) 
				{
					q.push(mp(-(curRes+1), mp(oPosNew, mp(bPosNew, seqPosNew))));
					mem[oPosNew][bPosNew][seqPosNew] = curRes+1;
				}
			}
		}
	}

	int mx = 0;
	FOR(i,0,100) 
	{
		FOR(j,0,100) 
		{
			mx = max(mx, mem[i][j][N]);
		}
	}
	return mx;
}

int main()
{
	freopen("in-A.txt", "r", stdin);
	freopen("out-A.txt", "w", stdout);
	clock_t startTime = clock();

	int Cases;
	scanf("%d", &Cases);
	FOR(Case,0,Cases)
	{
		printf("Case #%d: ", Case+1);
		//fprintf(stderr, "Case #%d: ", Case+1);

		scanf("%d ", &N);
		FOR(i,0,N)
		{
			char robot;
			int button;
			scanf("%c %d ", &robot, &button);
			--button;
			seqR[i] = robot == 'O' ? 0 : 1;
			seqB[i] = button;
		}
		int res = solve();
		printf("%d\n", res);
	}

	clock_t endTime = clock();
	fprintf(stderr, "\nTime: %.3lf\n", double(endTime-startTime)/CLOCKS_PER_SEC);
	return 0;
} 
