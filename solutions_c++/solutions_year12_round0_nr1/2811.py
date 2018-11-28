#include <stdio.h>
FILE *inFile;
FILE *outFile;
char inputFile[] = "input.txt";
char outputFile[] = "output.txt";
int test = 0;
char convert(char c){
	if(c=='a') return 'y';
	if(c=='b') return 'h';
	if(c=='c') return 'e';
	if(c=='d') return 's';
	if(c=='e') return 'o';
	if(c=='f') return 'c';
	if(c=='g') return 'v';
	if(c=='h') return 'x';
	if(c=='i') return 'd';
	if(c=='j') return 'u';
	if(c=='k') return 'i';
	if(c=='l') return 'g';
	if(c=='m') return 'l';
	if(c=='n') return 'b';
	if(c=='o') return 'k';
	if(c=='p') return 'r';
	if(c=='q') return 'z';
	if(c=='r') return 't';
	if(c=='s') return 'n';
	if(c=='t') return 'w';
	if(c=='u') return 'j';
	if(c=='v') return 'p';
	if(c=='w') return 'f';
	if(c=='x') return 'm';
	if(c=='y') return 'a';
	if(c=='z') return 'q';
	if(c==' ') return ' ';
	if(c=='\n') return '\n';
}
int main(void) {
	char c = '\0';
	inFile = fopen(inputFile,"r");
	outFile = fopen(outputFile,"w");
	fscanf(inFile,"%d",&test);
	fscanf(inFile,"%c",&c);
	for(int i=1;i<=test;i++) {
		fprintf(outFile,"Case #%d: ",i);
		do{
			fscanf(inFile,"%c",&c);
			fprintf(outFile,"%c",convert(c));
		}while(c!='\n');
	}
	fclose(inFile);
	fclose(outFile);
	return 0;
}