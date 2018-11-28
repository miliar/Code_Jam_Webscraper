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
#define LIM 10005

int main()
{
	freopen("in.txt","r",stdin);
		if (!DEBUG)
			freopen("out.txt","w",stdout);
	//vars
	int t,T;
	int N,DD;
	static int D[LIM],L[LIM];
	int i,s;
	PR sw;
	set <PR> S; // <how far you can get, where you can start>
	set <PR>::iterator I,J;
	//testcase loop
	scanf("%d",&T);
		for (t=1; t<=T; t++)
		{
			//init
			printf("Case #%d: ",t);
			//input
			scanf("%d",&N);
				for (i=0; i<N; i++)
					scanf("%d%d",&D[i],&L[i]);
			scanf("%d",&DD);
			//convex hull trick
			S.clear();
			S.insert(mp(D[0]*2,D[0]));
				for (i=1; i<=N; i++)
				{
					//can you make it to the end?
						if ((!S.empty()) && ((S.rbegin()->x)>=DD))
							goto Good;
						if (i==N)
							break;
					//discard swings which don't make it here
						while ((!S.empty()) && ((S.begin()->x)<D[i]))
							S.erase(S.begin());
					//can't make it here at all?
						if (S.empty())
							break;
					//find earliest start that does get you here
					s=S.begin()->y;
					//create a new swing
					sw=mp(D[i]+min(D[i]-s,L[i]),2e9);
					I=S.lower_bound(sw);
					sw.y=D[i];
					//new swing obsolete?
						if (I!=S.end())
							if ((I->y)<=sw.y)
								continue;
					//previous swings obsolete?
						if (I!=S.begin())
						{
							I--;
								while (true)
								{
										if ((I->y)<=sw.y)
											break;
										if (I==S.begin())
										{
											S.erase(I);
											break;
										}
									J=I;
									I--;
									S.erase(J);
								}
						}
					//add new swing
					S.insert(sw);
				}
			printf("NO\n");
			continue;
Good:;
			printf("YES\n");
		}
	return(0);
}