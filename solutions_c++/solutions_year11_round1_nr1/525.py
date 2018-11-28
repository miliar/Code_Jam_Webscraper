#include <stdio.h>

int pd,pg;
long long n;
bool flag;

void solve()
{
	int d,g;

	flag=false;
	
	if(pg==100)
		if(pd==100) {flag=true;return;}
		else return;

	if(pg==0)
		if(pd==0) {flag=true;return;}
		else return;
		
	
	int limit;
	if(n>100LL) limit=100;
	else limit=n;
	
	//printf("limit=%d\n",limit);
	
	for(int i=1;i<=limit;i++)
	{
		d=pd*i;
		//
		if(d%100) continue;
		d=d/100;
		flag=true;
		return;
	}
	
}

int main()
{
	int casen;
	int i=0;
	
	scanf("%d",&casen);
	while(casen--)
	{
		i++;
		printf("Case #%d: ",i);
		scanf("%I64d%d%d",&n,&pd,&pg);
		solve();
		if (flag) printf("Possible\n");
		else printf("Broken\n");
	}

	return 0;
}
