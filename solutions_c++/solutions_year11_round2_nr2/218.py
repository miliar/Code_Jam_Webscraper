///Team Heisenbug
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
#include <cassert>
#include <vector>
#include <fstream>
#include <stack>
#include <cstring>
#include<sys/time.h>
/*****************************************************************************************************
					macros and typedefs for shortening length
******************************************************************************************************/
///Fast IO
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
#define mp make_pair
#define SZ(c) (c).size()
#define ps(n) printf("%s\n",n)
typedef long long LL;
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<PII> VPII;
typedef vector<VI> VVI;

/*****************************************************************************************************
							Program starts here
******************************************************************************************************/
///macros for global constants
int C,D;
#define MAXN 1000011
int A[MAXN];
int N;
double tA[MAXN];

#define INFD 1e15
#define eps 1e-7
bool inline predicate(double t)
{
	//check if in time t, we can achieve min separation
	REP(i,N)
	tA[i] = A[i];
	
	tA[0] = tA[0] - t;//push him back
	
	FOR(i,1,N)
	{
		//maintain D from tA[i-1]
		double tpos = tA[i-1] + D;
		double tpos2 = tA[i] - t;
		double tpos3 = tA[i] + t;
		//tpos2,tpos,tpos3
		if(tpos < tpos3 || fabs(tpos - tpos3) < eps)
		{
			//assign greedy best
			if(tpos2 > tpos || fabs(tpos2 - tpos) < eps)
			tA[i] = tpos2;
			else if(tpos > tpos2 && tpos < tpos3)
			tA[i] = tpos;
			else
			tA[i] = tpos3;
		}
		else
		return false;
	}
	return true;
}

double solve()
{
	double lo = 0,hi = INFD;
	double mid;
	int itr = 100;
	while(itr--)
	{
		mid = (lo + hi)/2.0;
		
		//printf("Lo:%.9lf Mid:%.9lf Hi:%.9lf\n",lo,mid,hi);
		if(predicate(mid))
		hi = mid;
		else
		lo = mid;
		
		if(fabs(lo - hi) < eps)
		break;
	}
	if(predicate(lo))
	return lo;
	else if(predicate(mid))
	return mid;
	else if(predicate(hi))
	return hi;
	
	assert(-1 > 0);
}		
int main()
{
	int T;
	scanf("%d",&T);
	FOR(cases,1,T+1)
	{
		scanf("%d %d",&C,&D);
		N = 0;
		REP(i,C)
		{
			int p,v;
			scanf("%d %d",&p,&v);
			while(v--)
			A[N++] = p;
		}
		fprintf(stderr,"%d\n",cases);
		//binary search
		printf("Case #%d: %.9lf\n",cases,solve());
	}
	return 0;
}
