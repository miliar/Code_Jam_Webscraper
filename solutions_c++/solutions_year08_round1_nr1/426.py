#include<iostream>
using namespace std;

long long A[1024], B[1024];
int n;

int main()
{
	freopen("A_L.in", "r", stdin);
	freopen("A_L.out", "w", stdout);
	int T, i, j;
	int ctr = 0;
	long long Res;
	scanf("%d", &T);
	while(T--)
	{
		scanf("%d", &n);
		for(i = 0;i < n; i++)
			scanf("%I64d", &A[i]);
        sort(A, A + n);
		for(j = 0; j < n; j++)
			scanf("%I64d", &B[j]);
        sort(B, B + n);
        Res = 0;
		for(i = 0; i < n; ++i)
            Res += A[i] * B[n - i - 1];
		printf("Case #%d: %I64d\n", ++ctr, Res);
	}
}
