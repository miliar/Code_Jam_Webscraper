#include <stdio.h>
#include <string.h>

int table[26] = 
{
	24,     7,      4,      18,     14,     2,      21,     23,     3,      20,
	8,      6,      11,     1,      10,     17,     25,     19,     13,     22,
	9,      15,     5,      12,     0,      16
};

int main()
{
	int i,t;
	int cases = 1;
	char str[101];
	//freopen("a.in","r",stdin);
	//freopen("a.out","w",stdout);

	scanf("%d",&t);
	gets(str);
	while(t--)
	{
		gets(str);
		printf("Case #%d: ",cases++);
		for(i=0;str[i];i++)
		{
			if(str[i]>='a' && str[i]<='z')
				printf("%c",table[str[i]-'a']+'a');
			else if(str[i]>='A' && str[i]<='A')
				printf("%c",table[str[i]-'A']+'A');
			else
				printf(" ");
		}
		printf("\n");
	}
	return 0;
}