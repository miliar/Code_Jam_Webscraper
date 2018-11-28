#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

typedef vector<int> vint;

int T;


bool IS(int a1, int b1, int a2, int b2)
{
	return (a1 <= b2 && b2 <= b1) && (a1 <= a2 && a2 <= b1) ||
		(a2 <= b1 && b1 <= b2) && (a2 <= a1 && a1 <= b2) ||
		(b1 <= b2 && b2 <= a1) && (b1 <= a2 && a2 <= a1) ||
		(b2 <= b1 && b1 <= a2) && (b2 <= a1 && a1 <= a2) ||
		(a1 <= a2 && b1 >= b2) || (a2 <= a1 && b2 >= b1);
}

int main()
{
	freopen("A1.in", "r", stdin);
	freopen("A1.out", "w", stdout);
	scanf("%d", &T);
	for(int I = 0; I < T; ++I)
	{
		int n;
		scanf("%d", &n);
		vint A, B;
		A.resize(n);
		B.resize(n);
		for(int i = 0; i < n; ++i)
		{
			scanf("%d", &A[i]);
			scanf("%d", &B[i]);
		}
		int res = 0;
		for(int i = 0; i < n; ++i)
		{
			for(int j = i + 1; j < n; ++j)
			{
				if (IS(A[i], B[i], A[j], B[j])) ++res;
			}
		}
		printf("Case #%d: %d\n", I + 1, res);
	}
	return 0;
}