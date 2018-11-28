#include <map>
#include <string>
#include <iostream>
#include <algorithm>
using namespace std;


int T, N;
int main()
{
	freopen("C-large.in", "r",stdin);
	freopen("C3.txt", "w", stdout);
	scanf("%d", &T);
	for (int i=1; i<=T; i++)
	{
		int C[1001];
		scanf("%d", &N);
		int sum = 0;
		for (int j=0; j<N; j++)
		{
			scanf("%d", &C[j]);
		}
		sort(C, C+N);
		int res = C[0];
		for (int j=1; j<N; j++)
		{
			sum += C[j];
			res ^= C[j];
		}
		printf("Case #%d: ", i);
		if(res != 0)
		{
			puts("NO");
		}
		else 
		{
			printf("%d\n", sum);
		}
	}
//	while(1);
	return 0;
}