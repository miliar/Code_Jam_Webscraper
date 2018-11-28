#include <stdio.h>
void solve(int nCase)
{
	int r,k,n;
	int group[1001];
	int i,tmpk,sum,s,e,tmpsum;
	scanf("%d %d %d",&r,&k,&n);
	for(i=0;i<n;i++)
	{
		scanf("%d",&group[i]);
	}
	s=0;
	sum=0;
	for(i=0;i<r;i++)
	{
		e=s;
		tmpk=k;

		while(tmpk-group[e]>=0)
		{
			sum+=group[e];
			tmpk-=group[e];
			e=(e+1)%n;
			if(e==s)break;
		}
		s=e;
	}
	printf("Case #%d: %d\n",nCase,sum);
}
int main()
{
	int nCase;
	int i;
	freopen("C-small-attempt0.in","r",stdin);
	freopen("test.out","w",stdout);
	scanf("%d",&nCase);
	for(i=1;i<=nCase;i++)
		solve(i);
	fclose(stdin);
	fclose(stdout);
	return 0;
}