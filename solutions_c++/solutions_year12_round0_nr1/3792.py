#include<cstdio>
#include<cstring>
using namespace std;

char conv(char a)
{
    switch(a)
    {
	case 'a': return 'y';
	case 'b': return 'h';
	case 'c': return 'e';
	case 'd': return 's';
	case 'e': return 'o';
	case 'f': return 'c';
	case 'g': return 'v';
	case 'h': return 'x';
	case 'i': return 'd';
	case 'j': return 'u';
	case 'k': return 'i';
	case 'l': return 'g';
	case 'm': return 'l';
	case 'n': return 'b';
	case 'o': return 'k';
	case 'p': return 'r';
	case 'q': return 'z';
	case 'r': return 't';
	case 's': return 'n';
	case 't': return 'w';
	case 'u': return 'j';
	case 'v': return 'p';
	case 'w': return 'f';
	case 'x': return 'm';
	case 'y': return 'a';
	case 'z': return 'q';
	case ' ': return ' ';
    }
}

int main()
{
    int t, i = 1;
    scanf("%d", &t);
    while(t--)
    {
	char inp[102];
	scanf(" %[^\n]", inp);
	printf("Case #%d: ", i);
	i++;
	for(int j = 0; j < strlen(inp); j++)
	{
	    printf("%c",conv(inp[j]));
	}
	printf("\n");
    }
    return 0;
}
