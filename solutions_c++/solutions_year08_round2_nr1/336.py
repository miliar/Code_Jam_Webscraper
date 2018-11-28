#include <iostream>
#include <string>
#include <cstring>
#include <fstream>
#include <cmath>
#include <algorithm>
#include <iomanip>
using namespace std;

ifstream fin("A-large.in");
ofstream fout("A-large.out");

const int maxn = 100001;

int n,A,B,C,D,M;
int x[maxn],y[maxn],z[maxn];
int s[9];

void solve()
{
	fin >> n >> A >> B >> C >> D >> x[0] >> y[0] >> M;
	for (int i = 1; i < n; ++i)
	{
		x[i] = ((__int64)x[i-1]*A+B)%M;
		y[i] = ((__int64)y[i-1]*C+D)%M;
	}
	
	memset(s,0,sizeof(s));
	for (int i=0; i<n; ++i)
	{
		x[i] %= 3;
		y[i] %= 3;
		z[i] = x[i]*3+y[i];
		s[z[i]]++;
	}
	
	__int64 ans = 0;
	for (int i=0; i<9; ++i)
	    for (int j=i+1; j<9; ++j)
	        for (int k=j+1; k<9; ++k)
	        {
				int a1=i/3, b1=j/3, c1=k/3;
				int a2=i%3, b2=j%3, c2=k%3;
				if ((a1+b1+c1)%3==0 && (a2+b2+c2)%3==0)
				    ans += (__int64)s[i]*s[j]*s[k];
			}
	for (int i=0; i<9; ++i)
		if (s[i]>2) ans += (__int64)s[i]*(s[i]-1)*(s[i]-2)/6;
	for (int i=0; i<9; ++i)
	    for (int j=i+1; j<9; ++j)
	    {
			int a1=i/3, b1=j/3;
			int a2=i%3, b2=j%3;
	        if (s[i]>1 && (a1+a1+b1)%3==0 && (a2+a2+b2)%3==0) ans += (__int64)s[i]*(s[i]-1)/2*s[j];
	        if (s[j]>1 && (a1+b1+b1)%3==0 && (a2+b2+b2)%3==0) ans += (__int64)s[j]*(s[j]-1)/2*s[i];
		}
	fout << ans << endl;
}

int main()
{
	int tc;
	fin >> tc;
	for (int i = 1; i <= tc; ++i)
	{
		fout << "Case #" << i << ": ";
		solve();
	}
	fin.close();
	fout.close();
	return 0;
}
