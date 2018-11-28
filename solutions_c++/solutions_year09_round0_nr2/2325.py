
#include <cstdio>
#include <fstream>

#define H 105
#define W 105
using namespace std;


FILE *in=fopen("input.txt","r");
FILE *out=fopen("output.txt","w");

int n,h,w,cnt;
int data[H][W],ans[H][W],mint[H][W];
int dir[5][2]={0,0,-1,0,0,-1,0,1,1,0};

void dfs(int y,int x){
	int i,j,k,yy,xx;
	ans[y][x]=cnt;
	for(i=1;i<=4;i++){
		yy=y+dir[i][0];
		xx=x+dir[i][1];
		if (yy<0 || yy>=h) continue;
		if (xx<0 || xx>=w) continue;
		if (ans[yy][xx]!=0) continue;
		if (mint[y][x]==i || mint[yy][xx]+i==5) dfs(yy,xx);
	}
}

int main(){
	int i,j,k;
	fscanf(in,"%d",&n);
	for(int tc=1;tc<=n;tc++){
		cnt=0;
		memset(ans,0,sizeof(ans));
		memset(mint,0,sizeof(mint));
		fscanf(in,"%d %d",&h,&w);
		for(i=0;i<h;i++)
			for(j=0;j<w;j++)
				fscanf(in,"%d",&data[i][j]);
		for(i=0;i<h;i++)
			for(j=0;j<w;j++){
				int minn=data[i][j];
				for(k=1;k<=4;k++){
					int ii=i+dir[k][0];
					int jj=j+dir[k][1];
					if (ii<0 || ii>=h) continue;
					if (jj<0 || jj>=w) continue;
					if (minn>data[ii][jj]){
						minn=data[ii][jj];
						mint[i][j]=k;
					}
				}
			}
		for(i=0;i<h;i++)
			for(j=0;j<w;j++)
				if (ans[i][j]==0){
					cnt++;
					dfs(i,j);
				}
		fprintf(out,"Case #%d:\n",tc);
		for(i=0;i<h;i++){
			for(j=0;j<w;j++)
				fprintf(out,"%c ",'a'+ans[i][j]-1);
			fprintf(out,"\n");
		}
	}
	return 0;
}