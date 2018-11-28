#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
const int Max=128;
int pr[Max][Max];
int N,K;
bool isOver(int a,int b){
	for(int i=0;i<K;++i) if(pr[a][i]<=pr[b][i]) return false;
	return true;
}
bool mp[Max*2][Max*2];
int mat[Max*2];
bool vst[Max*2];
bool match(int u){
	for(int v=0;v<N*2;++v){
		if(mp[u][v]&&!vst[v]){
			vst[v]=true;
			if(mat[v]==-1||match(mat[v])){
				mat[v]=u;
				return true;
			}
		}
	}
	return false;
}
int main(){
	freopen("C-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int TT;scanf("%d",&TT);
	for(int cas=1;cas<=TT;++cas){
		scanf("%d %d",&N,&K);
		for(int i=0;i<N;++i){
			for(int j=0;j<K;++j) scanf("%d",pr[i]+j);
		}
		memset(mp,0,sizeof(mp));
		for(int i=0;i<N;++i){
			for(int j=0;j<N;++j) mp[i][j+N]=isOver(i,j);
		}
		int cnt=0;
		memset(mat,-1,sizeof(mat));
		for(int i=0;i<N*2;++i){
			memset(vst,0,sizeof(vst));
			cnt+=match(i);
		}
		printf("Case #%d: %d\n",cas,N-cnt);
	}
	return 0;
}
