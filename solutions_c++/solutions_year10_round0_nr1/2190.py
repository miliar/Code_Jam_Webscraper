#include <stdio.h>
bool getstate(int i,int k)
{
	long mod,half;
	long tmp;
	mod=1<<i;
	half=1<<(i-1);
	tmp=k%mod;
	if(tmp<half)
		return false;
	else
		return true;
}
void solve(int nCase)
{
	int i;
	long k,n;
	scanf("%d %d",&n,&k);
	for(i=1;i<=n;i++)
	{
		if(!getstate(i,k))
		{
			printf("Case #%d: OFF\n",nCase);
			return;
		}
	}
	printf("Case #%d: ON\n",nCase);
}
int main()
{
	int i,nCase;
	freopen("A-large.in","r",stdin);
	freopen("A-large.in.out","w",stdout);
	scanf("%d",&nCase);
	for(i=0;i<nCase;i++)
		solve(i+1);
	fclose(stdin);
	fclose(stdout);
	return 0;
}
