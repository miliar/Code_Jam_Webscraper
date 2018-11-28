#include <cstdio>
#include <map>
using namespace std;

int region[101][101];
int mark[101][101];
int rows,cols;

void floodfill(int row,int col,int value){
	mark[row][col]=value;
	int neighborRow,neighborCol;
	int min=region[row][col];
	if(row>0 && region[row-1][col]<min){
		neighborRow = row-1;
		neighborCol = col;
		min = region[row-1][col];
	}
	if(col>0 && region[row][col-1]<min){
		neighborRow = row;
		neighborCol = col-1;
		min = region[row][col-1];
	}
	if(col<cols-1 && region[row][col+1]<min){
		neighborRow = row;
		neighborCol = col+1;
		min = region[row][col+1];
	}
	if(row<rows-1 && region[row+1][col]<min){
		neighborRow = row+1;
		neighborCol = col;
		min = region[row+1][col];
	}
	
	if(min==region[row][col]){
		// sink
		return;
	}
	if(mark[neighborRow][neighborCol]!=0){
		int tmp = mark[neighborRow][neighborCol];
		for(int i=0;i<rows;i++)
			for(int j=0;j<cols;j++)
				if(mark[i][j]==tmp)
					mark[i][j]=value;
		return;
	}else{
		return floodfill(neighborRow,neighborCol,value);
	}
}

int main(){
	int n;

	scanf("%d",&n);
	for(int i=1;i<=n;i++){
		scanf("%d %d",&rows,&cols);
		for(int j=0;j<rows;j++)
			for(int k=0;k<cols;k++){
				scanf("%d",&region[j][k]);
				mark[j][k]=0;
			}
		for(int j=0;j<rows;j++)
			for(int k=0;k<cols;k++)
				if(mark[j][k]==0)
					floodfill(j,k,j*cols+k+1);
		map<int,char> labels;
		int label = 0;
		for(int j=0;j<rows;j++)
			for(int k=0;k<cols;k++)
				if(labels.find(mark[j][k])==labels.end())
					labels[mark[j][k]]=label++;
		printf("Case #%d:\n",i);
		for(int j=0;j<rows;j++){
			for(int k=0;k<cols;k++){
				if(k!=0)
					printf(" ");
				printf("%c",'a'+labels[mark[j][k]]);
			}
			printf("\n");
		}
	}
}
