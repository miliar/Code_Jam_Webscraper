#include <iostream>
using namespace std;
const int size = 105;
const int maxInt = 50000;
FILE *in = fopen("B-large.in","r");
FILE *out = fopen("B-large.out","w");

int map[105][105];
int basin[105][105];
int ans[105][105];
int di[] = {-1,0,0,1};
int dj[] = {0,-1,1,0};
int sinkI,sinkJ;
int h,w,labelc;
bool visit[105][105];

void flows(int i,int j){
	//if(basin[i][j]!=0)return;
	int k,dir,maxAltitudes = map[i][j];
	int ni,nj;
	dir = -1;
	for(k = 0; k < 4; k++){
		ni = i+di[k];
		nj = j+dj[k];
		if(map[ni][nj]<maxAltitudes)
		{
			dir = k;
			maxAltitudes  = map[ni][nj];
		}
	}

	if(dir == -1){
		sinkI = i;
		sinkJ = j;
	}
	else
		flows(i+di[dir],j+dj[dir]);

	basin[i][j] = sinkI*w+sinkJ;
}

void label(int i,int j){
	int k;
	ans[i][j] = labelc;
	visit[i][j] = true;
	for(k = 0; k < 4; k++){
		int ni = i+di[k];
		int nj = j+dj[k];
		if(visit[ni][nj])continue;
		if(basin[i][j] == basin[ni][nj]){
			label(ni,nj);
		}
	}
}

void clasify(){
	int i,j;
	for(i = 1; i <= h; i++){
		for(j = 1; j <= w; j++)
		{
			if(basin[i][j]==0)
				flows(i,j);
		}
	}
// 	for(i = 1; i <= h; i++){
// 		for(j = 1; j <= h; j++)
// 		{
// 			fprintf(out,"%d ",basin[i][j]);
// 		}
// 		fprintf(out,"\n");
// 	}
	memset(visit,0,sizeof(visit));
	memset(ans,0,sizeof(ans));
	labelc = 'a';
	for(i = 1; i <= h; i++){
		for(j = 1; j <= w; j++)
		{
			if(!visit[i][j]){
				label(i,j);
				labelc++;
			}
		}
	}
	for(i = 1; i <= h; i++){
		for(j = 1;j <= w; j++)
			fprintf(out,"%c ",ans[i][j]);
		fprintf(out,"\n");
	}
}

int main(){
	int n,t,i,j;
	t = 0;
	fscanf(in,"%d",&n);
	while(n--){
		t++;
		memset(basin,0,sizeof(basin));
		memset(map,0,sizeof(map));
		fscanf(in,"%d %d",&h,&w);
		for(i = 0; i <= h+1; i++){
			map[i][0] = maxInt;
			map[i][w+1] = maxInt;
		}
		for(i = 0; i <= w+1; i++){
			map[0][i] = maxInt;
			map[h+1][i] = maxInt;
		}



		for(i = 1; i <= h; i++)
			for(j = 1; j <= w; j++)
				fscanf(in,"%d",&map[i][j]);

// 		for(i = 0; i <= h+1; i++){
// 			for(j = 0; j <= w+1; j++)
// 				fprintf(out,"%d ",map[i][j]);
// 			fprintf(out,"\n");
// 		}

		fprintf(out,"Case #%d:\n",t);
		clasify();

	}
	return 0;
}