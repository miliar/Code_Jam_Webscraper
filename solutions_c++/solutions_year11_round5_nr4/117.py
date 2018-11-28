#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cassert>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#pragma warning (disable:4996)

int n,T,limit;
char a[150],b[150];
bool process(int pos,__int64 num)
{
	if(pos>limit)
	{
		__int64 l=0,r=2100000000,m;
		while(l<r)
		{
			m=(l+r)/2;
			if(m*m<num) l=m+1;
			else r=m;
		}
		if(r*r==num)
		{
			printf("Case #%d: %s\n",++T,b+1);
			return true;
		}
		return false;
	}
	if(a[pos]=='?')
	{
		b[pos]='0';
		if(process(pos+1,num<<1)) return true;
		b[pos]='1';
		if(process(pos+1,(num<<1)+1)) return true;
	}
	else if(a[pos]=='0')
	{
		if(process(pos+1,num<<1)) return true;
	}
	else
		if(process(pos+1,(num<<1)+1)) return true;
	return false;
}

int main()
{
	int t;
	int i,j,k;

	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	for(scanf("%d",&t);t--;)
	{
		scanf("%s",a+1);
		n=strlen(a+1);
		strcpy(b+1,a+1);

		limit=n;
		j=0;
		for(i=1;i<=n;++i) if(a[i]=='?')
			if(++j==22){limit=i;break;}

		process(1,0);
	}
	return 0;
}
