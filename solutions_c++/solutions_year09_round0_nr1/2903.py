#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <string>
#include <list>
#include <set>
#include <algorithm>

using namespace std;

char str[5001][16];
char tmp[200000];

char dic[16][27];
int main(void)
{
	int L, D, N;
	int i, j, t, len;
	int cnt;
	FILE *fp;
	FILE *fp2;

	//cin >> L >> D >> N;
	fp = fopen("C:\\A-large.in", "r+");
	fp2 = fopen("C:\\A-large.out", "w+");

	fscanf(fp, "%d %d %d", &L, &D, &N);

	for(i=0; i<D; i++)
		fscanf(fp, "%s", &str[i]);

	for(t=1; t<=N; t++)
	{
		fscanf(fp, "%s", tmp);
		len = strlen(tmp);

		memset(dic, 0, sizeof(dic));
		j = 0;
		for(i=0; i<len; i++)
		{
			if(tmp[i] == '(')
			{
				i++;
				while(tmp[i] != ')')
				{
					dic[j][tmp[i]-'a'] = 1;
					i++;
				}
			}
			else
			{
				dic[j][tmp[i]-'a'] = 1;
			}
			j++;
		}

		fprintf(fp2, "Case #%d: ", t);
		
		cnt = 0;
		for(i=0; i<D; i++)
		{
			for(j=0; j<L; j++)
			{
				if(dic[j][str[i][j]-'a'] == 0) break;
			}
			if(j==L) cnt++;
		}
		fprintf(fp2, "%d\n", cnt);

	}

	return 0;
}