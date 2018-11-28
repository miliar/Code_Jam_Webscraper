#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
int t,n,d,g,pd,pg,kd,kg;

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&t);
	for (int tt=1;tt<=t;tt++)
	{
		scanf("%d%d%d",&n,&pd,&pg);
		printf("Case #%d: ",tt);
		if (pg==100 && pd<100 || pg==0 && pd>0)
			printf("Broken\n");
		else if (pg==100 || pg==0)
			printf("Possible\n");
		else 
		{
			if (pd%100==0) kd=1;
			else if (pd%50==0) kd=2;
			else if (pd%25==0) kd=4;
			else if (pd%20==0) kd=5;
			else if (pd%10==0) kd=10;
			else if (pd%5==0) kd=20;
			else if (pd%4==0) kd=25;
			else if (pd%2==0) kd=50;
			else kd=100;
			if (n<kd)
				printf("Broken\n");
			else printf("Possible\n");
		}
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}