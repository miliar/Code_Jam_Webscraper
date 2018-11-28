
#include <stdio.h>
#include <string.h>

unsigned long gcd(unsigned long a,unsigned long b)
{
	if(a < b) return gcd(b,a);
	if(0 == b) return a;
	if(1 == b) return 1;
	return gcd(b,a%b);
}

bool isbroken(unsigned long long n,unsigned long pd,unsigned long pg)
{
	if(0 == pg && pd != 0) return false;
	unsigned long dd = 100/gcd(100,pd);
	unsigned long long dt = dd;
	if(n < dt) return false;
	if(pg == 100 && pg > pd) return false;

	unsigned long dg = gcd(100,pg);
	int dis = (int)(pd) - (int)(pg);
	if(dis < 0) dis = 0 - dis;

	unsigned long ds = dg/gcd(dis,dg);
	unsigned long dr = gcd(dd,ds);

	dt = (unsigned long long)(dd*ds/dr);
	if(n < dt) return false;

	return true;
}

int main()
{
	char buff[0x1000] = { 0 };
	int nCases = 0;scanf("%d",&nCases);
	for(int iCases = 1;iCases <= nCases;++iCases)
	{
		scanf("%s",buff);
		unsigned long long n = 0;
		for(size_t i = 0;i < strlen(buff);++i)
		{
			n *= 10;
			n += buff[i] - '0';
		}
		int pd = 0,pg = 0;scanf("%d%d",&pd,&pg);
		bool r = isbroken(n,pd,pg);
		if(r) printf("Case #%d: Possible\n",iCases);
		else printf("Case #%d: Broken\n",iCases);
	}
	return 0;
}