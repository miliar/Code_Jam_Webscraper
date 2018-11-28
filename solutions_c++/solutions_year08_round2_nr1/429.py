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
#include <complex>
#include <queue>
#include <ext/numeric>

using namespace std;
using namespace __gnu_cxx;

#define PB push_back
#define rep(i,X,n) for( int (i) = (X) ; (i)<(n) ; (i) ++)
#define repit(it,X,n) for(__typeof((X)) it = (X) ; (it) != (n) ; (it)++)
#define PRINT(...) fprintf(stdout,__VA_ARGS__)
#define ALL(X) (X).begin(),(X).end()

#define X first
#define Y second

long long A,B,C,D,X,Y,M,n;
pair<int,int> pts[100001];

void gen()
{
	pts[0] = make_pair(X,Y);
	rep(i,1,n)
	{
		X = (A*X+B)%M;
		Y = (C*Y+D)%M;
		pts[i] = make_pair(X,Y);
	}
}

int main()
{
	freopen("A-small-attempt0.in","rt",stdin);
	freopen("out.out","wt",stdout);
	
	int t;
	
	scanf("%d",&t);
	rep(tt,0,t)
	{
		scanf("%d %d %d %d %d %d %d %d",&n,&A,&B,&C,&D,&X,&Y,&M);
		gen();
		int res=0;
		rep(i,0,n)
			rep(j,i+1,n)
				rep(k,j+1,n)
					if((pts[i].X+pts[j].X+pts[k].X)%3 == 0 && (pts[i].Y+pts[j].Y+pts[k].Y)%3==0)
						res++;
		printf("Case #%d: %d\n",tt+1,res);
	}
	
	return 0;
}
