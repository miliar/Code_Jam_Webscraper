#include<iostream>
#include<malloc.h>
using namespace std;
bool flag;
char preusedbasin;
bool markbasin(int **input,char **output,int row,int colum,char basin,int H,int W){
	if(output[row][colum]!='#'){
		preusedbasin=output[row][colum];
		flag=false;
		return false;
	}
	else{
		output[row][colum]=basin;
		int label=input[row][colum],new_row=row,new_colum=colum;
		if(row>0){
			if(input[row-1][colum]<label){
				label=input[row-1][colum];
				new_row=row-1, new_colum=colum;
			}
		}
		if(colum>0){
			if(input[row][colum-1]<label){
				label=input[row][colum-1];
				new_row=row, new_colum=colum-1;
			}
		}
		if(colum<W-1){
			if(input[row][colum+1]<label){
				label=input[row][colum+1];
				new_row=row, new_colum=colum+1;
			}
		}
		if(row<H-1){
			if(input[row+1][colum]<label){
				label=input[row+1][colum];
				new_row=row+1, new_colum=colum;
			}
		}
		if(new_row==row and new_colum==colum)
			return true;
		else{
			bool check=markbasin(input,output,new_row,new_colum,basin,H,W);
			if(not flag)
				output[row][colum]=preusedbasin;
			return check;
		}
	}
}
int main(){
	int T;
	scanf("%d",&T);
	for(int i=1;i<=T;i++){
		int H,W;
		scanf("%d%d",&H,&W);
		int **input;
		input=(int **)malloc(sizeof(int *)*H);
		char **output;
		output=(char **)malloc(sizeof(char *)*H);
		char basin='a';
		for(int j=0;j<H;j++){
			*(input+j)=(int *)malloc(sizeof(int)*W);
			*(output+j)=(char *)malloc(sizeof(char)*W);
			for(int k=0;k<W;k++){
				scanf("%d",&input[j][k]);
				output[j][k]='#';
			}
		}
		for(int j=0;j<H;j++){
			for(int k=0;k<W;k++){
				if(output[j][k]=='#'){
					flag=true;
					preusedbasin=basin;
					bool newbasin=markbasin(input,output,j,k,basin,H,W);
					if(newbasin)
						basin++;
				}
			}
		}
		printf("Case #%d:\n",i);
		for(int j=0;j<H;j++){
			for(int k=0;k<W;k++){
				printf("%c ",output[j][k]);
			}
			printf("\n");
		}
	}
	return 0;
}
