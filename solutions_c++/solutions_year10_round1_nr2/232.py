#include<cstdio>

using namespace std;

int Del,Ins,Most,n;
int board[100];

int absol(int c){
	if(c<0) return -c;
	return c;
}

int process(){
	int dy[100][256] = {0,};
	int i,j,k;
	int MIN = 99999999;
	for(j=0;j<=255;j++){
		dy[0][j] = absol(j - board[0]);
	}
	for(i=1;i<n;i++){
		for(j=0;j<=255;j++){
			if(j==50){
				j = j;
			}
			dy[i][j] = dy[i-1][j] + Del;

			int temp = absol(j-board[i]);
			if(dy[i][j] > Del * i + temp){
				dy[i][j] = Del * i + temp;
			}
			int s, f;
			s = j - Most > 0 ? j - Most : 0;
			f = j + Most < 256 ? j + Most : 255;
			for(k=s;k<=f;k++){
				if(dy[i][j] > dy[i-1][k] + temp){
					dy[i][j] = dy[i-1][k] + temp;
				}
			}
			if(Most != 0){
				for(k=0;k<=255;k++){
					int addi = absol(j-k)/Most - 1 + (absol(j-k)%Most == 0 ? 0 : 1);
					if(addi < 0) continue;
					if(dy[i][j] > dy[i-1][k] + temp + Ins * addi){
						dy[i][j] = dy[i-1][k] + temp + Ins * addi;
					}
				}
			}
		}
	}
	for(i=0;i<=255;i++){
		if(dy[n-1][i] < MIN){
			MIN = dy[n-1][i];
		}
	}
	return MIN;
}

int main(void){
	int i,j,T;
	int ans;
	FILE *fin=fopen("input.txt","r");
	FILE *fout=fopen("output.txt","w");
	fscanf(fin,"%d",&T);
	for(i=1;i<=T;i++){
		fscanf(fin,"%d%d%d%d",&Del,&Ins,&Most,&n);
		for(j=0;j<n;j++){
			fscanf(fin,"%d",&board[j]);
		}
		ans = process();
		fprintf(fout,"Case #%d: %d\n",i,ans);
	}
	fcloseall();
	return 0;
}