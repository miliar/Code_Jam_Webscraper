#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

#define ABS(x) ((x)<0?(-(x)):(x))

int solve()
{
	int bpos = 1, opos = 1, btime = 0, otime = 0, time = 0;
	int n, pos; char c;
	
	cin>>n;	
	
	while(n--)
	{
		cin>>c>>pos;
		if(c=='B')
		{
			time = max( btime + ABS(pos-bpos), time ) + 1;
			btime=time; bpos=pos;
		}
		else
		{
			time = max( otime + ABS(pos-opos), time ) + 1;
			otime=time; opos=pos;		
		}
	}
	
	return time;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("a.out","w",stdout);
	int kases; scanf("%d",&kases);
	for(int kase=1;kase<=kases;kase++) printf("Case #%d: %d\n",kase,solve());
	return 0;
}
