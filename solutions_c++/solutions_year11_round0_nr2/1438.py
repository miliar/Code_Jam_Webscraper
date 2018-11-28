#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int combine[26][26];
bool opp[26][26];
int sol[1002];
char line[1002];

int main()
{
	freopen("data.in","r",stdin);
	freopen("data.out","w",stdout);
	int nCase;
	scanf("%d",&nCase);
	for (int nc=0;nc<nCase;nc++)
	{
		char tmp[20];
		memset(combine,0,sizeof(combine));
		memset(opp,0,sizeof(opp));
		int c;
		scanf("%d",&c);
		for (int i=0;i<c;i++)
		{
			scanf("%s",tmp);
			combine[tmp[0]-'A'][tmp[1]-'A'] = combine[tmp[1]-'A'][tmp[0]-'A'] = tmp[2]-'A';
		}
		int d;
		scanf("%d",&d);
		for (int i=0;i<d;i++)
		{
			scanf("%s",tmp);
			opp[tmp[0]-'A'][tmp[1]-'A'] = opp[tmp[1]-'A'][tmp[0]-'A'] = true;
		}
		int len;
		scanf("%d",&len);
		scanf("%s",line);
//		cerr << line << endl;
		int pos = 0;

		for (int i=0;i<len;i++)
		{
			sol[pos++] = line[i] - 'A';
			if (pos > 1)
			{
				if (combine[sol[pos-1]][sol[pos-2]] > 0)
				{
					sol[pos-2] = combine[sol[pos-1]][sol[pos-2]];
					pos -= 1;
					continue;
				}

				for (int k=0;k<pos;k++)
					for (int l=k+1;l<pos;l++)
				if (opp[sol[k]][sol[l]])
				{
					pos = 0;
				}
			}
		}
		printf("Case #%d: [",nc+1);
		for (int i=0;i<pos;i++)
			if (i)
				printf(", %c",sol[i] + 'A');
			else
				printf("%c",sol[i]+'A');
		printf("]\n");
	}
	return	0;
}