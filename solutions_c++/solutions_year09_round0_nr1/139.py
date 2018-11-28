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
vector<string> S;
int res;
int L,M;
vector<string> R;
//void go (int pos,string s)
//{
////	DEB(pos);
////	DEB(s);
////	DEB(M);
//	if (pos==L)
//	{
////		DEB(s);
//		res+=(S.find(s)!=S.end());
//		return ;
//	}
//	REP(i,SZ(R[pos]))
//	{
//		go(pos+1,s+R[pos].substr(i,1));
//	}
//} 
vector<string> toString(string A)
{
	vector<string> v;
	int i=0;
	while (i<SZ(A))
	{
		if (isalpha(A[i]))
		{
			string h;
			h+=A[i];
			v.PB(h);
			i++;
			continue;
		}
		i++;
		string h;
		while (i<SZ(A)&&A[i]!=')')
		{
			h+=A[i];
			
			i++;
		}
		i++;
		v.PB(h);
	}
	return v;
}
bool match(string h)
{
	REP(i,L)
	{
		bool ok=false;
		REP(j,SZ(R[i]))
		{
			if (h[i]==R[i][j])
			{
				ok=true;
				break;
			}
		}
		if (!ok) return false;
	}	
	return true;
}
char Pal[123];
int main ()
{
//	vector <string> H=toString("(abc)(abc)(abc)abc");
//	REP(i,SZ(H))
//		DEB(H[i]);
//	return 0;
	int c;
	scanf ("%d%d%d",&L,&M,&c);
	REP(i,M)
	{
		scanf ("%s",Pal);
		S.PB(Pal);
	}
//	DEB(c);
	FOR(cas,1,c)
	{
		res=0;
		scanf ("%s",Pal);
//		DEB(Pal);
		vector<string> v=toString(Pal);
				R=v;
		REP(i,SZ(S))
			if (match(S[i]))
				res++;

//		go(0,"");
		printf ("Case #%d: %d\n",cas,res);
	}
	return 0;
}
