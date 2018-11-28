#include<stdio.h>

char a[11111]="ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjvyqeez";
char b[11111]="ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveupazooq";

char Map[1111];
int T;
int l0;

int main(void)
{
	int l1;

	for(l1=0;l1<300;l1++)
	{
		Map[l1] = (char)l1;
	}

	for(l1=0;a[l1];l1++)
	{
		Map[a[l1]] = b[l1];
	}
	a[' '] = ' ';

	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);

	gets(a);
	sscanf(a,"%d",&T);

	for(l0=1;l0<=T;l0++)
	{
		gets(a);
		for(l1=0;a[l1];l1++)
		{
			a[l1] = Map[a[l1]];
		}
		printf("Case #%d: ",l0);
		puts(a);
	}


	return 0;
}