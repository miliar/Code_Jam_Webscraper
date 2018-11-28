#include <stdio.h>

bool Win(int A, int B)
{
	if (A<B)
	{
		int t = B;
		B = A;
		A = t;
	}

	//printf("%d %d \n", A,B);
	if (A==B)
	{
		return false;
	}
	if (A == 0 || B == 0)
	{
		return false;
	}
		
	int k = A/B;
	for(int i=k;i>=1;--i)
	{
		if (!Win(A-i*B, B))
		{
			return true;
		}
	}
	
	return false;
};

int main()
{
	int T;
	scanf("%d", &T);
	
	for(int i=0;i<T;i++)
	{
		int A1, A2, B1, B2;
		scanf("%d %d %d %d", &A1, &A2, &B1, &B2);
		
		int count = 0;
		for(int j=A1;j<=A2;j++)
		{
			
			for(int k=B1;k<=B2;k++)
			{
		//	printf("%d %d %d %d\n", A1, A2, B1, B2);
				if (Win(j,k))
				{
				//	printf("win %d %d\n", j, k);
					count++;
				}
			}
		}
		
		printf("Case #%d: %d\n", i+1, count);
	}
	
}
