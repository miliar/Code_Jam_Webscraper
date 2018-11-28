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
int D[1000][1000];
pair<double,double> center(int x,int y,int x1,int y1,double cx,double cy)
{
	int c=0;
	double sumx=0,sumy=0;
	FOR(i,x,x1)
	FOR(j,y,y1)
	{
		sumx+=(cx-i)*D[i][j];
		sumy+=(cy-j)*D[i][j];
		c++;
	}
	c-=4;
	sumx-=((cx-x)*D[x][y]+(cx-x)*D[x][y1]+(cx-x1)*D[x1][y]+(cx-x1)*D[x1][y1]);
	sumy-=((cy-y)*D[x][y]+(cy-y1)*D[x][y1]+(cy-y)*D[x1][y]+(cy-y1)*D[x1][y1]);
	return make_pair(sumx,sumy);
	
}
char M[1233][555];
int main ()
{
	int c,n,m,d;
	scanf ("%d",&c);
	long long N,pd,pg;
	FOR(cas,1,c)
	{
		//TODO
		int res=0;
		scanf ("%d%d%d",&n,&m,&d);
		REP(i,n)
		{
			scanf ("%s",M[i]);
			REP(j,m)
				D[i][j]=M[i][j]+d;

		}
		res=-1;
		
		FOR(i,0,n-1)
		FOR(j,0,m-1)
		FOR(k,2,max(n,m))
		{
		
			if (i+k>n||j+k>m) break;
			double t=i+k/2.0;
			double s=j+k/2.0;
			pair<double,double>h= center(i,j,i+k,j+k,t,s);
			if (fabs(h.first)+fabs(h.second)<1e-10)
			{
				res=max(k,res);

			}
		}
		if (res!=-1)
		printf ("Case #%d: %d\n",cas,res+1);
		else
		printf ("Case #%d: IMPOSSIBLE\n",cas);
		
	}
	return 0;
}

