#include<stdio.h>

void ReadFile(){
    #ifndef  ONLINE_JUDGE
    freopen("C-small-attempt0.in","r",stdin);
    #endif
}

int main()
{
	ReadFile();
	FILE * cfPtr;
	cfPtr = fopen("out.txt","w");
	int t;
	int r,k,n;
	int i;
	int sum;
	int total;
	int g[1000];
	bool flag[1000];
	scanf("%d",&t);
	int u;
	int s;
	for(u=1;u<=t;u++)
	{
		scanf("%d%d%d",&r,&k,&n);
		for(i=0;i<n;i++)
			scanf("%d",&g[i]);
		i = 0;
		total = 0;
		while(r--)
		{
			sum = 0;
			s = i;
			while(sum + g[i] <= k && (sum==0 || i!=s ))
			{
				sum += g[i];
				i = (i + 1) % n;
			}
			total += sum;
		}
		fprintf(cfPtr,"Case #%d: %d\n",u,total);
	}
	return 0;
}