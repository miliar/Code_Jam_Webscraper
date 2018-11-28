#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<map>
#include<vector>

using namespace std;

#define MAX 128

int v[MAX];

int main()
{
	int testes, n;
	char c;

	scanf("%d", &testes);

	for(int t = 1; t <= testes; t++)
	{
		scanf("%d", &n);

		for(int i = 0; i < n; i++)
		{
			v[i] = 0;

			for(int j = 0; j < n; j++)
			{
				scanf(" %c", &c);
				if(c == '1')
					v[i] = j;
			}
		}


		int trocas = 0, tmp;

	/*	for(int j = 0; j < n; j++)
		{
			for(int i = 0; i < n - 1; i++)
			{
				if(v[i] > i && v[i + 1] < v[i])
				{
				//	printf("Troca %d %d\n", v[i], v[i+1]);
					tmp = v[i + 1];
					v[i + 1] = v[i];
					v[i] = tmp;
					trocas++;

				}
			}
		}*/

		int s = 0, min;
		int ind = -1;

		while(s < n)
		{
			min = 222222;

			for(int j = s; j < n; j++)
			{
				if(v[j] <= s)
				{
					ind = j;
					break;
				}
			}

			while(ind != s)
			{
				if(v[ind] < v[ind-1])
				{
					tmp = v[ind];
					v[ind] = v[ind -1];
					v[ind - 1] = tmp;
					ind--;
					trocas++;
				}
				else
					break;
			}

			s++;
		}

		printf("Case #%d: %d\n",t, trocas);
	}

	return 0;
}
