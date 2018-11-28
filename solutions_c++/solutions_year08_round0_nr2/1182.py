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
typedef ostringstream oss;
#define FOR(i,f,n) for(int i=f; i<n; ++i) 
#define sz(a) ((int)a.size()) 
#define fill(w,v) memset(w,v,sizeof(w)) 
#define pb push_back 
#define all(a) a.begin(),a.end()
#define mp make_pair 
#define inf 1000000000 
template<class T> inline T gcd(T a, T b){T t; while (a && b) t = a, a = b%a, b = t; return a+b; }
template<class T> inline T power(T a, int p) {T r = T(1); while (p) { if (p&1) r = r*a; a = a*a; p >>= 1; } return r; }
template<class T> T extgcd(T a, T b, T& x, T& y) { if (b==0) return x=1, y=0, a; T x1, y1, g; g = extgcd(b, a%b, x1, y1); x = y1; y = x1 - a/b*y1; return g; }

int gcnt=0;
struct Event
{
	bool train;
	int start, end;
	int station;
	int id;

	Event(int stat, bool tr, int st, int e=-1): station(stat), train(tr), start(st), end(e), id(gcnt++) {}
	bool operator<(const Event& ev) const
	{
		if (start != ev.start)
			return start > ev.start;
		if (train != ev.train)
			return !train;
		return id < ev.id;
	}
};

priority_queue<Event> q;
int T, NA, NB;
int trcnt[2];
int res[2];
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int CA;
	scanf("%d", &CA);

	for (int ca=0; ca<CA; ++ca)
	{
		res[0] = res[1] = 0;
		scanf("%d%d%d", &T, &NA, &NB);
		trcnt[0] = trcnt[1] = 0;
		int m1,h1,m2,h2;
		FOR(i,0,NA)
		{
			scanf("%d:%d %d:%d", &h1, &m1, &h2, &m2);
			q.push(Event(0, false, h1*60+m1, h2*60+m2));
		}
		FOR(i,0,NB)
		{
			scanf("%d:%d %d:%d", &h1, &m1, &h2, &m2);
			q.push(Event(1, false, h1*60+m1, h2*60+m2));
		}

		while (!q.empty())
		{
			Event cur = q.top(); q.pop();
			if (cur.train)
			{
				trcnt[cur.station]++;
			}
			else
			{
				if (trcnt[cur.station])
					trcnt[cur.station]--;
				else
					++res[cur.station];
				q.push(Event(1-cur.station, true, cur.end+T));
			}
		}
		printf("Case #%d: %d %d\n", ca+1, res[0], res[1]);
	}
	return 0;
} 
