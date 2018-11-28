#include <stdio.h>
#include <windows.h>
#include <string.h>

char strEngine[110][110];
char strQuery[1010][110];
int maxEngine, maxQuery;
int match[110][1010];
int ismatch(char *str1, char *str2)
{
	int i = 0;
	while (str1[i]!='\0' &&str2[i]!='\0'&&str1[i] == str2[i]) i++;
	if (str1[i]=='\0' && str2[i] =='\0') return 1;
	else return 0;
}
int main()
{
    int i,j,k;
    char strtemp[10];
	int result[110][1010];
    int maxCase, icase = 0, tmp;
	freopen("A-large.in.txt","r",stdin);
	freopen("A-large.out.txt","w",stdout);
    scanf("%d", &maxCase);
    while (icase++ < maxCase)
    {
          scanf("%d",&maxEngine);
          gets(strtemp);
          for (i = 0;  i < maxEngine; i ++)
              gets(strEngine[i]);
		  scanf("%d", &maxQuery);
		  gets(strtemp);
          for (i = 0;  i < maxQuery; i ++)
              gets(strQuery[i]);
		  for (i = 0; i < maxEngine; i ++)
			  for (j = 0;  j < maxQuery; j ++)
				  if (ismatch(strEngine[i], strQuery[j]))
					  match[i+1][j+1] = 1;
				  else match[i+1][j+1] = 0;
		  for (i = 0; i <=maxEngine; i ++)
			  result[i][0] = 0;
		  for (i = 1; i <=maxQuery; i ++)
			  for (j = 1; j <=maxEngine; j ++)
			  {
				  if (match[j][i]) tmp = 10000;
				  else tmp = result[j][i-1];
				  for (k = 1; k <=maxEngine; k++)
					  if (!match[k][i] && k!=j && (result[k][i-1] + 1 < tmp))
						  tmp = result[k][i-1] + 1;
				  result[j][i] = tmp;
			  }
		  tmp = 10000;
		  for (i = 1; i <= maxEngine; i ++)
			  if (tmp > result[i][maxQuery]) tmp = result[i][maxQuery];
          printf("Case #%d: %d\r\n", icase, tmp);
    }
    
    return 0;
}
