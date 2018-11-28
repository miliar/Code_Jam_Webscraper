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
#define CLEAR(V,v) memset(V,v,sizeof V)
#define FOREACH(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define OUT(a,b,c) ((a)<(b)||(a)>(c))
#define IN(a,b,c) ((a)>=(b)&&(a)<=(c))
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
long long P[222];
vector<int> R;
bool test(int mask,int n)
{
	if (mask==0) return false;
//	if (!(mask&(1<<(SZ(R)-1))))return false;;
	int U[30];
	CLEAR(U,-1);
	vector<int> Y;
	int c=0;
	REP(i,SZ(R))
	if (mask&(1<<i))
	{
		Y.PB(R[i]);
		U[R[i]]=c+1;
		c++;
	}
//	DEB(SZ(Y));
	
//	REP(i,SZ(Y))
	{
		int r=U[n];
//		DEB(Y[i]);
//		DEB(r);
//		DEB(r);
		
		bool ok=true;
		if (r==-1)return false;
		while (r!=-1)
		{
			if (r==1)
				break;
			r=U[r];
//			DEB(r);
			
			if (r==-1)
			{
				ok=false;
				break;
			}
		}
		if (!ok) return false;
	}
//	{
//		REP(i,SZ(Y))printf ("%d ",Y[i]) ;printf ("\n");
//	}
	return true;
}
int main ()
{
	int c,M,C;
	//this does the table
//	FOR(i,25,25)
//	{
//		R.clear();
//		REP(j,i-1)
//			R.PB(j+2);
//		int res=0;
////		DEB(test(3));
//		REP(mask,1<<(SZ(R)))
//		{
//			if (test(mask,i))
//			{
////				DEB("ok");
//				
//				res++;
//			}
////			else
////				DEB("!ok");
//		}
//		P[i]=res;
//		printf ("P[%d]=%d;\n",i,res);
//	}
//return 0;
	P[2]=1;
P[3]=2;
P[4]=3;
P[5]=5;
P[6]=8;
P[7]=14;
P[8]=24;
P[9]=43;
P[10]=77;
P[11]=140;
P[12]=256;
P[13]=472;
P[14]=874;
P[15]=1628;
P[16]=3045;
P[17]=5719;
P[18]=10780;
P[19]=20388;
P[20]=38674;
P[21]=73562;
P[22]=140268;
P[23]=268066;
P[24]=513350;
P[25]=984911;
	
//	long long  F[123];
//	F[1]=1;F[0]=1;
//	FOR(i,2,30)
//	F[i]=F[i-1]+F[i-2];
//return 0;
	scanf ("%d",&c);
	FOR(cas,1,c)
	{
		int res=0;
		int n;
		scanf ("%d",&n);
		

		printf ("Case #%d: %lld",cas,P[n]%100003);
		
		printf ("\n");
	}
	return 0;
}
