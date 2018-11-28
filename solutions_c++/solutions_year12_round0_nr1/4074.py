#include <stdio.h>
#include <string.h>
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	char str[1000],ch;
	int n,len,i;
	scanf("%d ",&n);
	for(int k=0;k<n;k++)
	{
		gets(str);
		len = strlen(str);
		printf("Case #%d: ",k+1);
		for(i=0;i<len;i++)
		{
			ch = ' ';
			switch(str[i])
			{
			case 'a':
	 ch = 'y';
	break;
case 'b':
	 ch = 'h';
	break;
case 'c':
	 ch = 'e';
	break;
case 'd':
	 ch = 's';
	break;
case 'e':
	 ch = 'o';
	break;
case 'f':
	 ch = 'c';
	break;
case 'g':
	 ch = 'v';
	break;
case 'h':
	 ch = 'x';
	break;
case 'i':
	 ch = 'd';
	break;
case 'j':
	 ch = 'u';
	break;
case 'k':
	 ch = 'i';
	break;
case 'l':
	 ch = 'g';
	break;
case 'm':
	 ch = 'l';
	break;
case 'n':
	 ch = 'b';
	break;
case 'o':
	 ch = 'k';
	break;
case 'p':
	 ch = 'r';
	break;
case 'q':
	 ch = 'z';
	break;
case 'r':
	 ch = 't';
	break;
case 's':
	 ch = 'n';
	break;
case 't':
	 ch = 'w';
	break;
case 'u':
	 ch = 'j';
	break;
case 'v':
	 ch = 'p';
	break;
case 'w':
	 ch = 'f';
	break;
case 'x':
	 ch = 'm';
	break;
case 'y':
	 ch = 'a';
	break;
case 'z':
	 ch = 'q';
	break;

			}
			printf("%c",ch);
		}
		printf("\n");
	}
}