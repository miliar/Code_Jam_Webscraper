//GNU C++ compiler, gcc v. 4.4.3
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
#include <memory.h>

#define FI(i,a) for (int i=0; i<(a); ++i)
#define FOR(i,s,e) for (int i=(s); i<(e); ++i)
#define MEMS(a,b) memset(a,b,sizeof(a))
#define ISIN(s,a) (s.find(a)!=s.end())
#define VI vector <int>
#define VVI vector <vector <int> >
#define pb push_back
#define mp make_pair
#define pnt pair <int,int>
#define MIN(a,b) (((a)<(b))?(a):(b))
#define MAX(a,b) (((a)>(b))?(a):(b))
#define ABS(a) (((a)>0)?(a):-(a))
#define LL long long
#define U unsigned
#define ALL(a) a.begin(),a.end()

using namespace std;

#define DOUT(a) cerr << a << endl;
#define SOUT(a) cerr << a << "  ";

LL q[1001];
bool cycle[1001];
LL cyclcnt[1001];
LL cycll[1001];

int main()
{
	//freopen("sample.in","rt",stdin);
	freopen("C-large.in","rt",stdin);
	freopen("C-large.out","wt",stdout);
	int t;
	scanf("%d",&t);
	FOR(it,1,t+1)
	{
		LL r,k;
		int n;
		scanf("%lld%lld%d",&r,&k,&n);
		FI(i,n) {scanf("%lld",&q[i]); cycle[i]=false; cyclcnt[i]=0; cycll[i]=0;}
		cycle[0]=true;
		LL l=0;
		LL cash=0;
		int p=0;
		bool needcycle=true;
		while (l<r)
		{
			LL sum=0;
			int lim=0;
			bool cyclesign=false;
			while (lim<n && (sum+q[p])<=k)
			{
				sum+=q[p];
				if (p<n-1) p++;
				else {p=0; cyclesign=true;}
				lim++;
			}
			cash+=sum;
			l++;
			if (needcycle && cyclesign)
			{
				if (cycle[p])
				{
					//do cycle
					LL cycmul=((r-l)/(l-cycll[p]));
					cash+=(cash-cyclcnt[p])*cycmul;
					l+=cycmul*(l-cycll[p]);
					needcycle=false;
				}
				else {cycle[p]=true; cyclcnt[p]=cash; cycll[p]=l;}
			}
		}
		printf("Case #%d: %lld\n",it,cash);
	}
	return 0;
}
