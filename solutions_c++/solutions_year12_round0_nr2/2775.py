#include <stdio.h>
#include <stdlib.h>
int main(){
	char points[100];
	char answer;
	int j=1;
	FILE *fp,*fp2;
	fp=fopen("B-small-attempt1.in","r");
	fp2=fopen("answerB.out","w");
	char input[256];
	int num,sup,kijyun;
	int fuerukamo;
	fgets(input,256,fp);
	int count=atoi(input);
	while(fgets(input,256,fp) != NULL){
	answer=0,fuerukamo=0;
	sscanf(input,"%d %d %d %[^\n]",&num,&sup,&kijyun,input);
	for(int i=0;num>0;num--,i++){
		sscanf(input,"%d %[^\n]",&points[i],input);
		if(points[i]/3 >= kijyun) answer++;
		if(points[i]/3 == kijyun-1 && points[i]%3 > 0) answer++;
		if((points[i]/3 == kijyun-1 && points[i]%3 == 0 && points[i] >= kijyun) || (points[i]/3 == kijyun-2 && points[i]%3 == 2 && points[i] >= kijyun)) fuerukamo++;
	}
	answer += (fuerukamo < sup)? fuerukamo : sup; 
	fprintf(fp2,"Case #%d: %d\n",j,answer);
	j++;
	count--;
	if(count==0) break;
	}
	fclose(fp);
	fclose(fp2);
}