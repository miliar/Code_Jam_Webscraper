#define _CRT_SECURE_NO_DEPRECATE


#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<fstream>
#include<string>
#include<cmath>
#include<set>
#include<list>
#include<limits>
#include<string.h>
#include<memory.h>
using namespace std;

#define SZ(x) ((long long)x.size())

ifstream inf("B-large.in");
ofstream outf("out.txt");

#define cin inf

#define cout outf

long long a[1000001];
long long d[1000002];
long long s[1000001];
int main()
{
	long long T;
	cin>>T;
	for(long long xt=1;xt<=T;xt++)
	{
		memset(s,0,sizeof(s));
		memset(d,0,sizeof(d));
		memset(a,0,sizeof(a));
		long long l,t,n,c;
		cin>>l>>t>>n>>c;
		for(long long i=0;i<c;i++)
			cin>>a[i];
		long long ret = 0;
		for(long long i=0;i<n;i++)
			d[i] = a[i-i/c*c]*2;

		long long sb = n;
		for(long long i=0;i<n;i++)
		{
			if(ret + d[i] > t)
			{
				sb = i;
				break;
			}
			else
				ret += d[i];
		}
		if(sb==n)
			goto _out;
		d[sb] = d[sb] - (t-ret);

		if(l>=n-sb+1)
			for(long long i=sb;i<n;i++)
				s[i] = 1;
		else if(l)
		{
			sort(d+sb,d+n,greater<long long>());
			long long mx;
			mx = d[sb+l-1];

			for(long long i=sb;i<n;i++)
				d[i] = a[i-i/c*c]*2;
			d[sb] = d[sb] - (t-ret);
			for(long long i=sb;i<n;i++)
				if(d[i] > mx)
				{
					s[i] = 1;
					l --;
				}

				for(long long i=n-1;i>=sb;i--)
				{
					if(!l)
						break;
					if(d[i] == mx)
					{
						s[i] = 1;
						l--;
					}
				}
		}
		ret = t;
		for(long long i=sb;i<n;i++)
		{
			if(s[i])
				ret += d[i]/2;
			else
				ret += d[i];
		}
_out:
		cout<<"Case #"<<xt<<": "<<ret<<endl;
	}
} 