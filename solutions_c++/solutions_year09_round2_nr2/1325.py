#include<cstdio>
#include<cstring>

void digits(int s,int A[11])
{
	memset(A,0,44);
	while(s > 0)
	{
		A[s%10]++;
		//printf("%d %d %d\n",s,s%10,A[s%10]);
		s /= 10;
	}
}

bool equal(int A[11],int B[11])
{
	for(int i = 1;i <= 9;++i)
	{
		if(A[i] != B[i]) return false;
	}
	return true;
}

int main()
{
	int T,N;
	scanf("%d\n",&T);
	int A[11],B[11];

	for(int ii = 1;ii <= T;++ii)
	{
		scanf("%d\n",&N);
		digits(N,B);
		int s = N+1;
		//for(int i = 1;i <= 9;++i) printf("%d %d\n",N,B[i]);
		while(1)
		{
			digits(s,A);
			if(equal(A,B)) break;
			s++;
		}
		printf("Case #%d: %d\n",ii,s);
	}
	return 0;
}
