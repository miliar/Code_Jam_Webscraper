#include <stdio.h>
#include <string.h>
#define SET_SIZE 10000

int a[100][100];
int id[100][100];
int h,w;

int sbuff[SET_SIZE];
int rank[SET_SIZE];

void Link(int a,int b){
	if(rank[a]>rank[b])
		sbuff[b]=a;
	else if(rank[a]<rank[b])
		sbuff[a]=b;
	else{
		sbuff[a]=b;
		rank[b]++;
	}
}

void Make_Set(int x){
	sbuff[x] = x;
	rank[x] = 0;
}

void init(int n){
	for(int i=0;i<n;i++)
		Make_Set(i);
}



int Find_Root(int x){
	if(sbuff[x] != x)
		sbuff[x]=Find_Root(sbuff[x]);
	return sbuff[x];
}

void Union_Set(int sa, int sb){
	Link(Find_Root(sa),Find_Root(sb));
}

bool inb(int x,int y){
	if(x>=0 && x<h && y>=0 && y<w)
		return 1;
	return 0;
}

int dx[]={-1,0,0,1};
int dy[]={0,-1,1,0};
bool v[100][100];

void getac(int x,int y){
	v[x][y]=1;
	int h=a[x][y];
	int kk=-1;
	for(int k=0;k<4;k++){
		int nx=x+dx[k];
		int ny=y+dy[k];
		if(inb(nx,ny)){
			if(a[nx][ny]<h){
				h=a[nx][ny];
				kk=k;
			}
		}
	}
	if(kk!=-1){
		Union_Set(id[x][y],id[x+dx[kk]][y+dy[kk]]);
		getac(x+dx[kk], y+dy[kk]);
	}
}

//char ret[100][100];

char name[10000];

int main(){
	int T;
	scanf("%d\n", &T);
	for(int TT=1;TT<=T;TT++){
		scanf("%d%d",&h,&w);
		init(h*w);
		int cnt=0;
		for(int i=0;i<h;i++){
			for(int j=0;j<w;j++){
				scanf("%d",&a[i][j]);
				id[i][j]=cnt++;
			}
		}
		memset(v,0,sizeof(v));
		for(int i=0;i<h;i++){
			for(int j=0;j<w;j++){
				if(!v[i][j])
					getac(i,j);
			}
		}
		char cc='a';
		printf("Case #%d:\n",TT);
		memset(name,0,sizeof(name));
		for(int i=0;i<h;i++){
			for(int j=0;j<w;j++){
				int t = Find_Root(id[i][j]);
				if(name[t]==0){
					name[t]=cc++;
				}
				printf("%c ",name[t]);
				//ret[i][j]=name[t];
			}
			printf("\n");
		}
		
	}
}