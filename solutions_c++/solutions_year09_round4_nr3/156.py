#include <stdio.h>
#include <string.h>

const int size=200;
int n,k,pr[size][size],lt[size][size];
int ly[size],x[size];

int find(int i){
	x[i]=1;
	for(int j=0; j<n; j++){
		if(!lt[i][j]) continue;
		if(ly[j]<0||x[ly[j]]==0&&find(ly[j])){
			ly[j]=i;
			return 1;
		}
	}
	return 0;
}

int match(){
	int r=0;
	memset(ly,-1,sizeof(ly));
	for(int i=0; i<n; i++){
		memset(x,0,sizeof(x));
		r+=find(i);
	}
	return r;
}

int main(){
	int T;
	scanf("%d",&T);
	for(int cs=1; cs<=T; cs++){
		scanf("%d%d",&n,&k);
		for(int i=0; i<n; i++){
			for(int j=0; j<k; j++)
				scanf("%d",&pr[i][j]);
		}
		for(int i=0; i<n; i++){
			for(int j=0; j<n; j++){
				int v;
				for(v=0; v<k; v++)
					if(pr[i][v]>=pr[j][v]) break;
				lt[i][j]=(v>=k)?1:0;
				//if(lt[i][j]) printf("i=%d j=%d\n",i,j);
			}
		}
		printf("Case #%d: %d\n",cs,n-match());
	} 
	return 0;
}
