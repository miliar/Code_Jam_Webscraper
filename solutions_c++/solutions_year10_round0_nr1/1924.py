#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <cmath>

int main()
{
	int C;
	//int tab[101];
	
	scanf("%d", &C);

	for(int i = 1; i <= C; i++)
	{
		int N, K;
		/*for(int j = 1; j <= 100; j++)
			tab[j] = 0;
		tab[0] = 1;*/
	
		scanf("%d%d", &N, &K);
		
		/*for(int k = 1; k <= K; k++)
		{
			for(int j = 1; j <= N; j++)
			{
				int truc = tab[j];
				
				tab[j] = !tab[j];
				
				if(!truc)
					break;
			}
			
			bool ok = true;
		
			for(int j = 1; j <= N; j++)
				if(!tab[j])
					ok = false;

			if(ok)
				printf("ON at k=%d\n", k);
		}*/
		
		bool ok = true;
		
		while(N--)
		{
			if(K % 2 != 1)
				ok = false;
			K /= 2;
		}

		printf("Case #%d: ", i);
		if(ok)
			printf("ON\n");
		else
			printf("OFF\n");
	}
	
	return 0;
}

