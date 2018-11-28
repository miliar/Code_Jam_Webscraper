#include <stdio.h>

int main()
{
	char MagickaC[30][30];
	char MagickaD[30][30];
	char Ans[120];
	char chA, chB, chC, chD;
	int T, N, i, j, k, c, d, n, len;
	bool isBreak = false;
	scanf(" %d", &T);

	for(i=0 ; i<T ; i++)
	{
		for (j=0 ; j<30 ; j++)
		{
			for (k=0 ; k<30 ; k++)
			{
				MagickaC[j][k] = '0';
				MagickaD[j][k] = '0';
			}
		}

		scanf(" %d", &c);
		for(j=0 ; j<c ; j++)
		{
			scanf(" %c", &chA);
			scanf(" %c", &chB);
			scanf(" %c", &chC);
			MagickaC[chA-'A'][chB-'A'] = chC;
			MagickaC[chB-'A'][chA-'A'] = chC;
		}
		
		scanf(" %d", &d);
		for(j=0 ; j<d ; j++)
		{
			scanf(" %c", &chA);
			scanf(" %c", &chB);
			MagickaD[chA-'A'][chB-'A'] = '1';
			MagickaD[chB-'A'][chA-'A'] = '1';
		}
		
		scanf(" %d", &n);
		len = 0;
		for(j=0 ; j<n ; j++)
		{
			scanf(" %c", &Ans[len++]);
			isBreak = false;
			while(len > 1)
			{
				if(MagickaC[Ans[len-1] - 'A'][Ans[len-2] - 'A'] != '0')
				{
					Ans[len-2] = MagickaC[Ans[len-1] - 'A'][Ans[len-2] - 'A'];
					len--;
				}
				else
				{
					for(k = len-2 ; k >=0 ; k--)
					{
						if(MagickaD[Ans[k] - 'A'][Ans[len-1] - 'A'] == '1')
						{
							len = 0;
							break;
						}
					}
					isBreak = true;
				}
				if(isBreak == true)
					break;
			}
		}

		printf("Case #%d: [", i+1);
		for(j=0 ; j<len ; j++)
		{
			if(j != len-1)
				printf("%c, ",Ans[j]);
			else
				printf("%c",Ans[j]);
		}
		printf("]\n");
	}
	return 0;
}