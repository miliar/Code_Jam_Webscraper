#include<stdio.h>
#include<string.h>
const int N = 1000+10;
int value[N];

struct node
{
	int sum;//糖果和
	int value;//异或值
}dp[1<<16];
int main()
{
	//freopen("C-small-attempt0.in","r",stdin);
	//freopen("C-small-attempt0.out","w",stdout);
	int T;
	scanf("%d",&T);
	int cases;
	for(cases=1;cases<=T;cases++)
	{
		int n;
		scanf("%d",&n);
		int i;
		int total = 0;
		for(i=0;i<n;i++)
		{
			scanf("%d",&value[i]);
		    total^=value[i];
		}
        
		int tmp;
		int upper = 1<<n;
		int half = -1;
		upper--;
		for(i=0;i<upper;i++)
		{
			dp[i].sum = 0;
			dp[i].value = 0;
			tmp = i;
			int id = 0;
			while(tmp)
			{
				if(tmp&1)
				{
					dp[i].sum+=value[id];
					dp[i].value^=value[id];
				}
				tmp>>=1;
				id++;
			}
			
			int tmp = dp[i].value^total;
			if(tmp==dp[i].value)
			{
				if(half<dp[i].sum)
					half = dp[i].sum;
			}
		}
        if(half==-1)
		printf("Case #%d: NO\n",cases);
		else
			printf("Case #%d: %d\n",cases,half);
	}
	return 0;
}