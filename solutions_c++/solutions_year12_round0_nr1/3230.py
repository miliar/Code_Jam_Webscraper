//By Lin
#include<cstdio>
#include<cstring>

using namespace std; 

char 	change[27] ="yhesocvxduiglbkrztnwjpfmaq" ;
char s[1000000]; 
int		main()
{
	int cas,tt = 0; 
	scanf("%d", &cas ); 
	gets(s);
	while ( cas -- ) 
	{
		printf("Case #%d: ", ++ tt ); 
		gets(s);
		for (int i = 0; s[i]; i++)
			if ( s[i]>='a' && s[i] <='z' ) 	
				printf("%c", change[s[i]-'a'] ); 
			else printf("%c",s[i]); 
		printf("\n"); 
	}
	return 0; 
}
