#include "stdio.h"
#include "string.h"

char Googlerese(char word);


int main(void){
	char t[4];
	char g[30][102];
	int i;
	int j;
	int n;
	FILE *fp;

	fp=fopen("A-small-attempt2.in","r");
	
	fgets(t, 4, fp); 
	sscanf(t,"%d",&n);

	for(i=0;i<n;i++){
		fgets(g[i], 102, fp); 
	}
	
	fclose(fp);

	for(i=0;i<n;i++){
		for(j=0;j<102;j++){
			g[i][j]=Googlerese(g[i][j]);
		}
	}
	
	for(i=0;i<n;i++){
		printf("Case #%d: %s",i+1,g[i]);
	}

	fp=fopen("result.txt","w");
	for(i=0;i<n;i++){
		fprintf(fp,"Case #%d: %s",i+1,g[i]);
	}
	fclose(fp);

	return 0;
}

char Googlerese(char word){
	if(word=='a'){
		return 'y';
	}else if(word=='b'){
		return 'h';
	}else if(word=='c'){
		return 'e';
	}else if(word=='d'){
		return 's';
	}else if(word=='e'){
		return 'o';
	}else if(word=='f'){
		return 'c';
	}else if(word=='g'){
		return 'v';
	}else if(word=='h'){
		return 'x';
	}else if(word=='i'){
		return 'd';
	}else if(word=='j'){
		return 'u';
	}else if(word=='k'){
		return 'i';
	}else if(word=='l'){
		return 'g';
	}else if(word=='m'){
		return 'l';
	}else if(word=='n'){
		return 'b';
	}else if(word=='o'){
		return 'k';
	}else if(word=='p'){
		return 'r';
	}else if(word=='q'){
		return 'z';
	}else if(word=='r'){
		return 't';
	}else if(word=='s'){
		return 'n';
	}else if(word=='t'){
		return 'w';
	}else if(word=='u'){
		return 'j';
	}else if(word=='v'){
		return 'p';
	}else if(word=='w'){
		return 'f';
	}else if(word=='x'){
		return 'm';
	}else if(word=='y'){
		return 'a';
	}else if(word=='z'){
		return 'q';
	}else{
		return word;
	}
}