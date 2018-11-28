#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <cstring>
#include <ctime>
#include <queue>

using namespace std;

#define	sqr(a)		((a)*(a))
#define	rep(i,a,b)	for(int i=(a);i<(int)(b);i++)
#define	per(i,a,b)	for(int i=((a)-1);i>=(int)(b);i--)
#define	PER(i,n)	per(i,n,0)
#define	REP(i,n)	rep(i,0,n)
#define	clr(a)		memset((a),0,sizeof (a))
#define	SZ(a)		((int)((a).size()))
#define	ALL(x)		x.begin(),x.end()
#define	mabs(a)		((a)>0?(a):(-(a)))
#define	inf			1000000001
#define	eps			1e-6

#define	MAXN		

long long gcd(long long a,long long b)
{
	while(b!=0)
	{
		long long t = b;
		b = a % b;
		a = t;
	}
	return a;
}

char s[105][105];
double wp[105];
int win[105];
int lose[105];
double owp[105];
double oowp[105];


int main()
{
//#define MY_DEBUG
#ifndef MY_DEBUG
	freopen("data.in","r",stdin);
	freopen("data.out","w",stdout);
#endif

	int T;
	scanf("%d",&T);

	REP(k,T)
	{
		int n;
		scanf("%d",&n);
		clr(win);
		clr(lose);
		REP(i,n)
		{
			scanf("%s",s[i]);
		}

		REP(i,n)
		{
			REP(j,n)
			{
				if (s[i][j] == '0')
				{
					lose[i]++;
				}
				else if (s[i][j] == '1')
				{
					win[i]++;
				}
			}
			wp[i] = (double)win[i] / (double)(win[i] + lose[i]);
		}

		REP(i,n)
		{
			double temp = 0;
			int t_n = 0;
			REP(j,n)
			{
				if (s[i][j] == '0')
				{
					temp += (double)(win[j] - 1) / (double)(win[j] + lose[j] - 1);
					t_n++;
				}
				else if (s[i][j] == '1')
				{
					temp += (double)win[j] / (double)(win[j] + lose[j] - 1);
					t_n++;
				}
			}
			owp[i] = temp / (double)t_n;
		}

		REP(i,n)
		{
			double temp = 0;
			int t_n= 0;
			REP(j,n)
			{
				if (s[i][j] == '0' || s[i][j] == '1')
				{
					temp += owp[j];
					t_n++;
				}
			}
			oowp[i] = temp / (double)t_n;
		}

		printf("Case #%d:\n",k + 1);
		REP(i,n)
		{
			printf("%lf\n",0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]);
		}
	}

	return 0;
}