#include <cstdio>

using namespace std;

int main()
{
//	char table[26] = {'y'a,b'n',c'f',d'i',e'c',f'w',g'l',h'b',i'k',j'u',k'o',l'm',m'x',n's',o'e',p'v',q'z',r'p',s'd',t'r',u'j',v'g',w't',x'h',y'a',z'q'};	
	char table[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

	char str[102];

	int cases,i,j;

	scanf("%d\n",&cases);

	for(i=0;i<cases;i++)
	{
		printf("Case #%d: ",i+1);
		fgets(str,sizeof(str),stdin);
		for(j=0;str[j]!='\n' && str[j]!=0;j++)
		{
			if(str[j]==' ')
				printf(" ");
			else
				printf("%c",table[str[j]-'a']);
		}			
		printf("\n");
	}

	return 0;
}
