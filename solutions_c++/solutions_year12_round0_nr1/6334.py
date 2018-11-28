#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	char Googlerese[120];
	char GooglereseTranslate[120];
	char c;
	char mapping[26] = {
		'y', 'h', 'e', 's', 'o', 'c',
		'v', 'x', 'd', 'u', 'i', 'g', 
		'l', 'b', 'k', 'r', 'z', 't', 
		'n', 'w', 'j', 'p', 'f', 'm', 
		'a', 'q'};

	int T, N, i, j, k, d, n, len;
	bool isBreak = false;

	scanf(" %d", &T);
	fgets( Googlerese, 120, stdin );
	for(i=0 ; i<T ; i++)
	{
		fgets( Googlerese, 120, stdin );
		
		for(k=0 ; k < strlen(Googlerese) - 1 ; k++)
		{
			if(Googlerese[k] != ' ')
				GooglereseTranslate[k] = mapping[Googlerese[k]-'a'];
			else
				GooglereseTranslate[k] = Googlerese[k];
		}
		
		printf("Case #%d: ", i+1);
		for(k=0 ; k < strlen(Googlerese) - 1 ; k++)
		{
			printf("%c", GooglereseTranslate[k]);
		}
		printf("\n");
	}
	return 0;
}