#include<iostream>
#include<cstdio>

using namespace std;

int A[200];

void Money(int t)
{
	int n, j;	
	scanf("%d", &n);
	int xr = 0;
	int sum = 0, min = 0x7fffffff;
	for (int i = 0; i < n; i++) {
		scanf("%d", &A[i]);
		sum += A[i];
		if (A[i] < min) min = A[i];
		xr ^= A[i];
	}

	if (xr) {
		printf("Case #%d: NO\n", t);
		return;
	}
	printf("Case #%d: %d\n", t, sum-min);
	return;
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)Money(i);
	return 0;
}
