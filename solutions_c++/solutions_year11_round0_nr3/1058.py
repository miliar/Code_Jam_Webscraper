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
int D[10000];
int solve(int n)
{
    int sumA=0;
    REP(i,n)
        sumA+=D[i];
	map<pair<int,int>,int> M[2];
	M[0][make_pair(D[0],0)]=D[0];
	M[0][make_pair(0,D[0])]=0;
	int res=-1;
	FOR(i,1,n-1)
	{
		FOREACH(it,M[!(i%2)])
		{
			int a=(*it).first.first;
			int b=(*it).first.second;
			pair<int,int>A=make_pair(a^D[i],b);
			M[i%2][A]=max(M[i%2][A],(*it).second+D[i]);
			if (i==n-1)
			{
				if (A.first==A.second&&sumA!=M[i%2][A])
			    {
			     res=max(res,M[i%2][A]);

                }
			}
			A=make_pair(a,b^D[i]);
			M[i%2][A]=max(M[i%2][A],(*it).second);
			if (i==n-1)
			{
			   if (A.first==A.second&&sumA!=M[i%2][A])
			    {
			     res=max(res,M[i%2][A]);

			    }

			}
		}
		M[!(i%2)].clear();
	}
	return res;
}
int solveHard(int n)
{
    int r=0,s=0,m=INF;
    REP(i,n)
    {
        r^=D[i];
        s+=D[i];
        m=min(D[i],m);
    }
    if (r) return -1;
    return s-m;
}
int solveEasy(int n)
{
    int res=-1;
    REP(i,(1<<n)-1)
    {
        if (!i)continue;
        int a=0,ma=0;
        int b=0,mb=0;
        REP(j,n)
        {
            if (i&(1<<j))
            {
                a+=D[j];
                ma=ma^D[j];
            }
            else
            {
                b+=D[j];
                mb=mb^D[j];
            }
        }
        if (ma==mb)
        {
            res=max(a,res);
        }

    }
    return res;
}
int main ()
{
	int c,n,k;

	scanf ("%d",&c);
	DEB(c);
	FOR(cas,1,c)
	{
		scanf ("%d",&n);
		REP(i,n)
		{
			scanf ("%d",&D[i]);
		}
		int res=solveHard(n);
		if (res==-1)
		printf ("Case #%d: %s",cas,"NO");
		else
			printf ("Case #%d: %d",cas,res);

		printf ("\n");
	}
	return 0;
}


