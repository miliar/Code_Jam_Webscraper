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
int G1[40],G2[222];
int V1[55]={0},V2[55];
int go(int n,int k)
{
	memset(G2,0,sizeof G2);
	memset(G1,0,sizeof G1);
	memset(V2,0,sizeof V2);
	memset(V1,0,sizeof V1);
	V1[0]=1;
	G1[0]=1;
//	REP(i,n+1)
//		printf ("%d ",V1[i]);printf ("\n");
	REP(www,k)
	{
		int j=1;
		REP(i,n+1)
			V2[i]=V1[i];
		REP(i,n+1)
			G2[i]=G1[i];
		while (j<=n&&G1[j-1]&&V1[j-1])
		{
			V2[j]=!V1[j];
			G2[j]=!G1[j];
			j++;
		}
		REP(i,n+1)
			V1[i]=V2[i];
		REP(i,n+1)
			G1[i]=G2[i];
//		REP(i,n+1)
//		printf ("(%d,%d )",V1[i],G1[i]);printf ("\n");
	}
//	REP(i,n+1)
//		printf ("%d ",V1[i]);printf ("\n");
	
	int j=1;
	while (j<=n&&G1[j-1]&&V1[j])
	{
		j++;
	}
//	DEB(j);
	return j==n+1;
}
int main ()
{
	int c,n,k;
	scanf ("%d",&c);
	
	FOR(cas,1,c)
	{
		int res=0;
		
		
		scanf ("%d%d",&n,&k);
		res=go(n,k);
		printf ("Case #%d: %s",cas,res?"ON":"OFF");
		
		printf ("\n");
	}
	return 0;
}

