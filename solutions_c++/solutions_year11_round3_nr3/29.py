#include <cstdio>
#include <ctime>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <string>
#include <iostream>
using namespace std;
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define pi 3.1415926535897932384626433832795

long long a[100000];
int n;

bool test(long long x)
{
	for(int i=0; i<n; ++i)
		if((x%a[i]!=0)&&(a[i]%x!=0))
			return false;
	return true;
}

long long gcd(long long a, long long b)
{
	return b==0?a:gcd(b, a%b);
}

int main()
{
	freopen("problem_3.in", "r", stdin);
	freopen("problem_3.out", "w", stdout);
	int t;
	cin >> t;
	for(int it=1; it<=t; ++it)
	{
		long long l, h, mx=0;
		cin >> n >> l >> h;
		for(int i=0; i<n; ++i)
		{
			cin >> a[i];
			mx=max(a[i], mx);
		}
		long long ans=-1;
		for(long long j=1; j*j<=mx; ++j)
			if(mx%j==0)
			{
				if((l<=j)&&(j<=h)&&(test(j)))
					if(ans==-1)
						ans=j;
					else
						ans=min(ans, j);
				if((l<=mx/j)&&(mx/j<=h)&&(test(mx/j)))
					if(ans==-1)
						ans=mx/j;
					else
						ans=min(ans, mx/j);
			}
		if(ans==-1)
		{
			long long lcm=1;
			for(int i=0; i<n; ++i)
			{
				long long g=gcd(a[i], lcm);
				lcm/=g;
				if(!(lcm<=h/a[i]))
				{
					lcm=-1;
					break;
				}
				else
					lcm*=a[i];
			}
			if(lcm!=-1)
			{
				long long test_num=((l+lcm-1)/lcm)*lcm;
				if((test_num>=l)&&(test_num<=h))
					ans=test_num;
			}
		}
		if(ans==-1)
			cout << "Case #" << it << ": NO" << endl;
		else
			cout << "Case #" << it << ": " << ans << endl;
		cerr << it << endl;
	}
	return 0;
}