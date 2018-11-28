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

using namespace std;
#define REP(i,n) for(int i=0,n_=(n);i<n_;i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define FOR(i,a,b) for (int i=a,b_=b;i<=(b_);i++)
#define ALL(a) a.begin(),a.end()
#define SZ(a) (int)(a).size()
#define SORT(a) sort(ALL(a))
#define INF 1073741823
#define DEB(x) cerr<<#x<<":"<<x<<"\n"
#define PB(b) push_back(b)
#define FOREACH(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)

int Area(int x1 , int y1 , int x2 , int y2 , int x3 , int y3){
        int a,b;
        int a2,b2;
        a=x2-x1;
        b=y2-y1;
        a2=x3-x1;
        b2=y3-y1;
        int cross = (a * b2) - (a2 * b);
        return abs(cross);
    }


int main ()
{
	int c,cas=1,A,M,N;
	scanf ("%d",&c);
	freopen ("output","w",stdout);
	while (c--)
	{
		scanf ("%d%d%d",&N,&M,&A);
		
		
		TPunto x(0,0);
		bool ok=false;
		
		printf ("Case #%d: ",cas++);
		FOR(i,0,N)
		FOR(j,0,M)
		FOR(k,0,N)
		FOR(l,0,M)
		{
			long long a=Area(0,0,i,j,k,l);
			if (a==A)
			{	
				DEB(a);
				printf ("%d %d %d %d %d %d",0,0,i,j,k,l);
				i=INF;
				j=INF;
				k=INF;
				l=INF;
				ok=true;
			}
		}
		if (!ok)
		{
			printf ("IMPOSSIBLE");
		}
		
		printf ("\n");
	}
	fclose(stdout);
}


