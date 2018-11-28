#include <stdio.h>
#include <string.h>

int main(){
	FILE *in = fopen("input.txt", "rt");
	FILE *out = fopen("output.txt", "wt");

	int t, i=1;
	fscanf(in, "%d", &t);
	char str[200];
	fgets(str, 200, in);
	while(t--){
		fgets(str, 200, in);
		fprintf(out, "Case #%d: ", i++);
		for(int i=0; i<strlen(str); i++){
			if(str[i]=='a') fprintf(out, "y");
			else if(str[i]=='b') fprintf(out, "h");
			else if(str[i]=='c') fprintf(out, "e");
			else if(str[i]=='d') fprintf(out, "s");
			else if(str[i]=='e') fprintf(out, "o");
			
			else if(str[i]=='f') fprintf(out, "c");
			else if(str[i]=='g') fprintf(out, "v");
			else if(str[i]=='h') fprintf(out, "x");
			else if(str[i]=='i') fprintf(out, "d");
			else if(str[i]=='j') fprintf(out, "u");
			else if(str[i]=='k') fprintf(out, "i");
			else if(str[i]=='l') fprintf(out, "g");
			else if(str[i]=='m') fprintf(out, "l");
			else if(str[i]=='n') fprintf(out, "b");
			else if(str[i]=='o') fprintf(out, "k");
			else if(str[i]=='p') fprintf(out, "r");

			else if(str[i]=='q') fprintf(out, "z");
			else if(str[i]=='r') fprintf(out, "t");
			else if(str[i]=='s') fprintf(out, "n");
			else if(str[i]=='t') fprintf(out, "w");
			else if(str[i]=='u') fprintf(out, "j");
			else if(str[i]=='v') fprintf(out, "p");
			else if(str[i]=='w') fprintf(out, "f");
			else if(str[i]=='x') fprintf(out, "m");
			else if(str[i]=='y') fprintf(out, "a");
			else if(str[i]=='z') fprintf(out, "q");
			else fprintf(out, "%c", str[i]);
		}
		fprintf(out, "\n");
	}
	return 0;
}
