#include <cstdio>
#include <cstring>

int letra[30];
char oposed[30][2];
char match[30][30];

int main()
{
	char answ[1000];
	
	int cases;
	scanf("%d", &cases);
	for (int c = 1; c <= cases; c++)
	{
		int C, D, N;
		char ele, mag[5];
		scanf("%d", &C);
		memset(letra, 0, sizeof(int) * 30);
		memset(match, 0, sizeof(char) * 30 * 30);
		for (int i = 0; i < C; i++)
		{
			scanf("%s", mag);
			match[mag[0]-'A'][mag[1]-'A'] = mag[2];
			match[mag[1]-'A'][mag[0]-'A'] = mag[2];
		}
		scanf("%d", &D);
		for (int i = 0; i < D; i++)
		{
			scanf("%s", mag);
			oposed[i][0] = mag[0];
			oposed[i][1] = mag[1];
		}
		scanf("%d", &N);
		int index = 0;
		char n, o;
		scanf("%*c%c", &n);
		letra[n-'A']++;
		for (int i = 0; i < N-1; i++)
		{
			o = n;
			scanf("%c", &n);
			letra[n-'A']++;
			if (match[o-'A'][n-'A'])
			{
				answ[index] = match[o-'A'][n-'A'];
				letra[n-'A']--;
				letra[o-'A']--;
				index++;
				i++;
				o = 0;
				n = 0;
				if (i < N-1)
				{
					scanf("%c", &n);
					letra[n-'A']++;
				}
			}
			for (int j = 0; j < D; j++)
			{
				if (letra[oposed[j][0]-'A'] && letra[oposed[j][1]-'A'])
				{
					index = 0;
					memset(letra, 0, sizeof(int)*30);
					o = 0;
					n = 0;
					i++;
					if (i < N-1)
					{
						scanf("%c", &n);
						letra[n-'A']++;
					}
					break;
				}
			}
			if (o) 
			{
				answ[index] = o;
				index++;
			}
		}
		if (n)
		{
			answ[index] = n;
			index++;
		}
		printf("Case #%d: [", c);
		for (int i = 0; i < index-1; i++) printf("%c, ",answ[i]);
		if (index-1 >= 0)
		{
			printf("%c", answ[index-1]);
		}
		printf("]\n");
	}
	return 0;
}
