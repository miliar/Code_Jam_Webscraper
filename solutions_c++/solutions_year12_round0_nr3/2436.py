#include <algorithm>
#include <functional>
#include <numeric>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <sstream>
using namespace std;

#define LL long long
#define LD long double
#define PR pair<int,int>

#define For(i,n) for (i=0; i<int(n); i++)
#define ForR(i,n) for (i=int(n)-1; i>=0; i--)
#define Sz(s) int((s).size())
#define All(s) (s).begin(),(s).end()
#define Fill(s,v) memset(s,v,sizeof(s))
#define pb push_back
#define mp make_pair
#define x first
#define y second

template<typename T> T Abs(T x) { return(x < 0 ? -x : x); }
template<typename T> T Sqr(T x) { return(x*x); }

const int INF = (int)1e9;
const LD EPS = 1e-9;
const LD PI = acos(-1.0);

#define DEBUG 0

int main()
{
	//files
	freopen("in.txt","r",stdin);
		if (!DEBUG)
			freopen("out.txt","w",stdout);
	//vars
	int T,t;
	int A,B;
	int i,j,p,d,cnt;
	//testcase loop
	scanf("%d",&T);
		For(t,T)
		{
			//input
			scanf("%d%d",&A,&B);
				for (p=1; p<=A; p*=10);
			p/=10;
			//try every number
			cnt=0;
				for (i=A; i<=B; i++)
				{
					j=i;
						while (true)
						{
							d=j%10;
							j/=10;
							j=d*p+j;
								if (j==i)
									break;
								if ((j<i) && (j>=A))
									cnt++;
						}
				}
			//output
			printf("Case #%d: %d\n",t+1,cnt);
		}
	return(0);
}