#include <cstdio>

const char STR[] = "welcome to code jam";
const int LEN = 19;
const int INP_LEN = 600;
const int ALPH = 256;
const int MODD = 10000;

int num_assoc[ALPH];
int assoc[ALPH][LEN];
int table[INP_LEN][LEN];

int main()
{
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	
	int n;
	scanf("%d%*c", &n);
	
	for (int i = 0; i < LEN; i++)
	{
		assoc[STR[i]][num_assoc[STR[i]]++] = i;
	}
	
	for (int i = 0; i < n; i++)
	{
		
		for (int j = 0; j < INP_LEN; j++)
			for (int k = 0; k < LEN; k++)
				table[j][k] = 0;
			
		char tmp;
		int j;
		for (j = 0;; j++)
		{
			if (scanf("%c", &tmp) < 1)
				break;
			if ((tmp != ' ') && ((tmp < 'a') || (tmp > 'z')))
				break;
			
			if (j)
			{
				for (int k = 0; k < LEN; k++)
					table[j][k] = table[j - 1][k];
			}
			
			for (int k = 0; k < num_assoc[tmp]; k++)
			{
				if (!assoc[tmp][k])
				{
					table[j][0]++;
					table[j][0] %= MODD;
				}
				else
				{
					table[j][assoc[tmp][k]] += table[j][assoc[tmp][k] - 1];
					table[j][assoc[tmp][k]] %= MODD;
				}
			}
		}
		
		printf("Case #%d: %04d\n", i + 1, table[j - 1][LEN - 1]);
	}
	
	return 0;
}