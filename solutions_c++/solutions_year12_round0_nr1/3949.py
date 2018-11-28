#include <iostream>
#include <cstdio>
using namespace std;

char code[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u',
                 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w',
                 'j', 'p', 'f', 'm', 'a', 'q'};

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int t, i, cnt = 1;
	char mess[105];
	scanf("%d",&t);
	getchar();	
	while(t--)
	{
		gets(mess);
		printf("Case #%d: ", cnt++);
		for(i = 0; mess[i] != '\0'; i++)
		{
			if(mess[i] == ' ')
				printf(" ");
			else
				printf("%c", code[mess[i] - 'a']);
		}
		printf("\n");
	}
	return 0;
}
