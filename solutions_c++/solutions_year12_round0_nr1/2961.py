#include <stdio.h>


int main(){
int cases;
char g[110],c;
int i,j,k;
FILE *input;
FILE *output;
input = fopen("A-small-attempt0.in","r");
output = fopen("output1.txt", "w");
fscanf(input, "%d", &cases);
c=fgetc(input);
for(i=0;i<cases;i++){
	j=0;
	while((c=fgetc(input))!='\n'){
		g[j]=c;
		j++;
	}
	g[j]='\0';
	for(k=0;k<j;k++){
		switch(g[k]){
			case 'a': g[k]='y';break;
			case 'b': g[k]='h';break;
			case 'c': g[k]='e';break;
			case 'd': g[k]='s';break;
			case 'e': g[k]='o';break;
			case 'f': g[k]='c';break;
			case 'g': g[k]='v';break;
			case 'h': g[k]='x';break;
			case 'i': g[k]='d';break;
			case 'j': g[k]='u';break;
			case 'k': g[k]='i';break;
			case 'l': g[k]='g';break;
			case 'm': g[k]='l';break;
			case 'n': g[k]='b';break;
			case 'o': g[k]='k';break;
			case 'p': g[k]='r';break;
			case 'q': g[k]='z';break;
			case 'r': g[k]='t';break;
			case 's': g[k]='n';break;
			case 't': g[k]='w';break;
			case 'u': g[k]='j';break;
			case 'v': g[k]='p';break;
			case 'w': g[k]='f';break;
			case 'x': g[k]='m';break;
			case 'y': g[k]='a';break;
			case 'z': g[k]='q';break;
			case ' ': g[k]=' ';break;
		}
	}
	fprintf(output,"Case #%d: %s\n",i+1, g);
}
fclose(input);
fclose(output);

	return 0;
}