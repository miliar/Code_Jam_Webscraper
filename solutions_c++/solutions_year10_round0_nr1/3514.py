#include <cstdio>

int nnn,kkk;
int w[35];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("a.out.txt","w",stdout);
	int i,j,ss;
	scanf("%d",&ss);
	for(i=1;i<=ss;i++)
	{
		scanf("%d%d",&nnn,&kkk);
		int tt = 1<<nnn;
		kkk %= tt;
		if(tt-1 == kkk) printf("Case #%d: ON\n",i);
		else printf("Case #%d: OFF\n",i);
	}
	return 0;
}
