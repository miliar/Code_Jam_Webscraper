#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <set>
#include <map>

#define MAX 256

using namespace std;

set<string>ini;

char base[MAX];
map<string,char>comb;


char temp[MAX];

char resp[MAX];
char teste[MAX];
int tam;	

int main()
{
	int cas, casos;
	
	scanf("%d", &casos);
	
	
	memset(base,0,sizeof(base));
	base[(int)'Q'] = 1;
	base[(int)'W'] = 1;
	base[(int)'E'] = 1;
	base[(int)'R'] = 1;
	base[(int)'A'] = 1;
	base[(int)'S'] = 1;
	base[(int)'D'] = 1;
	base[(int)'F'] = 1;
	
	int c, d, n;
	int i, j, a, b;
	char carac, c2;
	
	for (cas = 1; cas <= casos; cas++)
	{
		printf("Case #%d: [", cas);
		scanf("%d", &c);
		
		comb.clear();
		ini.clear();
		
		for (i=0; i<c; i++)
		{
			scanf("%s", temp);
			c2 = temp[2];
			
			temp[2] = 0;
			comb[temp] = c2;
			
			carac = temp[0];
			temp[0] = temp[1];
			temp[1] = carac;
			comb[temp] = c2;

		}
		
		scanf("%d", &d);
		
		for (i=0; i<d; i++)
		{
			scanf("%s", temp);
			
			ini.insert(temp);
			
			carac = temp[0];
			temp[0] = temp[1];
			temp[1] = carac;			

			ini.insert(temp);
		}
		
		scanf("%d %s", &n, temp);
		
		teste[2] = 0;
		for (i=0, j=0; i<n; i++)
		{
			resp[j] = temp[i];
			j++;

			if (j == 1)
			{
				continue;
			}
			
			teste[0] = resp[j-1];
			teste[1] = resp[j-2];
			
			if (comb.find(teste)!=comb.end())
			{
				j--;
				resp[j-1] = comb[teste];
				continue;
			}
			
			
			for (a = 0; a<j && j>0; a++)
			{
				if (!base[(int)resp[a]])
					continue;
				teste[0] = resp[a];
				teste[1] = temp[i];
				if (ini.find(teste)!=ini.end())
				{
					j = 0;
				}
			}
			
			
		}
		
		for (i=0; i<j; i++)
		{
			if (i)
				printf(", ");
			printf("%c", resp[i]);
		}
		
		printf("]\n");
	}
	
	
	return 0;
}
