#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<algorithm>
#include<iostream>
using namespace std;

int pic[150][150];
int cnt[150];

int n,m;
int check(int x,int y,int len){
	int tot=0;
	for(int i=0;i<len&&i+x<n;++i){
		for(int j=0;j<len&&j+y<m;++j){
			int bit=((i&1)^(j&1));
			if(pic[i+x][j+y]==-1)return 0;
			if(bit==0&&pic[i+x][j+y]==pic[x][y]||
			   bit==1&&pic[i+x][j+y]==1-pic[x][y])
				++tot;
			else return 0;
		}
	}
	//printf("check (%d,%d) %d: %d\n",x,y,len,tot);
	//system("pause");
	if(tot==len*len)return 1;
	return 0;
}

int cut(int x,int y,int len){
	for(int i=0;i<len&&i+x<n;++i){
		for(int j=0;j<len&&j+y<m;++j){
			pic[i+x][j+y]=-1;
		}
	}
	return 0;
}

int main(){
	int M,N;
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;++t){
		scanf("%d%d",&n,&m);
		memset(pic,0,sizeof(pic));
		memset(cnt,0,sizeof(cnt));
		for(int i=0;i<n;++i){
			for(int j=0;j<m;j+=4){
				int s;
				scanf("%1x",&s);
				if(s&(1<<3))pic[i][j]=1;
				if(s&(1<<2))pic[i][j+1]=1;
				if(s&(1<<1))pic[i][j+2]=1;
				if(s&(1<<0))pic[i][j+3]=1;
			}
		}
		/*for(int i=0;i<n;++i){
			for(int j=0;j<m;++j)
				printf("%d",pic[i][j]);
			printf("\n");
		}*/
		int ans=0;
		for(int len=min(n,m);len>0;--len){
			for(int i=0;i<n;++i){
				for(int j=0;j<m;++j){
					if(check(i,j,len)){
						cut(i,j,len);
						++cnt[len];
					}
				}
			}
			if(cnt[len])++ans;
			//system("pause");
		}
		printf("Case #%d: %d\n",t,ans);
		for(int len=min(n,m);len>0;--len){
			if(cnt[len])
				printf("%d %d\n",len,cnt[len]);
		}
	}
}