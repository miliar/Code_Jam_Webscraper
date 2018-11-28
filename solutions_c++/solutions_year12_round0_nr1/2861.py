#include <stdio.h>

void main()
{
	FILE *in, *out;
	int i, N, length;
	char str[200];
	char decode[] = "yhesocvxduiglbkrztnwjpfmaq";

	in = fopen("A-small-attempt0.in","r");
	out = fopen("A-small-attempt0.out","w");

	fscanf(in, "%d", &N);
	
	for( i=0; i<N; i++) {
	
		length = 0;
		while(1) {

			str[length] = fgetc(in);

			if( str[length] == '\n' && length == 0 )
				continue;
			
			if( str[length] == '\n' || str[length] == EOF) {
				str[length++] = NULL;
				break;
			}

			if( str[length] != ' ')
				str[length] = decode[str[length]-'a'];

			length++;
		}
		
		fprintf(out,"Case #%d: %s\n",i+1,str);
	}
}