
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define  max(x, y)  ((x)>(y)?(x):(y))
#define  abs(x)   ((x)<0?-(x):(x))

char buf[1024];

// int _tmain(int argc, _TCHAR* argv[])
int main()
{
	gets(buf);
	int ncase = atoi(buf);
//	printf("%d\n", ncase);
  
	for(int i=1; i<=ncase; i++)
	{
		int  C, D, N;
		char BaseStr[200];
		char ResultStr[200];
		int  p = 0;

		int comb[26][26];
		int opplist[26][10];
		int refcount[26];

		// initialize
		for(int j=0; j<26; j++)
		{
			for(int k=0; k<26; k++)
			{
				comb[j][k] = -1;
			}
			opplist[j][0] = 0;
			refcount[j] = 0;
		}

		scanf("%d", &C);
		for(int j=1; j<=C; j++)
		{
			char  CombStr[100];
			scanf("%s", CombStr);
			char b0 = CombStr[0]-'A';
			char b1 = CombStr[1]-'A';
			comb[b0][b1] = CombStr[2]-'A';
			comb[b1][b0] = CombStr[2]-'A';
		}

		scanf("%d", &D);
		for(int j=1; j<=D; j++)
		{
			char  OppStr[100];
			scanf("%s", OppStr);
			char b0 = OppStr[0]-'A';
			char b1 = OppStr[1]-'A';

			int idx0 = opplist[b0][0];
			opplist[b0][idx0+1] = b1;
			opplist[b0][0]++;

			int idx1 = opplist[b1][0];
			opplist[b1][idx1+1] = b0;
			opplist[b1][0]++;
		}

		scanf("%d", &N);
		scanf("%s", BaseStr);

		p = 0;
		int BaseStrLen = strlen(BaseStr);
		for(int j=0; j<BaseStrLen; j++)
		{
			int  c = BaseStr[j]-'A';
			if ( p > 0 && comb[ResultStr[p-1]][c] != -1 )
			{
				refcount[ResultStr[p-1]]--;
				ResultStr[p-1] = comb[ResultStr[p-1]][c];
			}
			else
			{
				int opplistlen = opplist[c][0];
				int found = 0;
				for(int k=1; k<=opplistlen; k++)
				{
					if ( refcount[opplist[c][k]] >= 1 )
					{
						found = 1;
						break;
					}
				}
				if ( found == 1 )
				{
					// clear ResultStr and refcount 
					p = 0;
					for (int k=0; k<26; k++)
						refcount[k] = 0;
					continue;
				}
				refcount[c]++;
				ResultStr[p] = c;
				p++;
			}
		}

		printf("Case #%d:", i);
		printf(" [");
		for(int j=0; j<p; j++)
		{
			if ( j>0 )
				printf(", ");
			printf("%c", ResultStr[j]+'A');
		}
    	printf("]\n");
	}
  
	return  0;  
}

