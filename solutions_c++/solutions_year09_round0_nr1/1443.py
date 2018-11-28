#include <cstdio>

const int MAX_DICT_LEN = 5100;
const int MAX_W_LEN = 20;
const int ALPH = 30;

char dict[MAX_DICT_LEN][MAX_W_LEN];
char pattern[MAX_W_LEN][ALPH];

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	
	int l, d, n;
	scanf("%d%d%d", &l, &d, &n);
	
	for (int i = 0; i < d; i++)
	{
		for (int j = 0; j < l; j++)
		{
			do
			{
				scanf("%c", &(dict[i][j]));
			}
			while ((dict[i][j] < 'a') || (dict[i][j] > 'z'));
		}
	}
	
	for (int i = 0; i < n; i++)
	{
		int res = 0;
		
		for (int j = 0; j < MAX_W_LEN; j++)
			for (int k = 0; k < ALPH; k++)
				pattern[j][k] = 0;
		
		char tmp;
		for (int j = 0; j < l; j++)
		{
			do
			{
				scanf("%c", &tmp);
			}
			while (((tmp < 'a') || (tmp > 'z')) && (tmp != '(') && (tmp != ')'));
			
			if (tmp != '(')
			{
				pattern[j][tmp - 'a'] = 1;
			}
			else
			{
				scanf("%c", &tmp);
				do
				{
					pattern[j][tmp - 'a'] = 1;
					scanf("%c", &tmp);
				}
				while (tmp != ')');
			}
		}
		
		for (int j = 0; j < d; j++)
		{
			int k = 0;
			for (; k < l; k++)
			{
				if (!pattern[k][dict[j][k] - 'a'])
					break;
			}
			if (k == l)
				res++;
		}
		
		printf("Case #%d: %d\n", i + 1, res);
	}
	
	return 0;
}