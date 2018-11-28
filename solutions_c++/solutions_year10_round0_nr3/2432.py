
#include<stdio.h>
#include<stdlib.h>
void main(){
	int d,i,j,n,r,count,flag,point,people;
	long total;
	int num[1005];
	FILE *fin=fopen("C.in","r");
	FILE *fout=fopen("C.out","w");
	fscanf(fin,"%d\n",&count);
	for(i=1;i<=count;i++){
		point=0;
		total=0;
		fscanf(fin,"%d %d %d\n",&r,&d,&n);
		for(j=0;j<n;j++)
			fscanf(fin,"%d",&num[j]);
		for(j=0;j<r;j++){
			flag=0;
			people=d;
			while(true){
				if(num[point]>people||flag>=n)
					break;
				people-=num[point];
				total+=num[point];
				point=(point+1)%n;
				flag++;
			}
		}
		fprintf(fout,"Case #%d: %ld\n",i,total);
	}
	fclose(fin);
	fclose(fout);
	exit(0);
}