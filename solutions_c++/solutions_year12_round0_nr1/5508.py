#include <cstdio>
#include <cstring>

using namespace std;

char str[200];
char a[30] = 
{
	'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'
//	'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
};

int main()
{
	int casenum;
	scanf("%d", &casenum);
	gets(str);
	
	int ii = casenum;
	while (ii--)
	{
		gets(str);
		printf("Case #%d: ", casenum-ii);
		for (int i=0; i<strlen(str); i++)
		{
			if (str[i]>='a' && str[i]<='z')
				printf("%c", a[str[i]-'a']);
			else
				printf("%c", str[i]);
		}
		puts("");
		
	}
	
	return 0;
	
}

