#include <stdio.h>
#include <string.h>
#include <map>
#include <set>
using namespace std;
int H[100][100];
int label[100][100];
int R, C;
#define inside(r,c) (((0<=(r)) && ((r)<R)) && ((0<=(c)) && ((c)<C)))

int dRow[4]={-1,0,0,1};
int dCol[4]={0,-1,1,0};

int getBasin(int r, int c, int &lab){
	if(label[r][c]>=0){
		return label[r][c];
	}
	int sel=-1;
	int minSel=H[r][c];
	for(int k=0;k<4;++k){
		int rr=r+dRow[k];
		int cc=c+dCol[k];
		if(inside(rr,cc) && H[rr][cc]<minSel){
			sel=k;
			minSel=H[rr][cc];
		}
	}
	if(sel==-1){
		label[r][c]=lab;
		++lab;
		return label[r][c];
	}
	int rr=r+dRow[sel];
	int cc=c+dCol[sel];
	return getBasin(rr,cc,lab);
}

int main(int argc, char *argv[]){
	int N;
	scanf("%d", &N);
	for(int caseNum=1;caseNum<=N;++caseNum){
		scanf("%d%d", &R, &C);
		for(int i=0;i<R;++i)
			for(int j=0;j<C;++j){
				scanf("%d", &H[i][j]);
			}
		memset(label, -1, sizeof(label));
		int currentLetter='a';
		for(int i=0;i<R;++i)
			for(int j=0;j<C;++j)
				if(label[i][j]==-1)
					label[i][j]=getBasin(i,j,currentLetter);
		printf("Case #%d:\n", caseNum);
		for(int i=0;i<R;++i){
			for(int j=0;j<C;++j){
				printf("%c", label[i][j]);
				if(j<C-1){
					printf(" ");
				}else{
					printf("\n");
				}
			}
		}
	}
	return 0;	   
}
