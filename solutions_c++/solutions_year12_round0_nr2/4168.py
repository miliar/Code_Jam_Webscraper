#include <stdio.h>
#include <algorithm>

using namespace std;

int input[110];

int main ()
{
	int T, x, N, S, p;
	int i, j;
	int ans, count[3];
	
	scanf("%d", &T);
	
	for (j=1; j<=T; j++)
	{
		scanf("%d %d %d", &N, &S, &p);
		count[0] = count[1] = count[2] = ans = 0;
		
		for (i=0; i<N; i++)
		{
			scanf("%d", &input[i]);
			x = input[i]/3;
			
			if (input[i] == 3*x)
			{
					if (x >= p)
						ans++;
					else if (x+1 >= p and x+1<=input[i])
						count[0]++;
			}
			
			else if (input[i] == 3*x+1 and x+1 >= p)
				ans++;
			
			else if (input[i] == 3*x+2)
			{
				if (x+1 >= p)
					ans++;
				else if (x+2 >= p)
					count[2]++;
			}
		}
		
		ans += min(S, count[0]+count[2]);
		printf("Case #%d: %d\n", j, ans);
	}
	
	return 0;
}
