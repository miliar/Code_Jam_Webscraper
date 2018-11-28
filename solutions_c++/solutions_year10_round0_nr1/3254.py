#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

int main()
{
	int t,n,k,ct,cases=0;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d",&n,&k);
		ct=0;
		while(k)
		{
			if(k&0x1)ct++;
			else break;
			k>>=1;
		}
		printf("Case #%d: ",++cases);
		if(ct>=n)printf("ON\n");
		else printf("OFF\n");

	}

	return 0;
}