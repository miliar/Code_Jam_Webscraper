#include <cstdio>
#include <algorithm>

bool check(int A, int B)
{
	if (A==B) return false;
	if (B>A) std::swap(A,B);
	if (B==1) return true;
	if (A%B==0) return true;
	if (B%(A-B)==0) return false;
	if (A-B<B) return !check(B, A-B);
	return true;
}

__int64 calc(int A1, int A2, int B1, int B2)
{
	__int64 res = 0;
	for (int i=A1;i<=A2;++i)
	{
		for (int j=B1;j<=B2;++j)
		{
			if (check(i,j)) ++res;
		}
	}
	return res;
}

void main()
{
	unsigned int N, A1, A2, B1, B2;

	scanf("%u\n",&N);
	for (unsigned int i=1;i<=N;++i)
	{
		scanf("%u %u %u %u\n", &A1, &A2, &B1, &B2);
		printf("Case #%u: %I64d\n", i, calc(A1, A2, B1, B2));
	}
}
