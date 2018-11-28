#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <string.h>
using namespace std;
#define REP(i,n) for(int i=0,n_=(n);i<n_;i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define FOR(i,a,b) for (int i=a,b_=b;i<=(b);i++)
#define ALL(a) a.begin(),a.end()
#define SZ(a) (int)(a).size()
#define SORT(a) sort(ALL(a))
#define INF 1073741823
#define DEB(x) cerr<<#x<<":"<<x<<"\n"
#define PB(b) push_back(b)
#define i64 long long
#define FOREACH(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)

vector<int> SplitInt(string &s)
{
	vector<int>Res;int tmp;stringstream a(s);
	while (a>>tmp){Res.push_back(tmp);}return Res;
}

vector<string> SplitStr(string &s)
{
	vector<string>Res;string tmp;stringstream a(s);
	while (a>>tmp){Res.push_back(tmp);}return Res;
}

//////////////////////////////////////////////////////////////
int V[101][101][101];
char R[101][3];
int B[101];
struct ST
{
	int pos,ro,rb;
};
int bfs(int n)
{
	memset(V,-1,sizeof V);
	queue<ST>  Q;
	ST x;
	x.ro=1;
	x.rb=1;
	x.pos=0;
	Q.push(x);
	V[0][1][1]=0;
	while (!Q.empty())
	{
		ST x=Q.front();
		//DEB(x.pos);
		Q.pop();

		if (x.pos==n)
		{

			return V[x.pos][x.ro][x.rb];
		}
		if (R[x.pos][0]=='B')
		{
			if (x.rb==B[x.pos])
			{
				ST y=x;
				y.pos=x.pos+1;
				FOR(dx,-1,1)
				{
					y.ro=x.ro+dx;
					if (y.ro<=0||y.ro>100) continue;
					if(V[y.pos][y.ro][y.rb]!=-1)continue;
					Q.push(y);
					V[y.pos][y.ro][y.rb]=V[x.pos][x.ro][x.rb]+1;
				}
			}
			else
			{
				ST y=x;
				FOR(dx,-1,1)
				FOR(dy,-1,1)
				{
					y.ro=x.ro+dx;
					y.rb=x.rb+dy;
					if (y.ro<=0||y.ro>100) continue;
					if (y.rb<=0||y.rb>100) continue;
					if(V[y.pos][y.ro][y.rb]!=-1)continue;
					Q.push(y);
					V[y.pos][y.ro][y.rb]=V[x.pos][x.ro][x.rb]+1;
				}
			}
		}


		if (R[x.pos][0]=='O')
				{
					if (x.ro==B[x.pos])
					{
						ST y=x;
						y.pos=x.pos+1;
						FOR(dx,-1,1)
						{
							y.rb=x.rb+dx;
							if (y.rb<=0||y.rb>100) continue;
							if(V[y.pos][y.ro][y.rb]!=-1)continue;
							Q.push(y);
							V[y.pos][y.ro][y.rb]=V[x.pos][x.ro][x.rb]+1;
						}
					}
					else
					{
						ST y=x;
						FOR(dx,-1,1)
						FOR(dy,-1,1)
						{
							y.ro=x.ro+dx;
							y.rb=x.rb+dy;
							if (y.ro<=0||y.ro>100) continue;
							if (y.rb<=0||y.rb>100) continue;
							if(V[y.pos][y.ro][y.rb]!=-1)continue;
							Q.push(y);
							V[y.pos][y.ro][y.rb]=V[x.pos][x.ro][x.rb]+1;
						}
					}
				}


	}
	return 0;
}

int main ()
{
	int c,n,k;

	scanf ("%d",&c);
	DEB(c);
	FOR(cas,1,c)
	{
		int res=0;


		scanf("%d",&n);
		REP(i,n)
		{
			scanf ("%s %d",R[i],&B[i]);
		}
		 res=bfs(n);

		printf ("Case #%d: %d",cas,res);

		printf ("\n");
	}
	return 0;
}

