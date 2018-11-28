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
double R[1000],W[1000],OWP[1000],OOWP[1000],W2[1000];
char P[123][123];
int pos[123333];
int V[5000000];
int hay,d;
bool test(double x)
{
	double pos=V[0]-x;
	FOR(i,1,hay-1)
	{
		pos+=d;
		if(V[i]>=pos)
		{
			pos=max(V[i]-x,pos);
		}
		else
		if (V[i]<pos)
		{
			if (fabs(V[i]-pos)>x)
				return false;
		}
	}
	return true;
}
double bs(double ini,double fin,int it)
{
	if (fabs(ini-fin)<1e-9||it>70)
		return (ini+fin)/2;
	double x=(ini+fin)/2;
	if (test(x))
	{
		return bs(ini,x,it+1);
	}
	return bs(x,fin,it+1);
}
int main ()
{
	int c,n,q;
	scanf ("%d",&c);
	long long N,pd,pg;
	FOR(cas,1,c)
	{
		//TODO
		int mx=-INF;
		int mn=INF,q;
		long long sum=0;
		int mxq=0;
		scanf ("%d%d",&n,&d);
		double avg=0;

		hay=0;
		REP(i,n)
		{
			scanf ("%d %d",&pos[i],&q);
			avg+=pos[i];
			mn=min (pos[i],mn);
			mx=max (pos[i],mx);
			mxq=max(q,mxq);
			REP(j,q)
				V[hay++]=pos[i];
			sum+=q;
		}
		avg/=sum;
		sort(V,V+hay);
		double res=bs(0,1e14,0);
		printf ("Case #%d: %.6lf\n",cas,res);
		DEB(cas);
		
	}
	return 0;
}

