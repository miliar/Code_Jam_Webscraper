#include <fstream>
#include <assert.h>
#include <algorithm>
using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

double x, s, r, t;
int n;
struct Walk
{
	double b, e, w;
};

bool operator<(const Walk& a, const Walk& b)
{
	return a.w < b.w;
}

Walk a[2005];

double solve(Walk& k)
{
	if(k.b == k.e)
		return 0;
	if(t == 0)
		return (k.e - k.b)/(s + k.w);
	if((k.e - k.b)/(r + k.w) <= t)
	{
		t -= (k.e - k.b)/(r + k.w);
		return (k.e - k.b)/(r + k.w);
	}
	double vaz = t*(r+k.w);
	double ans = t;
	assert(vaz <= k.e - k.b);
	t = 0;
	return ans + (k.e - k.b - vaz)/(s+k.w);
}

int main()
{
	int ct, caseN,i;
	double ans;
	fin>>ct;
	for(caseN=1; caseN<=ct; ++caseN)
	{
		ans=0;
		fin>>x>>s>>r>>t;
		fin>>n;
		a[1].b = 0;
		a[1].w = 0;
		for(i=2; i<=2*n; i+=2)
		{
			fin>>a[i].b>>a[i].e>>a[i].w;
			if(i==2)
				a[1].e = a[2].b;
			else
			{
				a[i-1].b = a[i-2].e;
				a[i-1].e = a[i].b;
				a[i-1].w = 0;
			}
		}
		a[2*n+1].b = a[2*n].e;
		a[2*n+1].e = x;
		a[2*n+1].w = 0;
		sort(a+1, a+2*n+2);
		for(i=1; i<=2*n+1; ++i)
			ans+=solve(a[i]);
		fout<<"Case #"<<caseN<<": ";
		fout.setf(ios::fixed);
		fout.precision(10);
		fout<<ans<<endl;
	}
	return 0;
}