#include <stdio.h>

char cmb[30][30];
bool del[30][30];

int main(void)
{
	int t;
	scanf("%d",&t);
	for(int j=0;j<t;++j)
	{
		int c,d,n,pos = 0;
		char tmp[110];
		char str[110];
		for(int i=0;i<26;++i)
		{
			for(int j=0;j<26;++j)
			{
				cmb[i][j] = 0;
				del[i][j] = false;
			}
		}
		scanf("%d",&c);
		for(int i=0;i<c;++i)
		{
			scanf("%s",tmp);
			cmb[tmp[0]-'A'][tmp[1]-'A'] = tmp[2];
			cmb[tmp[1]-'A'][tmp[0]-'A'] = tmp[2];
		}
		scanf("%d",&d);
		for(int i=0;i<d;++i)
		{
			scanf("%s",tmp);
			del[tmp[0]-'A'][tmp[1]-'A'] = true;
			del[tmp[1]-'A'][tmp[0]-'A'] = true;
		}
		scanf("%d%s",&n,tmp);
		for(int i=0;i<n;++i)
		{
			str[pos++] = tmp[i];
			if(pos>1)
			{
				int a = str[pos-1]-'A',b = str[pos-2]-'A';
				if(cmb[a][b])
				{
					str[pos-2] = cmb[a][b];
					--pos;
					continue;
				}
			}
			for(int i=0;i<pos;++i)
			{
				int a = str[pos-1]-'A';
				int b = str[i]-'A';
				if(del[a][b])
				{
					pos = 0;
					break;
				}
			}
		}
		printf("Case #%d: [",j+1);
		for(int i=0;i<pos;++i)
		{
			if(i!=pos-1)printf("%c, ",str[i]);
			else printf("%c",str[i]);
		}
		printf("]\n");
	}
	return 0;
}
