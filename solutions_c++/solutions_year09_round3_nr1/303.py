#include <iostream>
char mark[128];
void init()
{
	int i;
	for(i=0;i<128;i++)
		mark[i] = -1;
}
long long solve()
{
	int i, j;
	char sym[64];
	int base = 2, tag = 0;
	long long sum;
	init();
	scanf("%s", sym);
	mark[sym[0]] = 1;
	for(i=1;sym[i];i++)
	{
		if(-1 != mark[sym[i]])
			continue;
		if(!tag)
			mark[sym[i]] = 0, tag=1;
		else 
			mark[sym[i]] = base++;
	}
	sum = mark[sym[0]];
	for(i=1;sym[i];i++)
		sum = sum*base + mark[sym[i]];
	return sum;
}
int main()
{
	int ncase, icase;
	freopen("test.in", "r+", stdin);
	freopen("test.out", "w+", stdout);
	scanf("%d", &ncase);
	for(icase = 1;icase<=ncase;icase++)
		printf("Case #%d: %lld\n", icase, solve());
	return 0;
}