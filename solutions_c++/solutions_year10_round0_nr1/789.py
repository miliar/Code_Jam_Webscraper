#include <stdio.h>
#include <string.h>

using namespace std;

bool check(int n,long k)
{
	int i = 1;
	if(!k)
		return false;
	while(i<=n)
	{
		if(!(k%2))
			return false;
		k/=2;
		i++;
	}
	return true;
}

int main()
{
	int i,n,t;
	long k;
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	scanf("%d",&t);
	for(i=1;i<=t;++i)
	{
		scanf("%d %ld",&n,&k);
		printf("Case #%d: O",i);
		if(check(n,k))
			printf("N\n");
		else
			printf("FF\n");
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
