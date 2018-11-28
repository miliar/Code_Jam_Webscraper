#include<iostream>
#include<stdio.h>
using namespace std;
#include<vector>
#include<map>
#include<algorithm>
#include<string>
#include<stdlib.h>

int a[1000];
int b[1000];
int cmp1(const void * p1, const void * p2)
{
	int t1 = *((int *)p1);
	int t2 = *((int *)p2);
	return t1 - t2;
}
int cmp2(const void * p1, const void * p2)
{
	int t1 = *((int *)p1);
	int t2 = *((int *)p2);
	return t2 - t1;
}
int main()
{
	int n;
	int i;
	freopen( "test.in", "r", stdin );
	freopen( "test.out", "w", stdout );
	scanf("%d", &n);
	for(i = 0; i < n; i++)
	{
		int num;
		scanf("%d", &num);
		int j;
		for(j = 0; j < num; j++)
			scanf("%d", &a[j]);
		for(j = 0; j < num; j++)
			scanf("%d", &b[j]);

		qsort(a, num, sizeof(a[0]), cmp1);
		qsort(b, num, sizeof(b[0]), cmp2);
		__int64 mn = 0;
		for(j = 0; j < num; j++)
		{
			mn = mn + a[j] * b[j];
		}
		printf("Case #%d: %I64d\n", i + 1, mn);
	}
}