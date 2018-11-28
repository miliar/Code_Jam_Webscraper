#include <stdio.h>
FILE * in = fopen("input.txt","r");
FILE * out = fopen("output.txt","w");
int T,H,W;
int arr[105][105];
int label[105][105],label_cnt,current_label;
int wx[4]={0,-1,1,0},wy[4]={-1,0,0,1};

void bt(int y, int x){
	int i,X,Y,ind=-1,min=9999;
	if (label[y][x]!=0){
		current_label=label[y][x];
		return;
	}	
	for(i=0;i<4;i++){
		X=x+wx[i];
		Y=y+wy[i];
		if (1<=X && X<=W && 1<=Y && Y<=H){
			if (arr[Y][X]<arr[y][x] && arr[Y][X]<min){
				ind=i;
				min=arr[Y][X];
			}
		}
	}
	if (ind!=-1) {
		bt(y+wy[ind],x+wx[ind]);
		label[y][x]=current_label;
	}
	else{
		current_label=label_cnt++;
		label[y][x]=current_label;
		return;
	}
}
int main(){
	int i,j,k;
	
	fscanf(in,"%d",&T);
	
	for(k=0;k<T;k++){
		fscanf(in,"%d %d",&H,&W);
		for(i=1;i<=H;i++){
			for(j=1;j<=W;j++){
				fscanf(in,"%d",&arr[i][j]);
				label[i][j]=0;
			}
		}
		label_cnt=1;
		for(i=1;i<=H;i++){
			for(j=1;j<=W;j++){
				if (label[i][j]==0){
					bt(i,j);
				}
			}
		}
		fprintf(out,"Case #%d:\n",k+1);

		for(i=1;i<=H;i++){
			for(j=1;j<=W;j++){
				fprintf(out,"%c ",label[i][j]+'a'-1);
			}
			fprintf(out,"\n");
		}		
	}

	return 0;
}