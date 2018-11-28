#include<stdio.h>
#include<stdlib.h>
#include<string.h>	

int main(){
	FILE *fp=fopen("input.txt","r");
	FILE *fo=fopen("output.txt","w");
	int T,N;
	char data[200],trans[27]="yhesocvxduiglbkrztnwjpfmaq";
	fscanf(fp,"%d\n",&T);
	for(int casen = 1 ; casen <= T ;casen++ ){
		fgets(data,200,fp);
		int strn = strlen(data);
		for(int i=0;i<strn;i++){
			if(data[i]>='a'&&data[i]<='z'){
				data[i]=trans[data[i]-'a'];
				}
		}
		fprintf(fo,"Case #%d: %s",casen,data);
		
	}
	

}

