#include <cstdio>
#include <algorithm>

using namespace std;

int N;
int A[100];
char Buf[100];

void Work()
{
	// A[i] <= i
	scanf("%d", &N);
	for (int i = 0; i < N; i ++)
	{
		scanf("%s", &Buf);
		A[i] = -1;
		for (int j = N - 1; j >= 0; j --)
			if (Buf[j] == '1')
			{
				A[i] = j;
				break;
			}
	}
	int Ans = 0;
	for (int i = 0; i < N; i ++)
	{
		int Ptr = -1;
		for (int j = i; j < N; j ++)
			if (A[j] <= i)
			{
				Ptr = j;
				break;
			}
		Ans += Ptr - i;
		for (int j = Ptr; j > i; j --)
			swap(A[j], A[j - 1]);
	}
	printf("%d\n", Ans);
}

int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	
	int Cases;
	scanf("%d", &Cases);
	for (int Case = 1; Case <= Cases; Case ++)
	{
		printf("Case #%d: ", Case);
		Work();
	}
	return 0;
}
