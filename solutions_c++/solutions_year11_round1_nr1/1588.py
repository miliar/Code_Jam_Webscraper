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
#include <complex>
#include <climits>
#include <queue>
#include <ctime>

using namespace std;

#define PB push_back
#define ALL(x) (x).begin(),(x).end()
#define rep(i,x,n) for(int i = (x) ; i < (n) ; ++i)
#define repit(it,x,n) for(__typeof(x) it = (x) ; it!=(n) ;++it)

long long n,pd,pg;
int t;

bool isx(long long d)
{
	if((d*pd)%100!=0)
		return false;
	return true;
}

bool isy(long long d,long long g)
{
	if((g*pg)%100!=0)
		return false;
	long long x = (d*pd)/100;
	long long y = (g*pg)/100;
	if(y<x)
		return false;
	return g>=(d-x+y);
}

int main()
{
	freopen("1.txt","rt",stdin);
	freopen("2.txt","wt",stdout);

	cin>>t;
	rep(tt,0,t)
	{
		cin>>n>>pd>>pg;
		printf("Case #%d: ",tt+1);
		rep(i,1,n+1)
		{
			if(isx(i))
			{
				rep(j,i,100000)
				{
					if(isy(i,j))
					{
						printf("Possible\n");
						goto next;
					}
				}
			}
		}
		printf("Broken\n");
		next:;
	}

	return 0;
}
