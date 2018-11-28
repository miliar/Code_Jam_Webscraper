#include <stdio.h>

struct combine
{
	char first, second, result;
};

struct destroyer
{
	char c1, c2;
};

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int numCase, cases, C, D, N, i, idxarr, j, k, l;
	combine combination[36];
	destroyer destroy[28];
	char data[200], arr[1000];
	bool destroyed;

	for(scanf("%i\n", &cases), numCase = 1; numCase <= cases; numCase++)
	{
		scanf("%i", &C);

		for(i = 0; i < C; i++)		
			scanf(" %c%c%c ", &combination[i].first, &combination[i].second,
				&combination[i].result);
		

		scanf("%i", &D);
		for(i = 0; i < D; i++)
			scanf(" %c%c ", &destroy[i].c1, &destroy[i].c2);

		scanf("%i", &N);
		scanf("%s", data);

		idxarr = 1;
		arr[0] = data[0]; // karakter pertama selalu masuk dalam list
		for(i = 1; i < N; i++)
		{
			arr[idxarr] = data[i];
						
			// cek kombinasi
			for(j = 0; j < C; j++)
			{
				if( (arr[idxarr - 1] == combination[j].first && arr[idxarr] == combination[j].second) ||
					(arr[idxarr - 1] == combination[j].second && arr[idxarr] == combination[j].first))
				{
					arr[idxarr - 1] = combination[j].result;
					idxarr--;
					break;
				}
			}

			// cek destroy
			destroyed = false;
			for(j = 0; !destroyed && j <= idxarr; j++)
			{
				for(k = j + 1; !destroyed && k <= idxarr; k++)
				{
					for(l = 0; l < D; l++)
					{
						if( (arr[j] == destroy[l].c1 && arr[k] == destroy[l].c2) ||
							(arr[j] == destroy[l].c2 && arr[k] == destroy[l].c1))
						{
							destroyed = true;
							idxarr = -1;
							break;
						}
					}
				}
			}

			idxarr++;
		}

		printf("Case #%i: [", numCase);
		for(j = 0; j < idxarr; j++)
		{
			if(j == 0) printf("%c", arr[j]);
			else printf(", %c", arr[j]);
		}
		printf("]\n");
	}
	return 0;
}