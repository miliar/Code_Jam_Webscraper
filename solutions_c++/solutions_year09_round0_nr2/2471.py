#include <iostream>
#include <string>
using namespace std;

const int DIR_LEN=4;
const int DX[]={-1,0,0,1};
const int DY[]={0,-1,1,0};

const int N=10000;
int pr[N];
int rank[N];

int Find(int x){
	if(x==pr[x]){
		return x;
	}
	return pr[x]=Find(pr[x]);
}

void Merge(int x,int y){
	int px=pr[x];
	int py=pr[y];
	if(px!=py){
		if(rank[px]>rank[py]){
			pr[py]=px;
		}else{
			pr[px]=py;
			if(rank[px]==rank[py]){
				++rank[py];
			}
		}	
	}
	return;
}


int T;
int H,W;

char id[N];
int a[100][100];

bool Input(){
	scanf("%d%d",&H,&W);
	int i,j;
	for(i=0;i<H;++i){
		for(j=0;j<W;++j){
			scanf("%d",&a[i][j]);
		}
	}
    return 1;
}

void Solve(int caseNum){
	int i,j,k;
	
	for(i=0;i<W*H;++i){
		pr[i]=i;
		rank[i]=0;
	}

	for(i=0;i<H;++i){
		for(j=0;j<W;++j){
			for(k=0;k<DIR_LEN;++k){
				int tx=i,ty=j;
				for(k=0;k<DIR_LEN;++k){
					int x=i+DX[k];
					int y=j+DY[k];
					if(x>=0&&x<H&&y>=0&&y<W&&a[x][y]<a[tx][ty]){
						tx=x,ty=y;
					}
				}
				Merge(i*W+j,tx*W+ty);
			}
		}
	}

	printf("Case #%d:\n",caseNum);
	memset(id,0,sizeof(id));
	char c='a';
	for(i=0;i<H;++i){
		for(j=0;j<W;++j){
			int p=Find(i*W+j);
			if(!id[p]){
				id[p]=c++;
			}
			if(j>0){
				printf(" ");
			}
			printf("%c",id[p]);
		}
		printf("\n");
	}
    return;
}

int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&T);
	int i;
	for(i=1;i<=T;++i){
		Input();
		Solve(i);
	}
    return 0;
}
