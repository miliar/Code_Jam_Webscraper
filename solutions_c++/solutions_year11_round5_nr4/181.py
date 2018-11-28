#include <cstdio>
#include <cmath>
#include <cstring>
#include <vector>
using namespace std;
typedef unsigned long long ULL;
void solve()
{
	char str[1024];
	scanf("%s",str);
	int n=strlen(str);
	ULL u=0,d=0;
	vector<int> p;
	for(int i=0;i<n;i++)
	{
		u<<=1;
		d<<=1;
		if(str[i]=='?')
		{
			u|=1;
			p.push_back(n-i-1);
		}
		if(str[i]=='1') d|=1;
	}
	int m=p.size();
	for(int i=0;i<(1<<m);i++)
	{
		ULL t=d;
		for(int j=0;j<m;j++)
			if((1<<j)&i)
			{
				t|=1ULL<<p[j];
			}
		ULL z=sqrt(t);
		if(z*z==t)
		{
			for(int j=n-1;j>=0;j--)
			{
				if(t&(1ULL<<j)) putchar('1'); else putchar('0');
			}
			putchar('\n');
			return;
		}
	}
}
int main()
{
	int t;
	scanf("%d",&t);
	for(int cs=1;cs<=t;cs++)
	{
		printf("Case #%d: ",cs);
		solve();
	}
	return 0;
}
