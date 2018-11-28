#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>

using namespace std;

char hash[128];

int main(void)
{
	char table[3][2][200] = {	{"ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand"},
							{"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities"},
							{"de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up"}
						};

	for(int i=0;i<3;i++)
	{
		int len=strlen(table[i][0]);
		for(int j=0;j<len;j++)
		{
			if(table[i][0][j]==' ') continue;
			hash[table[i][0][j]]=table[i][1][j];
		}
	}

	hash['q']='z';
	hash['z']='q';

	int n;
	scanf("%d", &n);
	char temp[101];
	gets(temp);

	for(int caseN=1;caseN<=n;caseN++)
	{
		gets(temp);
		printf("Case #%d: ", caseN);
		int len = strlen(temp);
		for(int i=0;i<len;i++) if(temp[i]==' ') printf(" "); else printf("%c", hash[temp[i]]);
		printf("\n");
	}

	return 0;
}
