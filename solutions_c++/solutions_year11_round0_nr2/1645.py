#include <stdio.h>
#include <string.h>

char cc[36][3];
char cct[36];
char dd[28][3];
char s[101];
char st[101];

char status[256];
char cnt[256];

int main()
{
	//freopen("B.txt", "r", stdin);
	//freopen("B-small.in", "r", stdin);
	//freopen("B-small.out.txt", "w", stdout);
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out.txt", "w", stdout);
	int i, t;
	scanf("%d", &t);
	for(i = 1; i <= t; i++)
	{
		int mc, md, n;
		int j, k;
		char temp[4];
		scanf("%d", &mc);
		for(j = 0; j < mc; j++)
		{
			scanf("%s", temp);
			cc[j][0] = temp[0];
			cc[j][1] = temp[1];
			cc[j][2] = 0;
			cct[j] = temp[2];
		}
		scanf("%d", &md);
		for(j = 0; j < md; j++)
		{
			scanf("%s", dd + j);
		}
		scanf("%d", &n);
		scanf("%s", s);
		int sp = 0;
		
		for(j = 0; j < n; j++)
		{
			st[sp++] = s[j];
			if(sp >= 2) 
			{
				bool found = true;
				while(found) {
					st[sp] = 0;
					found = false;
					for(k = 0; k < mc; k++)
					{
						if((st[sp-2] == cc[k][0] && st[sp-1] == cc[k][1]) || (st[sp-2] == cc[k][1] && st[sp-1] == cc[k][0])) {
							sp -= 2;
							st[sp++] = cct[k];
							found = true;
							break;
						}
					}
				}

				for(k = 0; k < 256; k++) status[k] = cnt[k] = 0;

				for(k = 0; k < sp; k++)	{
					status[st[k]] = 1;
					cnt[st[k]]++;
				}
				
				for(k = 0; k < md; k++)
				{
					if(status[dd[k][0]] == 1 && status[dd[k][1]] == 1) {	
						if(dd[k][0] == dd[k][1] && cnt[dd[k][0]] < 2) continue;
						sp = 0;
						break;
					}
				}
			}
		}


		printf("Case #%d: [", i);
		if(sp > 0) {
			printf("%c", st[0]);
			for(j = 1; j < sp; j++)
			{
				printf(", %c", st[j]);
			}
		}
		printf("]\n");

	}
	return 0;
}