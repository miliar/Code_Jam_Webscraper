#include <stdio.h>
#include <string.h>

int main()
{
	int nCase = 0;
	scanf("%d\n", &nCase);

	int score;
	for (int i=0; i<nCase; i++)
	{
		int N, S, p;
		scanf("%d %d %d", &N, &S, &p);
		int res = 0;
		for (int j=0; j<N; j++)
		{
			scanf("%d", &score);
			if (score >= p*3)
			{
				res++;
			}
			else if (score+2 >= p*3 && p-1 >= 0)
			{
				res++;
			}
			else if (S > 0 && score+4 >= p*3 && p-2 >= 0)
			{
				S--;
				res++;
			}			
		}

		printf("Case #%d: %d\n", i+1, res);
	}
	return 0;
}
