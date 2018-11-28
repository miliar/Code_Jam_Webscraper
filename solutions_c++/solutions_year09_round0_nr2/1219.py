#include <algorithm>
#include <cstdio>
#include <cstdlib>
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
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<PII> VPII;
typedef vector<VI> VVI;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w+", stdout);
	char d[4][2]={{-1,0},{0,-1},{0,1},{1,0}};
	char alpha[26]={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
	int T,min;
	cin >> T;
	REP (t, T)
	{
		int H,W;
		cin >> H >> W;
		cout << "Case #"<< (t+1) << ":" << endl;
		VVI mat(H+2, VI(W+2, INF));
		REP (tt, H)
			REP (ttt, W)
			cin >> mat[tt+1][ttt+1];
		vector<VVI> con (H, VVI(W, VI(5,0)));
		REP (tt,H)
			REP (ttt, W)
			{
				min=-1;
				for (int i=0; i<4 && min<0; i++) 
				{
					if(mat[tt+1][ttt+1]>mat[tt+1+d[i][0]][ttt+1+d[i][1]]) min=i;
				}
				if (min>=0 && min<4) 
				{
					for (int i=min+1; i<4; i++) if(mat[tt+1+d[min][0]][ttt+1+d[min][1]]>mat[tt+1+d[i][0]][ttt+1+d[i][1]]) min=i;
					con[tt][ttt][min]=1;
					con[tt+d[min][0]][ttt+d[min][1]][3-min]=1;
					con[tt][ttt][4]=1;
					con[tt+d[min][0]][ttt+d[min][1]][4]=1;
				}
		}
		int p=0;
		int ch=0;
		VPII stack(10000);
		REP (tt,H)
			REP(ttt, W)
		{
			if(con[tt][ttt][4]==1)
			{
				p=0;
				stack[p].X=ttt;
				stack[p].Y=tt;
				for(int i=0; i<=p; i++)
				{
					mat[stack[i].Y+1][stack[i].X+1]=ch;
					con[stack[i].Y][stack[i].X][4]=-1;
					REP(tttt,4)
						if(con[stack[i].Y][stack[i].X][tttt]==1 && con[stack[i].Y+d[tttt][0]][stack[i].X+d[tttt][1]][4]>-1)
						{
							p++;
							stack[p].X=stack[i].X+d[tttt][1];
							stack[p].Y=stack[i].Y+d[tttt][0];
						}
				}
				ch++;
			} else
			if(con[tt][ttt][4]==0)
			{
				con[tt][ttt][4]=-1;
				mat[tt+1][ttt+1]=ch;
				ch++;
			} 
		}
		REP(tt, H)
		{
			cout << alpha[mat[tt+1][1]];
			REP(ttt, W-1)
			{
				cout <<" " << alpha[mat[tt+1][ttt+2]];
			}
			cout << endl;
		}
	}	
	return 0;
}
