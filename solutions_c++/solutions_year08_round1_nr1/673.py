#include <cstdio>
#include <algorithm>
using namespace std;

const int N = 800;

int upgrade(const void *arg1, const void *arg2)
{
	return *((int*)arg1) - *((int*)arg2);
}

int degrade(const void *arg1, const void *arg2)
{
	return *((int*)arg2) - *((int*)arg1);
}


int main()
{
	int x[N+1];
	int y[N+1];
	int t ; //test cases
	int k; //test case number
	int n; //vector size
	__int64 sum;
	scanf("%d", &t);
	k = 1;
	while(k<=t)
	{	
		scanf("%d", &n);
		for(int i=0; i<n; i++)
			scanf("%d", &x[i]);			
		for(int i=0; i<n; i++)
			scanf("%d", &y[i]);			
		qsort(x, n, sizeof(int), upgrade);
		qsort(y, n, sizeof(int), degrade);
		sum = 0;
		for(int i=0; i<n; i++)
		{
			sum += x[i]*y[i];
		}
		printf("Case #%d: %I64d\n", k, sum);

		k++;
	}
	return 0;
}