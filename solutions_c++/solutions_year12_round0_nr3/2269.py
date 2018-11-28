#include <iostream>
#include <vector>
#include <stdio.h>
#include <string>
#include <math.h>
#include <algorithm>
#include <set>
#include <math.h>
#include <time.h>
#include <stdio.h>
#define rep(i,k,n) for(int (i) = (k); (i) < (n); (i)++)
#define sqr(r) (r)*(r)
#define ii pair<int,int>
#define vii vector<ii>
#define vi vector<int>
#define vvi vector<vi>
using namespace std;


set<long long> si;
long long mod;
long long n,m,k,d,l,r, INF = 10000009;

vvi v;
vii w;

void add(int i)
{
	int ten = 10, len = 1, k = 0,t;
	int f = 0;
	while(i >= len)
	{
		len *= 10;
		k++;
	}
	len/=10;
	while( k > 1)
	{
		f = 0;
		t = (i%ten)*len + i/ten;
		if(t >= i)
		{
			ten*=10;
			len/=10;
			k--;
			continue;
		}
		rep(j,0,v[i].size())
			if(t == v[i][j])
			{
				ten*=10;
				len/=10;
				k--;
				f = 1;
				break;
			}
		if(f)
		{continue;}
		v[i].push_back(t);
		ten*=10;
		len/=10;
		k--;
	}
	
	
}

int sd(int a, int b)
{
	int ten = 10, len = 1, k = 0,t;
	while(a >= len)
	{
		len *= 10;
		k++;
	}
	len/=10;
	while( k > 1)
	{
		if(b == (a%ten)*len + a/ten)
			return 1;
		k--;
		ten*=10;
		len/=10;
	}
	return 0;


}
int main()
{
	freopen("in","r", stdin);
	freopen("out", "w", stdout);
	cin >> n;
	v.push_back(vi(0));
	rep(i,1,2000002)
	{
		v.push_back(vi(0));
		add(i);
	}
	long long sp;
	rep(i,1,n+1)
	{
		 sp = 0;

		cout << "Case #" << i << ": ";
		cin >> l >> r;
		rep(j,l,r+1)
		{
			rep(p,0,v[j].size())
				if( v[j][p] >= l && v[j][p] <= r)
					sp++;
		}
		cout << sp << "\n";
	}
	

	return 0;
}
