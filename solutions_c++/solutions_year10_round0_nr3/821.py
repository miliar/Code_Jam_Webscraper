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
#define DEB(x) cout<<#x<<":"<<x<<"\n"
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
long long T[10000],S[10000];
int gi[10000];
int main ()
{
//	printf ("50\n");
//	REP(www,50)
//	{
//	printf ("100000000 1000000000 1000\n");
//	REP(i,1000)
//		printf ("%d ",rand()%10000000+1);
//	printf ("\n");
//	}
//	return 0;
	int c,R,k,n;
	scanf ("%d",&c);
	
	FOR(cas,1,c)
	{
		scanf ("%d%d%d",&R,&k,&n);

		REP(i,n)
		{
			scanf ("%d",&gi[i]);
			
		}
//		DEB(n);
		REP(i,n)
		{
			int j=i,h=0;
			long long s=0;
			while (s+(long long)gi[j]<=k&&h<n)
			{
				s+=(long long)gi[j];
				h++;
				j++;
				j%=n;
			}
			if (h==0)
				T[j]=-1;
			T[i]=j;
			S[i]=s;
//			DEB(i);
		}
		long long res=0;
		int cur=0;
		REP(www,R)
		{
			if (T[cur]==-1) break;
			res+=S[cur];
			
			cur=T[cur];
//			DEB(cur);
		}
		printf ("Case #%d: %lld",cas,res);
		
		printf ("\n");
	}
	return 0;
}
