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
#define FOR(i,a,b) for (long long i=a,b_=b;i<=(b);i++)
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
long long A[10];
int main ()
{
	int c,M,C;
	scanf ("%d",&c);
	
	FOR(cas,1,c)
	{
//		DEB(cas);
		long long res=0;
		int n;
		scanf ("%d",&n);
		
		REP(i,n)
			scanf ("%lld",&A[i]);
		sort(A,A+n);
		long long t=abs(A[1]-A[0]);
		DEB(t);
		REP(i,n)
		REP(j,i)
		{
			t=__gcd(t,abs(A[i]-A[j]));
		}
		
		long long otro=A[0];
		REP(i,n)
			otro=__gcd(otro,A[i]);
		
		
		long long y=0;
		
		res=t-A[0]%t;
//		DEB(t);
		long long rrr=A[0]+res;
		REP(i,n)
			rrr=__gcd(rrr,A[i]+res);
//		DEB(rrr);
		if (rrr==otro)
			res=0;
		printf ("Case #%lld: %lld",cas,res);
		
		printf ("\n");
	}
	return 0;
}
