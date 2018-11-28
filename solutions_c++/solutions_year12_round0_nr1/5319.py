#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std;

void prnt(char c)
{
	switch(c)
	{
		case 'a':
			printf("y");
			return;
		case 'b':
			printf("h");
			return;
		case 'c':
			printf("e");
			return;
		case 'd':
			printf("s");
			return;
		case 'e':
			printf("o");
			return;
		case 'f':
			printf("c");
			return;
		case 'g':
			printf("v");
			return;
		case 'h':
			printf("x");
			return;
		case 'i':
			printf("d");
			return;
		case 'j':
			printf("u");
			return;
		case 'k':
			printf("i");
			return;
		case 'l':
			printf("g");
			return;
		case 'm':
			printf("l");
			return;
		case 'n':
			printf("b");
			return;
		case 'o':
			printf("k");
			return;
		case 'p':
			printf("r");
			return;
		case 'q':
			printf("z");
			return;
		case 'r':
			printf("t");
			return;
		case 's':
			printf("n");
			return;
		case 't':
			printf("w");
			return;
		case 'u':
			printf("j");
			return;
		case 'v':
			printf("p");
			return;
		case 'w':
			printf("f");
			return;
		case 'x':
			printf("m");
			return;
		case 'y':
			printf("a");
			return;
		case 'z':
			printf("q");
			return;


	}
}

int main()
{
	int t;
	scanf("%d",&t);
	int j = 1;
	while(t--)
	{
		char s[110];
		getchar();
		scanf("%[^\n]",s);
		printf("Case #%d: ",j);
		for(int i=0;i<strlen(s);i++)
		{
			if(s[i] == ' ')
				printf(" ");
			else
				prnt(s[i]);
		}
		printf("\n");
		j++;
//		printf("\nreal\n");
//		printf("%s\n",s);
	}
}

