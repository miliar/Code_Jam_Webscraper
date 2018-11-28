#include<iostream>
using namespace std;

long map[101][101];
long dat[10001][2];
long pos[101][101];
char chr[101][101];

void swap(long i,long j){
	long k;
	k=dat[i][0];dat[i][0]=dat[j][0];dat[j][0]=k;
	k=dat[i][1];dat[i][1]=dat[j][1];dat[j][1]=k;
}

void P(long p,long r){
	if(p<r){
		long i=p,j=r+1;
		swap(p,(p+r)/2);
		while(1){
			while(dat[++i][0]<dat[p][0]);
			while(dat[--j][0]>dat[p][0]);
			if(i>=j)break;
			swap(i,j);
		}
		swap(p,j);
		P(p,j-1);
		P(j+1,r);
	}
}

long h,t,w;

void bfs1(long j,long k){
	if(j>1 && pos[j-1][k]==0 && map[j][k]<map[j-1][k] && (k==w ||map[j][k]<map[j-1][k+1])&& (k==1 ||map[j][k]<map[j-1][k-1])&&(j==2 || map[j][k]<map[j-2][k])){
		pos[j-1][k]=pos[j][k];
		bfs1(j-1,k);
	}
	if(k>1 && pos[j][k-1]==0 && map[j][k]<map[j][k-1] && (k==2 ||map[j][k]<map[j][k-2]) &&(j==1||map[j][k]<map[j-1][k-1])&&(j==t||map[j][k]<=map[j+1][k-1])){
		pos[j][k-1]=pos[j][k];
		bfs1(j,k-1);
	}
	if(k<w && pos[j][k+1]==0 && map[j][k]<map[j][k+1] && (j==1||map[j][k]<map[j-1][k+1])&&(k==w-1||map[j][k]<=map[j][k+2])&&(j==t||map[j][k]<=map[j+1][k+1])){
		pos[j][k+1]=pos[j][k];
		bfs1(j,k+1);
	}
	if(j<t && pos[j+1][k]==0 && map[j][k]<map[j+1][k] && (j==t-1||map[j][k]<=map[j+2][k])&&(k==1||map[j][k]<=map[j+1][k-1])&&(k==w||map[j][k]<=map[j+1][k+1])){
		pos[j+1][k]=pos[j][k];
		bfs1(j+1,k);
	}
}

void bfs2(long j,long k){
	if(j>1 && chr[j-1][k]==0 &&pos[j-1][k]==pos[j][k]){
		chr[j-1][k]=chr[j][k];
		bfs2(j-1,k);
	}
	if(k>1 && chr[j][k-1]==0 && pos[j][k-1]==pos[j][k]){
		chr[j][k-1]=chr[j][k];
		bfs2(j,k-1);
	}
	if(k<w && chr[j][k+1]==0 && pos[j][k+1]==pos[j][k]){
		chr[j][k+1]=chr[j][k];
		bfs2(j,k+1);
	}
	if(j<t && chr[j+1][k]==0 && pos[j+1][k]==pos[j][k]){
		chr[j+1][k]=chr[j][k];
		bfs2(j+1,k);
	}
}

int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	long i,j,k,z=1;
	scanf("%ld",&h);
	for(z=1;z<=h;z++){
		memset(map,0,sizeof(map));
		memset(dat,0,sizeof(dat));
		memset(pos,0,sizeof(pos));
		memset(chr,0,sizeof(chr));
		scanf("%ld%ld",&t,&w);
		for(i=1;i<=t;i++)
			for(j=1;j<=w;j++){
				scanf("%ld",&map[i][j]);
				dat[(i-1)*w+j][0]=map[i][j];
				dat[(i-1)*w+j][1]=(i-1)*w+j;
			}
		P(1,t*w);
		for(i=1;i<=t*w;i++){
			if(dat[i][1]%w==0){
				j=dat[i][1]/w;k=w;
			}else{
				j=dat[i][1]/w+1;k=dat[i][1]%w;
			}
			if(pos[j][k]==0){
				pos[j][k]=i;
				bfs1(j,k);
			}
		}
		k='a';
		for(i=1;i<=t;i++)
			for(j=1;j<=w;j++){
				if(chr[i][j]==0){
					chr[i][j]=k;
					bfs2(i,j);
					k++;
				}
			}
		printf("Case #%ld:\n",z);
		for(i=1;i<=t;i++)
			for(j=1;j<=w;j++){
				putchar(chr[i][j]);
				if(j==w)putchar('\n');
				else putchar(' ');
			}
	}
	return 0;
}