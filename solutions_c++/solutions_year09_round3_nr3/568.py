#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
#define M 100
#define MAX 0x7fffffff
int sou[M+5];
int used[M+5];
int wall[M+10];
int p,q;
int res;

int DFS(int d,int s){

	if(d==q){
		if(s<res)
			res=s;
		return 0;
	}

	int i,j;

	for(i=0;i<q;i++){
		if(!used[i]){
			int t=s;
			used[i]=1;
			wall[sou[i]]=1;
			for(j=sou[i]-1;j>=1;j--){
				if(wall[j]==0)
					t++;
				else break;
			}

			for(j=sou[i]+1;j<=p;j++){
				if(wall[j]==0)
					t++;
				else break;
			}

			DFS(d+1,t);
			used[i]=0;
			wall[sou[i]]=0;
		}
	}
	return 0;
}

int main(){
	freopen("C-small-attempt0.in","rb",stdin);
	freopen("C-small-attempt0.out","wb",stdout);
	int ca,i,j;
	scanf("%d",&ca);
	for(i=1;i<=ca;i++){
		scanf("%d%d",&p,&q);

		for(j=0;j<q;j++)
			scanf("%d",&sou[j]);
		memset(used,0,sizeof(used));
		memset(wall,0,sizeof(wall));
		res=MAX;
		DFS(0,0);
		printf("Case #%d: %d\n",i,res);
	}
	return 0;
}