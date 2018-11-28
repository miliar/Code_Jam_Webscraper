#include <cstdio>
#include <algorithm>
using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);	
	int nt;
	scanf("%d\n", &nt);	
	for (int t = 1; t <= nt; t++)
	{
		int n;
		scanf("%d", &n);		
		int s = 0;
		int p = 1000000000;
		int q = 0;
		for (int i = 0; i < n; i++)
		{
			int c;
			scanf("%d", &c);
			p = min(p, c);
			s += c;
			q ^= c;
		}
		printf("Case #%d: ", t);
		if (q == 0) 
		{
			printf("%d\n", s - p);
		}
		else
		{
			printf("NO\n");
		}
		
	}	
	return 0;
}