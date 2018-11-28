#include <stdio.h>
#include <math.h>
int cs[102];
int pos[102];
int ns;

void Solve()
{
	int ltime[2] = {0};
	int curtime = 0;
	int p[2]={1,1};
	for (int i=1; i<=ns; i++)
	{
		int rob = cs[i];
		int pb = pos[i];
		int tcost = fabs(0.0+pb-p[rob]);
		if (tcost+ltime[rob]> curtime)
		{
			curtime = tcost + ltime[rob] + 1;
		}
		else
		{
			curtime += 1;
		}
		p[rob] = pb;
		ltime[rob] = curtime;
	}
	printf("%d\n",curtime);
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int ncase;
	scanf("%d",&ncase);
	for (int c=1; c<=ncase; c++)
	{
		printf("Case #%d: ",c);
		scanf("%d\n",&ns);
		for (int i=1;i<=ns;i++)
		{
			char tc;
			scanf("%c %d\n",&tc,&pos[i]);
			cs[i] = tc=='O' ? 1:0;
		}

		Solve();
	}
	return 0;
}