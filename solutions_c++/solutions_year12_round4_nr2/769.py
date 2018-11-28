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
#define LIM 10

bool inter(int x1,int y1,int x2,int y2, int X1,int Y1,int X2,int Y2)
{
		if (x1>=X2)
			return(0);
		if (X1>=x2)
			return(0);
		if (y1>=Y2)
			return(0);
		if (Y1>=y2)
			return(0);
	return(1);
}

int main()
{
	freopen("in.txt","r",stdin);
		if (!DEBUG)
			freopen("out.txt","w",stdout);
	//vars
	int t,T;
	int N,X,Y;
	static PR R[LIM],tmp[LIM];
	static int ox[LIM],oy[LIM],outx[LIM],outy[LIM];
	int i,j,k,a,x,y;
	//testcase loop
	scanf("%d",&T);
		for (t=1; t<=T; t++)
		{
			//init
			printf("Case #%d:",t);
			//input
			scanf("%d%d%d",&N,&X,&Y);
				For(i,N)
				{
					scanf("%d",&R[i].x);
					R[i].y=i;
				}
			sort(R,R+N);
			reverse(R,R+N);
			//greedy
				For(i,N)
				{
					//find lowest-leftmost place to put it, that doesn't intersect
					ox[i]=oy[i]=2e9;
						For(j,i+1)
							For(k,i+1)
							{
								if (j==i)
									x=0;
								else
									x=ox[j]+R[j].x + R[i].x;
								if (k==i)
									y=0;
								else
									y=oy[k]+R[k].x + R[i].x;
								if (x>X)
									continue;
								if (y>Y)
									continue;
								For(a,i)
									if (inter(
										x-R[i].x,y-R[i].x,x+R[i].x,y+R[i].x,
										ox[a]-R[a].x,oy[a]-R[a].x,ox[a]+R[a].x,oy[a]+R[a].x))
											goto Bad;
								if ((x<ox[i]) || (x==ox[i]) && (y<oy[i]))
									ox[i]=x,oy[i]=y;
Bad:;
							}
					outx[R[i].y]=ox[i];
					outy[R[i].y]=oy[i];
				}
			//output
Done:;
				For(i,N)
					printf(" %d %d",outx[i],outy[i]);
			printf("\n");
		}
	return(0);
}