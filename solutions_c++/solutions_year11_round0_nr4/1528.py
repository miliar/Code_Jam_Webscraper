#include <stdio.h>
#include <string.h>

int main()
{
	FILE *fr = freopen("D-large.in", "r", stdin);
	FILE *fw = freopen("d.out", "w+", stdout);
	int casenum, time = 1;
	scanf("%d", &casenum);
	while(casenum--)
	{
		int N, i, temp, ans = 0;
		scanf("%d",&N);
		for(i = 1; i <= N; i++)
		{
			scanf("%d", &temp);
			if(temp!=i)	
				ans++;
		}
		printf("Case #%d: %d.000000\n", time++, ans);
	}
	return 0;
}
