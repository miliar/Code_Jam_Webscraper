#include<stdio.h>
int main(){
	int tc;
	scanf("%d",&tc);
	int N,K,j;
	for(int i=1 ; i<=tc ; i++)
	{
		scanf("%d%d",&N,&K);

		for(j=0 ; j<N ; j++)
		{
			if( ((K>>j) & 1) != 1)
				break;
		}

		if(j==N)
		{
			printf("Case #%d: ON\n",i);
		}
		else
			printf("Case #%d: OFF\n",i);

	}
	return 0;
}
