#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
#define M 100
#define MAX 100000
int sou[M+10][M+10];
int used[M+5][M+5];
int mid[M+100][M+100];
char id[M+5][M+5];
int rank[M*M+100];
int pre[M*M+100];
int h,w;
int coor[4][2]={{-1,0},{0,-1},{0,1},{1,0}};
int ch='a';
int cnt;
int len;

int make_set(){
	int i;
	for(i=0;i<h*w;i++){
		rank[i]=0;
		pre[i]=i;
	}
	return 0;
}

int find_set(int d){
	if(pre[d]==d) return d;
	else pre[d]=find_set(pre[d]);
	return pre[d];
}

int union_set(int a,int b){
	int c=find_set(a);
	int d=find_set(b);
	if(rank[c]>=rank[d]){
		pre[d]=c;
		if(rank[c]==rank[d])
			rank[c]++;
	}
	else pre[c]=d;
	return 0;
}

int solve(){
	make_set();
	int i,j,k,p;
	len=0;
	for(i=0;i<h;i++){
		for(j=0;j<w;j++){
			int mmin=sou[i][j];
			int u;
			for(k=0;k<4;k++){
				int x=i+coor[k][0];
				int y=j+coor[k][1];
				if(x>=0&&x<h&&y>=0&&y<w){
					if(sou[x][y]<mmin){
						mmin=sou[x][y];
						u=x*w+y;
					}
				}
			}
			if(mmin==sou[i][j]) continue;
			int temp=i*w+j;
			union_set(u,temp);
		}
	}

	for(i=0;i<h;i++){
		for(j=0;j<w;j++){
			mid[i][j]=find_set(i*w+j);
		}
	}

	memset(used,0,sizeof(used));
	ch='a';
	for(i=0;i<h;i++){
		for(j=0;j<w;j++){
			if(!used[i][j]){
				used[i][j]=1;
				id[i][j]=ch;
				for(k=0;k<h;k++){
					for(p=0;p<w;p++){
						if(mid[k][p]==mid[i][j]){
							used[k][p]=1;
							id[k][p]=ch;
						}
					}
				}
				ch++;
			}
		}
	}
	return 0;
}

int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int ca;
	scanf("%d",&ca);
	int c;
	for(c=1;c<=ca;c++){
		int i,j;
		scanf("%d%d",&h,&w);
		for(i=0;i<h;i++){
			for(j=0;j<w;j++){
				scanf("%d",&sou[i][j]);
			}
		}

		solve();

		printf("Case #%d:\n",c);
		for(i=0;i<h;i++){
			for(j=0;j<w-1;j++){
				printf("%c ",id[i][j]);
			}
			printf("%c\n",id[i][j]);
		}
	}
	return 0;
}