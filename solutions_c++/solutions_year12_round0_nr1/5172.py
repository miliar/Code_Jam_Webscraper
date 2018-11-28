#include <stdio.h>

char *conv = "yhesocvxduiglbkrztnwjpfmaq";
int main(int argc, char* argv[])
{
	int N;
	scanf("%d",&N);
	char ch[1025];
	gets(ch);
	for(int I=0; I<N; ++I)
	{
		gets(ch);
		for(char* p=ch; *p; ++p)
		{
			if( *p>='a' && *p<='z' )
			{
				*p = conv[*p-'a'];
			}
		}
		printf("Case #%d: %s\n", I+1, ch);
	}
	return 0;
}


