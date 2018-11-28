#include <stdio.h>

FILE *f_input, *f_output;

char g_google[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
char g_charArr[128];
void work();

int main(){
	int tmp;
	
	f_input = fopen("A-small-attempt1.in", "r");
	f_output = fopen("first.out", "w");

	fscanf(f_input, "%d\n", &tmp);

	for(int i=0; i<tmp; i++){
		fprintf(f_output, "Case #%d: ", i+1);
		work();
		fprintf(f_output, "\n");
	}

	fclose(f_input);
	fclose(f_output);
}

void work(){
	int iTmp=0;
	char cTmp;

	for(int i=0; i<128; i++) g_charArr[i] = '\0';

	fgets(g_charArr, 128, f_input);

	while(1){
		cTmp = g_charArr[iTmp++];
		
		if(cTmp == '\n') break;
		if(cTmp == ' '){
			fprintf(f_output, " ");
			continue;
		}
		fprintf(f_output, "%c", g_google[cTmp-97]);
	}
	
}