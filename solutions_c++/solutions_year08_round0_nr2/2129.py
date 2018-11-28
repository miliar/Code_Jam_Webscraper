#include<stdio.h>
#include<assert.h>
#include<stdlib.h>

void main()
{

int i,test,j,k;
int delay;
int ab;
int ba;
int a,b,c,d;
int tota=0,ata=0,totb=0,atb=0;
struct ti{
int tim;
int type;};
typedef ti time;
time * times,temp;

FILE * fp;
FILE * fp2;
fp=fopen("Bsmall.in","r");
fp2=fopen("Bsmall2.txt","w");
assert(fp!=NULL);
assert(fp2!=NULL);

fscanf(fp,"%d",&test); //input of number of test values is made

for( i=0 ; i<test ; i++ ){  //Number of test values-iteration

	fscanf(fp,"%d",&delay);
	fscanf(fp,"%d%d",&ab,&ba);

	times =(time*)malloc((ab+ab+ba+ba)*sizeof(time));

	for(j=0;j<ab*2;j+=2){
	fscanf(fp,"%d:%d%d:%d",&a,&b,&c,&d);
	times[j].tim=100*a+b;
	times[j].type=0;
	times[j+1].tim=100*c+d+delay;
	times[j+1].type=1;}

	for(j=ab*2;j<(ab+ba)*2;j+=2){
	fscanf(fp,"%d:%d%d:%d",&a,&b,&c,&d);
	times[j].tim=100*a+b;
	times[j].type=2;
	times[j+1].tim=100*c+d+delay;
	times[j+1].type=3;}

	for(j=1;j<ab+ba+ab+ba;j++){
		for(k=j;k>0;k--){
			if((times[k].tim < times[k-1].tim)||((times[k].tim==times[k-1].tim)&&((times[k].type==1)||(times[k].type==3)))){
				temp=times[k];
				times[k]=times[k-1];
				times[k-1]=temp;}}}

tota=ata=totb=atb=0;
           printf("%d\n",i+1);
	 for(j=0;j<ab+ba+ab+ba;j++){
	 printf("\n%d %d",times[j].tim,times[j].type);
			 switch (times[j].type){
		 case 0:
				 if(ata==0){
				 tota+=1;
				 printf(" train spawned at A");}
				 else{
				 ata-=1;
				 printf(" train sent to B");}
				 break;
		 case 1:
				 atb+=1;
				 printf(" train came to B");
				 break;
		 case 2:
				 if(atb==0){
				 totb+=1;
				 printf(" train spawned and sent at B");}
				 else{
				 printf(" train sent to A");
				 atb-=1;}
				 break;
		 case 3:
				 ata+=1;
             printf("train came to A");
				 break;
		 default :printf("here");}}

	 fprintf(fp2,"Case #%d: %d %d\n",i+1,tota,totb);
    printf("Case #%d: %d %d\n",i+1,tota,totb);
}
printf("woohoo!");
}
