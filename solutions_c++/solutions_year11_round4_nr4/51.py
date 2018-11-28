#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <sstream>
#include <queue>
#include <set>
#include <map>
#include <vector>
#include <complex>

#define mp make_pair
#define pb push_back
#define sqr(x) ((x)*(x))
#define foreach(it,c) for(typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)
#define BIT(x) (1LL<<(x))

using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int,int> PII;
typedef long long LL;
typedef complex<double> Point;

template<typename T> inline int size(const T &a) { return a.size(); }
template<typename T> inline bool operator<(const int &a,const vector<T> &b) { return a<b.size(); }
inline void setmax(int &a, int b) { if(a < b) a=b; }

struct asdf
{
    asdf(int pos, LL mask, int dist) : pos(pos), mask(mask), dist(dist) {};

    int pos;
    LL mask;
    int dist;
};

LL move[40];
int n,m;

set<LL> visit[40];

void process(void)
{
    for(int i=0;i<40;i++) visit[i].clear();
    memset(move, 0, sizeof(move));
    scanf("%d %d",&n,&m);
    for(int i=0;i<m;i++)
    {
        int a,b;
        scanf(" %d,%d",&a,&b);
        move[a] |= (1LL << b);
        move[b] |= (1LL << a);
    }

    queue<asdf> Q;
    Q.push(asdf(0,move[0],0));

    visit[0].insert(move[0]);

    int limit = -1;
    int maxcnt = 0;

    while(Q.empty() == false)
    {
        int pos = Q.front().pos;
        LL mask = Q.front().mask;
        int dist = Q.front().dist;

        if(limit != -1 && dist > limit) break;

        Q.pop();

        if(mask & 2LL)
        {
            limit = dist;
            int cnt=0;
            mask>>=1;
            for(cnt=0;mask;cnt+=(mask & 1),mask>>=1);
            setmax(maxcnt, cnt);
            continue;
        }

        for(int i=0;i<n;i++) if(mask & (1LL << i))
        {            
            if(visit[i].count(mask | move[i])) continue;
            visit[i].insert(mask | move[i]);
            Q.push(asdf(i, mask | move[i], dist + 1));
        }
    }

    cout << limit << " " << maxcnt - limit << endl;
}

int main(void)
{
    int T;
    cin >> T;
    for(int i=0;i<T;i++)
    {
        cout << "Case #" << i+1 << ": ";
        process();
        cerr << i << endl;
    }
	return 0;
}

