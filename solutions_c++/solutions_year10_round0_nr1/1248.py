#include<stdio.h>
int T, N, K;
int main()
{
	freopen("large.in","r",stdin);
	freopen("large.out","w",stdout);

	int i, j;
	scanf("%d",&T);
	for(i=1;i<=T;i++)
	{
		scanf("%d %d",&N,&K);
		
		int flag = 1;
		for(j=1;j<=N;j++)
		{
			if( ( (K >> (j-1)) & 1 ) ) // �ڿ��� N��° bit�� ���̸�
				flag = flag;
			else
				flag = 0;
				
		}
		if(flag)
			printf("Case #%d: ON\n",i);
		else
			printf("Case #%d: OFF\n",i);
	}
	return 0;
}