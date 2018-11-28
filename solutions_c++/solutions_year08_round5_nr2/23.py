#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>

using namespace std;

#define FOR(i,a,b) for (int _b=(b), i=(a); i <= _b; i++)
#define REP(i,n) for (int i=0,_n=(n); i < _n; i++)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))

#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)

#define CLEAR(x) memset(x,0,sizeof x);
#define CLEARA(x) memset(&x,0,sizeof x);
#define FILL(x,v) memset(x,v,sizeof x);
#define FILLA(x,v) memset(&x,v,sizeof x);

#define VAR(a,b) __typeof(b) a=(b)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)

#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 0x7fffffff
#define X first
#define Y second
#define pb push_back
#define SZ(c) (int)(c).size()

typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long LL;

#define NAME "B-large"
#define N 20
#define K 512

const int dx[4] = {1,0,-1,0};
const int dy[4] = {0,1,0,-1};

bool avail[N][N];
int n,m,k;
typedef pair<PII,int> Portal;
map<Portal,int> portals;
vector<Portal> lst;
int nearest[N][N][4];
typedef pair<PII,PII> State;
int d[17][17][512][512];
queue<State> q;
int tm;

int dbg[17][17];

void check(int x, int y, int p1, int p2)
{
	if (d[x][y][p1][p2]==-1)
	{
		d[x][y][p1][p2] = tm+1;
		q.push(make_pair(make_pair(x,y),make_pair(p1,p2)));
		dbg[x][y]=tm+1;
	}
}

void goabout(int x, int y, State cur)
{
				REP(sh1,5) REP(sh2,5)
				{
					int p1 = cur.second.first;
					int p2 = cur.second.second;
					if (sh1!=4)
					{
						p1 = nearest[x][y][sh1];
						if (p1==-1 || p1==k)
							continue;
					}
					if (sh2!=4)
					{
						p2 = nearest[x][y][sh2];
						if (p2==-1 || p2==k)
							continue;
					}
					check(x,y,p1,p2);
				}
}

int main()
{
	freopen(NAME ".in","r",stdin);
	freopen(NAME ".out","w",stdout);

	int tests;
	scanf("%d",&tests);
	REP(tst,tests)
	{
		CLEAR(avail);
		scanf("%d%d",&n,&m);
		PII st,fin;
		REP(i,n) REP(j,m)
		{
			char c;
			do c = getc(stdin);
			while (c!='X'&&c!='.'&&c!='#'&&c!='O');
			avail[i+1][j+1] = c!='#';
			if (c=='O')
				st=make_pair(i+1,j+1);
			else if (c=='X')
				fin=make_pair(i+1,j+1);
		}
		n+=2;
		m+=2;	
		FILL(nearest,-1);
		portals.clear();
		lst.clear();
		REP(i,n) REP(j,m) if (avail[i][j]) REP(dir,4)
		{
			int x = i, y = j;
			while (avail[x][y])
			{
				x+=dx[dir];
				y+=dy[dir];
			}
			Portal p = make_pair(make_pair(x,y),(dir+2)%4);
			if (portals.find(p)==portals.end())
			{
				portals[p] = portals.size();
				lst.push_back(p);
			}
			nearest[i][j][dir] = portals[p];
		}
		k=SZ(portals);
		if (k>=K-1)
			fprintf(stderr,"BAD!");
		FILL(d,-1);
		//d[st.X][st.Y][k][k]=0;
		while (!q.empty())
			q.pop();
		//q.push(make_pair(st,make_pair(k,k)));
		tm=-1;
		goabout(st.X,st.Y,make_pair(st,make_pair(k,k)));
		int res=-1;
		while (!q.empty())
		{
			State cur=q.front();
			tm = d[cur.X.X][cur.X.Y][cur.Y.X][cur.Y.Y];
			q.pop();
			if (cur.first == fin)
			{
				res=tm;
				break;
			}
			REP(move,4)
			{
				int x = cur.X.X + dx[move];
				int y = cur.X.Y + dy[move];
				Portal need = make_pair(make_pair(x,y),(move+2)%4);
				if (cur.second.first < k && need == lst[cur.second.first] && cur.second.second < k)
				{
					Portal p = lst[cur.second.second];
					x = p.first.X + dx[p.second];
					y = p.first.Y + dy[p.second];
					//tm++;
					//check(x,y,cur.second.first,cur.second.second);
					//continue;
				}
				else if (!avail[x][y])
					continue;
				//check(x,y,cur.second.first,cur.second.second);
				goabout(x,y,cur);
				/*REP(sh1,5) REP(sh2,5)
				{
					int p1 = cur.second.first;
					int p2 = cur.second.second;
					if (sh1!=5)
					{
						p1 = nearest[x][y][sh1];
						if (p1==-1 || p1==k)
							continue;
					}
					if (sh2!=5)
					{
						p2 = nearest[x][y][sh2];
						if (p2==-1 || p2==k)
							continue;
					}
					check(x,y,p1,p2);
				}/**/
			}
		}
		/*REP(i,n)
		{

			REP(j,m)
				printf("%d",dbg[i][j]);
			printf("\n");
		}*/
		
		
		fprintf(stderr,"*");
		printf("Case #%d: ",tst+1);
		if (res!=-1)
			printf("%d",res);
		else
			printf("THE CAKE IS A LIE");
		printf("\n");
	}
	return 0;
}
