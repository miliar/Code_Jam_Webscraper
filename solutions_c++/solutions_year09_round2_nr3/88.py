#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <complex>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

#define VAR(a,b) __typeof(b) a=(b)
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define REP(i,n) FOR(i,0,n)
#define ALL(c) (c).begin(), (c).end()

#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())

#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define SZ(c) (c).size()
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int, int> PII;
typedef vector<string> VS;

int GG[4][2] = {{-1,0},{0,-1},{0,1},{1,0}};

struct Move
{
	PII from;
	PII to;
	char sign;
	char change;
	Move(PII from, PII to, char sign, char change) : from(from), to(to), sign(sign), change(change)
	{
	}
};
typedef vector<Move> VMo;

bool inside(int x, int w)
{
	return 0 <= x && x < w;
}
bool inside(int x, int y, int w)
{
	return inside(x,w)&&inside(y,w);
}

typedef map<int, string> MIS;
typedef vector<MIS> VM;
typedef vector<VM> VVM;

int main()
{
    freopen("c.in", "r", stdin);
    freopen("c.out", "w+", stdout);
	int t;
	cin >> t;
	FOR(it,1,t+1)
	{
		int w, q;
		cin >> w >> q;
		VS M(w);
		REP(i,w)
			cin >> M[i];
		VMo moves;
		REP(i,w)
			REP(j,w)
			{
				REP(k,4)
				{
					int mi = i+GG[k][0];
					int mj = j+GG[k][1];
					if (inside(mi,mj,w))
					{
						REP(k1,4)
						{
							int ni = mi+GG[k1][0];
							int nj = mj+GG[k1][1];
							if (inside(ni,nj,w))
							moves.pb(Move(PII(i,j), PII(ni,nj), M[mi][mj], M[ni][nj]));
						}
					}
				}
			}
		VI Q(q);
		REP(i,q)
			cin >> Q[i]; 
		VVM next(w, VM(w));
		REP(i,w)
			REP(j,w)
				if ('0' <= M[i][j] && M[i][j] <= '9')
				{
					next[i][j][M[i][j]-'0'] = string(1, M[i][j]);
				}
		set<int> doQ;
		vector<bool> ToDo(10000000, false);
		REP(i,SZ(Q))
		{
			doQ.insert(Q[i]);
			ToDo[Q[i]+5000000] = true;
		}
		map<int,string> Sol;		
		while (true)
		{
			VVM was = next;
			REP(i,w)
				REP(j,w)
				{
					const map<int, string> &mapa = was[i][j];
					for(map<int, string>::const_iterator it = mapa.begin(); it != mapa.end(); ++it)
					{
						if (ToDo[it->X+5000000])
						{
							string ww = Sol[it->X];
							if (SZ(ww) == 0 || SZ(ww) > SZ(it->Y) || SZ(ww) == SZ(it->Y) && ww > it->Y)
								Sol[it->X] = it->Y;
						}
					}
				}
			if (SZ(Sol) == SZ(doQ))
				break;
			next = VVM(w, VM(w));
			REP(k,SZ(moves))
			{
				const Move &move = moves[k];
				const map<int, string> &fMap = was[move.from.X][move.from.Y];
				map<int, string> &tMap = next[move.to.X][move.to.Y];
				for (map<int, string>::const_iterator it = fMap.begin(); it != fMap.end(); ++it)
				{
					int nVal = it->X;
					if (move.sign == '+')
						nVal += move.change-'0';
					else
						nVal -= move.change-'0';
					{
						string nStr = it->Y+move.sign+move.change;
						string ww = tMap[nVal];
						if (SZ(ww) == 0 || SZ(ww) == SZ(nStr) && ww > nStr)
							tMap[nVal] = nStr;
					}
				}
			}
		}
		cerr << it << ' ' << t << endl;
		cout << "Case #" << it << ":" << endl;
		REP(i,SZ(Q))
			cout << Sol[Q[i]] << endl;
	}
}
