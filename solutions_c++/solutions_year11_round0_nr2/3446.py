#include <cstdio>

int T;
int combine[26][26];
struct oppose_t
{
	int a;
	int b;
} oppose[28];
int freq[26];
int list[100];
int llist;

int main()
{
	scanf("%d", &T);
	for (int i = 1; i <= T; i++)
	{
		int C, D, N;
		for (int j = 0; j < 26; j++) for (int k = 0; k < 26; k++)
			combine[j][k] = -1;
		for (int j = 0; j < 26; j++)
			freq[j] = 0;
		scanf("%d", &C);
		for (int j = 0; j < C; j++)
		{
			char a, b, c;
			scanf(" %c%c%c", &a, &b, &c);
			if (a > b) {char tmp = a; a = b; b = tmp;}
			combine[a-'A'][b-'A'] = c-'A';
		}
		scanf("%d", &D);
		for (int j = 0; j < D; j++)
		{
			oppose_t res;
			char a, b;
			scanf(" %c%c", &a, &b);
			res.a = a-'A';
			res.b = b-'A';
			oppose[j] = res;
		}
		scanf("%d", &N);
		char chr;
		scanf(" %c", &chr);
		list[0] = chr-'A';
		freq[list[0]]++;
		llist = 1;
		//printf("Took %c\n", chr);
#define out(); //{for (int x = 0; x < llist; x++) printf("%c", (char) (list[x]+'A')); printf("\n");}
		out();
		for (int j = 1; j < N; j++)
		{
			scanf("%c", &chr);
			//printf("Took %c\n", chr);
			out();
			list[llist++] = chr-'A';
			freq[list[llist-1]]++;
			int a = list[llist-1], b = list[llist-2];
			if (a > b) {char tmp = a; a = b; b = tmp;}
			if (llist > 1 && combine[a][b] != -1)
			{
				freq[a]--; freq[b]--;
				list[llist-2] = combine[a][b];
				freq[list[llist-2]]++;
				llist--;
			}
			out();
			for (int k = 0; k < D; k++)
			{
				if (freq[oppose[k].a] > 0 && freq[oppose[k].b] > 0)
				{
					llist = 0;
					for (int l = 0; l < 26; l++)
						freq[l] = 0;
				}
			}
			out();
		}
		printf("Case #%d: [", i);
		for (int j = 0; j < llist-1; j++)
		{
			printf("%c, ", (char) (list[j]+'A'));
		}
		if (llist > 0) printf("%c]\n", (char) (list[llist-1]+'A'));
		else printf("]\n");
		}
	return 0;
}
