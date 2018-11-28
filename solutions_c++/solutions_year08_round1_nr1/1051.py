#include <stdio.h>
#include <cstdlib>
#include <algorithm>

using namespace std;

int vec1[1000];
int vec2[1000];

int main()
{
	int cases;
	int n;
	long sum;

	freopen("A-small-attempt0.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	scanf("%d", &cases);
	for(int i = 0; i < cases; i++)
	{
		scanf("%d", &n);
		for(int j = 0; j < n; j++)
			scanf("%d", &vec1[j]);
		for(int j = 0; j < n; j++)
			scanf("%d", &vec2[j]);
		sort(vec1, vec1 + n);
		sort(vec2, vec2 + n);
		sum = 0;
		for(int j = 0; j < n; j++)
			sum += vec1[j] * vec2[n - j - 1];
		printf("Case #%d: %ld\n", i + 1, sum); 
 	}
	return 0;
}