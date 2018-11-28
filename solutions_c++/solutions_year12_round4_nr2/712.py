#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <stdio.h>
#include <string.h>
#include <iostream>
#include <assert.h>
#include <stack>
#include <sstream>
#include <list>
#include <math.h>
#include <algorithm>
#include <queue>
#include <set>
#include <string>
#include <vector>
#include <map>
using namespace std;

#define ll long long
#define clr(x) memset(x,0,sizeof(x))
#define _clr(x) memset(x,-1,sizeof(x))

const double eps = 1e-7;

#define fr(x,a,b) for( int x=a; x < b; ++x )
#define frr(x,a,b) for( int x=a;x>=b;--x)

#define pf printf
#define sf scanf

#define pb push_back
#define mp make_pair

const ll mod = 1000000007;


int a[22], n;
double x[22], y[22], r[22], w, l;

bool check()
{
	double nowx = 0, nowy = 0, maxy = r[a[0]];
	x[a[0]] = y[a[0]] = 0;
	fr(i,1,n)	
	{
		int nowid = a[i], leftid = a[i-1];		
		if(nowx + r[nowid] + r[leftid] > w + eps)
		{
			nowy = maxy;
			nowx = 0;
			x[nowid] = 0;
			y[nowid] = maxy + r[nowid];
			maxy = y[nowid] + r[nowid];
		}
		else
		{
			x[nowid] =  nowx + r[nowid] + r[leftid];
			nowx = x[nowid];
			if(nowy > eps) y[nowid] = nowy + r[nowid];
			else y[nowid] = 0;
			maxy = max(maxy, y[nowid] + r[nowid]);
		}
		if( y[nowid] > l + eps ) return false;
	}
	return true;
}

int main()
{
	int T;
	scanf("%d", &T);
	fr(c,0,T)
	{
		sf("%d%lf%lf",&n,&w,&l);

		fr(i,0,n)
		{
			scanf("%lf", &r[i]);
		}

		fr(i,0,n)
		{
			a[i] = i;
		}

		do
		{
			if(check())
			{
				break;
			}
		}while(next_permutation(a, a + n));

		pf("Case #%d:",c+1);
		for(int i = 0; i < n; ++i)
		{
			pf(" %.1lf %.1lf", x[i], y[i]);
		}
		pf("\n");
	}

	return 0;
}
