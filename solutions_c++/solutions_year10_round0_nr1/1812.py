#include <cstdio>
int main()
{
	int tab[31];
	int t,n,k,i;
	tab[1]=1;
	for(i=2;i<=30;i++) tab[i]=2*tab[i-1]+1;
	scanf("%d", &t);
	for(i=1;i<=t;i++)
	{
		scanf("%d %d", &n, &k);
		printf("Case #%d: ",i);
		if(k%(tab[n]+1)==tab[n]) printf("ON\n");
		else printf("OFF\n");
	}
	return 0;
}
