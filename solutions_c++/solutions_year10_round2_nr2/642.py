#include <cstdio>
#include <cmath>
#define MAX_N 50

int distance[MAX_N];
bool qe[MAX_N];
int blocking[MAX_N];

void testCase(int number)
{
	int N, K, B, T;
	int result = 0;
	int nqe = 0;

	// input
	scanf("%d %d %d %d", &N, &K, &B, &T);
	
	for (int i = 0; i < N; i++)
	{
		int x;
		scanf("%d", &x);
		distance[i] = B - x;
	}

	for (int i = 0; i < N; i++)
	{
		int v;
		scanf("%d", &v);
		qe[i] = (v * T >= distance[i]);
		if (qe[i]) nqe++;
	}

	if (nqe < K) {
		printf("Case #%d: IMPOSSIBLE\n", number);
		return;
	}

  int counter = 0;
	for (int i = N-1; i >= 0; i--) {
		if (!qe[i])
			counter++;
		else {
			blocking[i] = counter;
		}
	}

  for (int i = N-1; i >= 0 && K > 0; i--) {
		if (qe[i]) {
			result += blocking[i];
			K--;
		}
	}

	// output
	printf("Case #%d: %d\n", number, result);
}

int main()
{
	int t;
	scanf("%d", &t);

	for (int i = 0; i < t; i++)
	{
		testCase(i+1);
	}

	return 0;
}
