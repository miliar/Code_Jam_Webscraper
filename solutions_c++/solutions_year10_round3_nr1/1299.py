#include <cstdio>
#include <cstring>

int TC = 1, T, N;
long A[1000],B[1000];
int main(void)
{	
	//read all test cases
	for(scanf("%d",&T);TC <= T; TC++)
	{
		int i;
		long long cut=0;
		scanf("%d",&N);
		for(int i=0;i<N;i++)
			scanf("%ld %ld",&A[i],&B[i]);

		for(int i=0;i<N;i++)
			for(int j=0;j<N-i-1;j++)
				if(A[j]>A[j+1])
				{
					long temp=A[j];
					A[j]=A[j+1];
					A[j+1]=temp;
					temp=B[j];
					B[j]=B[j+1];
					B[j+1]=temp;
				}
		for(int i=0;i<N;i++)
			for(int p=0;p<i;p++)
				if(B[p]>B[i])
					cut++;		
		printf("Case #%d: %lld\n",TC,cut);
	}
	return 0;
}

