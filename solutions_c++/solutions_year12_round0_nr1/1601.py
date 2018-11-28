#include<stdio.h>

int T, Tcount;
FILE *fin, *fout;
char ch[101];

char map[31] = {'y', 'h', 'e', 's', 'o', 'c',  'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
char ch2[101];
void input();
void process();
void output();

void main(){
	fin = fopen("input.txt", "r");
	fout=  fopen("output.txt", "w");
	fscanf(fin,"%d\n", &T);
	for(Tcount = 1; Tcount <=T;Tcount++){
		input();
		process();
		output();
	}
	fclose(fin);
	fclose(fout);
}

void input(){
	int i = 0;
	while((ch[i]= fgetc(fin))!= '\n') i++;
}

void process(){
	int i;
	for(i=0;ch[i]!='\n';i++){
		if(ch[i] == ' ') ch2[i] = ' ';
		else if(ch[i] == '\n') ch2[i] = '\n';
		else ch2[i] = map[ch[i]-'a'];
	}
	ch2[i] = '\0';
}

void output(){
	fprintf(fout, "Case #%d: %s\n",Tcount,
		ch2);
}