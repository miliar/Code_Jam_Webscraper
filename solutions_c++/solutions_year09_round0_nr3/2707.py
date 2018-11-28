#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFFSIZE 512

int main() {
	int compute(char *input, char *target);
	int i=1, ln;
	char *target, line[BUFFSIZE];

	FILE *in = fopen("C-small.in","r");

	fgets(line,BUFFSIZE,in);

	sscanf(line,"%d", &ln);

	target = strdup("welcome to code jam");
	
	for( i=0; i<ln; i++ ) {
		fgets(line,BUFFSIZE,in);
	    printf("Case #%d: %04d\n", i+1, compute(line, target)%10000);		
	}
	return 0;
}

int compute(char *input, char *target) {
	if( *target == '\0' ) {
		return 1;
	}
	if( *input == '\0' ) {
		return 0;
	}

	if( *input == *target ) {
		return compute(input+1, target+1)+compute(input+1, target);
	}else{
		return compute(input+1, target);
	}
}

