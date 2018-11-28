#include <stdio.h>
#include <string.h>

int A[100][2];
int B[100][2];

int main()
{
    int n;
    int t;
    int na,nb;//a,b¸öÊý
	int i,j;
	int p,k;
	int numa,numb;
	int temp;
    freopen("B-large.in","r",stdin);
    freopen("B.out","w",stdout);
    scanf("%d",&n);
    for(i = 0; i < n; i++)
    {
		numa = 0;
		numb = 0;
		scanf("%d",&t);
		scanf("%d %d",&na,&nb);
		for(j = 0; j < na; j++)
		{
			scanf("%d:%d",&p,&k);
			A[j][1] = p*60+k;
			scanf("%d:%d",&p,&k);
			A[j][2] = p*60+k;
		}
		for(j = 0; j < nb; j++)
		{
			scanf("%d:%d",&p,&k);
			B[j][1] = p*60+k;
			scanf("%d:%d",&p,&k);
			B[j][2] = p*60+k;
		}
		for(j = 0;j < na-1; j++)
		{
			for(k = j+1;k < na;k++)
			{
				if(A[j][1] > A[k][1])
				{
					temp = A[j][1];
					A[j][1] = A[k][1];
					A[k][1] = temp;
				}
			}
		}
		for(j = 0;j < na-1; j++)
		{
			for(k = j+1;k < na;k++)
			{
				if(A[j][2] > A[k][2])
				{
					temp = A[j][2];
					A[j][2] = A[k][2];
					A[k][2] = temp;
				}
			}
		}
		for(j = 0;j < nb-1; j++)
		{
			for(k = j+1;k < nb;k++)
			{
				if(B[j][1] > B[k][1])
				{
					temp = B[j][1];
					B[j][1] = B[k][1];
					B[k][1] = temp;
				}
			}
		}
		for(j = 0;j < nb-1; j++)
		{
			for(k = j+1;k < nb;k++)
			{
				if(B[j][2] > B[k][2])
				{
					temp = B[j][2];
					B[j][2] = B[k][2];
					B[k][2] = temp;
				}
			}
		}
		for(j = 0;j < na; j++)
		{
			temp = 0;
			for(k = 0; k < nb; k++)
			{
				if((A[j][1] - B[k][2] -t) >= 0)
				{
					B[k][2] = 9999;
					temp++;
					break;
				}
			}
			if(temp == 0)
			{
				numa++;
			}
		}
		
		for(j = 0;j < nb; j++)
		{
			temp = 0;
			for(k = 0; k < na; k++)
			{
				if((B[j][1] - A[k][2] -t) >= 0)
				{
					A[k][2] = 9999;
					temp++;
					break;
				}
			}
			if(temp == 0)
			{
				numb++;
			}
		}
		printf("Case #%d: %d %d\n",i+1,numa,numb);
    }
    return 0;
}

























