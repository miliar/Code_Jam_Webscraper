#include<stdio.h>
int main(){
	int tc , N ;
	long long int answer ;
	int A[2000] , B[2000];
	scanf("%d",&tc);
	for(int i=1 ; i<=tc ; i++)
	{
		answer=0;
		scanf("%d",&N);
		for( int j=1; j<=N ; j++)
		{
			scanf("%d%d",&A[j] , &B[j]);
		}

		for(int j =1 ;j<=N ; j++)
		{
			for(int k=j ; k<=N ; k++)
			{
				if(j==k)
					continue;
				if((A[j] > A[k] && B[j] < B[k]) || A[k] > A[j] && B[k] < B[j])
					answer++;
			}
		}

		printf("Case #%d: %lld\n",i,answer);
	}
	return 0;
}
