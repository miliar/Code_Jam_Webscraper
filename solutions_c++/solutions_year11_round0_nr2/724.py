#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

const int MAX = 105, M = 27;
int com[M][M], opp[M][M];
char list[MAX], ans[MAX];
int c, d, n;

int main()
{
	FILE *f1 = fopen("input.in", "r");
	FILE *f2 = fopen("out.in", "w");
	int numcas;
	fscanf(f1, "%d", &numcas);
	for(int cas = 1; cas <= numcas; cas ++)
	{
		memset(com, -1, sizeof(com));
		memset(opp, -1, sizeof(opp));
		fscanf(f1, "%d ", &c);
		for(int i = 0; i < c; i ++)
		{
			char ch1, ch2, ch3;
			fscanf(f1, "%c%c%c ", &ch1, &ch2, &ch3);
			com[ch1-'A'][ch2-'A'] = com[ch2-'A'][ch1-'A'] = ch3-'A';
		}
		fscanf(f1, "%d ", &d);
		for(int i = 0; i < d; i ++)
		{
			char ch1, ch2;
			fscanf(f1, "%c%c ", &ch1, &ch2);
			opp[ch1-'A'][ch2-'A'] = opp[ch2-'A'][ch1-'A'] = 1;
		}
		fscanf(f1, "%d ", &n);
		fscanf(f1, "%s", list);
		fprintf(f2, "Case #%d: ", cas);
		int size = 0;
		for(int i = 0; i < n; i ++)
			if(size == 0)
				ans[size++] = list[i];
			else
			{
				int ok = 1;
				for(int j = size-1; j >= 0; j --)
					if(j==size-1 && com[list[i]-'A'][ans[j]-'A'] != -1)
					{
						ans[size-1] = com[list[i]-'A'][ans[j]-'A'] + 'A';
						ok = 0;
						break;
					}
					else if(opp[list[i]-'A'][ans[j]-'A'] != -1)
					{
						size = 0;
						ok = 0;
						break;
					}
				if(ok) ans[size++] = list[i];
			}
		fprintf(f2, "[");
		for(int i = 0; i < size; i ++)
		{
			fprintf(f2, "%c", ans[i]);
			if(i != size-1) fprintf(f2, ", ");
		}
		fprintf(f2, "]\n");
	}
	fclose(f1);
	fclose(f2);

	return 0;
}