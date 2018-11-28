#include<cstdio>
#include<cstring>

#include<map>
#include<algorithm>

#define inb(a,b) (a>=0 && a<h && b>=0 && b<w)

using namespace std;

int dx[4] = {-1, 0, 0, 1};
int dy[4] = {0, -1, 1, 0};

int m[200][200], px[200][200], py[200][200],pc[200][200];

int h,w;

int utp(int i, int j){
	int ti = i;
	int tj = j;
	while(px[ti][tj]!=ti || py[ti][tj]!=tj){
		//printf(" eee %d %d\n",px[ti][tj],py[ti][tj]);
		int ttx = px[ti][tj];
		tj = py[ti][tj];
		ti = ttx;
		//printf(" fff %d %d\n",ti,tj);
	}
	int tti = ti;
	int ttj = tj;
	ti = i;
	tj = j;
	while(px[ti][tj]!=ti || py[ti][tj]!=tj){
		//printf(" cpress (%d,%d)->(%d,%d)\n",ti,tj,tti,ttj);
		int ttx = px[ti][tj];
		int tty = py[ti][tj];
		px[ti][tj]=tti;
		py[ti][tj]=ttj;
		ti = ttx;
		tj = tty;
		//printf(" cpreee (%d,%d)->(%d,%d)\n",ti,tj,tti,ttj);
	}
	return 0;
}

int unio(int i1, int j1, int i2, int j2){
	utp(i2,j2);
	utp(i1,j1);
	if(px[i2][j2]!=px[i1][j1] || py[i2][j2]!=py[i1][j1]){
		/*
		printf("indi (%d,%d) - (%d,%d)\n",i1,j1,i2,j2);
		printf("cxe (%d,%d) -> (%d,%d)\n",px[i2][j2],py[i2][j2],i1,j1);
			for(int a=0;a<h;a++){
				for(int b=0;b<w;b++)printf("   (%d,%d)",px[a][b],py[a][b]);
				printf("\n");
			}*/
		int ppx = px[i2][j2];
		int ppy = py[i2][j2];
		px[ppx][ppy] = i1;
		py[ppx][ppy] = j1;
		utp(i2,j2);
		//printf("para (%d,%d))\n",px[i2][j2],py[i2][j2]);
	}
	return 0;
}

int main(){
	int nn;
	scanf("%d",&nn);
	for(int ii=1;ii<=nn;ii++){
		scanf("%d%d",&h,&w);
		for(int i=0;i<h;i++)for(int j=0;j<w;j++){
			scanf("%d",&m[i][j]);
			px[i][j]=i;
			py[i][j]=j;
		}
		int nc=0;
		for(int i=0;i<h;i++)for(int j=0;j<w;j++){
			int me = m[i][j];
			int kk = -1;
			for(int k=0;k<4;k++){
				if(inb(i+dx[k],j+dy[k])){
					if(m[i+dx[k]][j+dy[k]]< me){
						me = m[i+dx[k]][j+dy[k]];
						kk = k;
					}
				}
			}
			//printf(" r %d\n",kk);
			if(kk>=0)unio(i+dx[kk],j+dy[kk],i,j);
			/*for(int a=0;a<h;a++){
				for(int b=0;b<w;b++)printf("   (%d,%d)",px[a][b],py[a][b]);
				printf("\n");
			}*/
		}
		memset(pc,0,sizeof(pc));
		printf("Case #%d:\n", ii);
		for(int i=0;i<h;i++){
			for(int j=0;j<w;j++){
			utp(i,j);
		}
	}
		for(int i=0;i<h;i++){
			for(int j=0;j<w;j++){
			
			if(pc[px[i][j]][py[i][j]]==0){
				pc[px[i][j]][py[i][j]] = ++nc;
			}
			//printf("(%d,%d)",px[i][j],py[i][j]);
			printf("%s%c",j?" ":"",pc[px[i][j]][py[i][j]]+'a'-1);
		}
		printf("\n");
		}
	}
		
	return 0;
}
