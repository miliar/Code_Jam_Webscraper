#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>

using namespace std;

int q[1000];
int ex[1000];

int main()
{
	int ca, T, i, j, k;
	int n;
	char tmp[100];
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	
	scanf("%d",&T);
	for(ca = 1; ca <= T; ca ++)
	{
		scanf("%d",&n);
		for(i=1;i<=n;i++){
			scanf("%s%d",tmp, &j);
			if(tmp[0]=='O') q[i] = j;
			else q[i] = 101 + j;
		}
		memset(ex, 0, sizeof(ex));
		for(i=1;i<=n;i++)
		{
			if(q[i]<=100){
				ex[i] = q[i];
				break;
			}
		}

		for(i=1;i<=n;i++)
		{
			if(q[i]>101){
				ex[i] = q[i] - 101;
				break;
			}
		}
		
		for(i = 1; i <= n; i++)
		{
			if(i > 1)
			{
				if((q[i]-101)*(q[i-1]-101)<0)
					ex[i] = max(ex[i], ex[i-1]+1);
				
			}
			for(j=i+1;j<=n;j++)
			{
				if((q[i]-101)*(q[j]-101)>0){
					ex[j] = ex[i] + (q[i]-q[j] > 0? q[i]-q[j] : q[j]-q[i]) + 1;
					break;
				}
			}
		}
		/*for(i=1;i<=n;i++)
			printf("%d ",ex[i]);
			printf("\n");*/
		printf("Case #%d: %d\n", ca, ex[n]);
	}
	return 0;
}
			
					
			
			

