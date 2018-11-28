#include<stdio.h>
#include<string.h>
#include<algorithm>

using namespace std;

const int N=204;

struct Node{
	int a[26];
}ft[N];


int operator<(Node x,Node y){
	return x.a[0]>y.a[0];
}

int visit[N];
int n,m;
int map[N][N];
int link[N];


int check(int x,int y){
	int i;
	for(i=0;i<m;i++) if(ft[x].a[i]<=ft[y].a[i]) return 0;
	return 1;
}

int find(int a){
	int i,j,k;
	for(i=0;i<n;i++){
		if(!visit[i]&&map[a][i]){
			k=link[i];
			link[i]=a;
			visit[i]=1;
			if(k==-1||find(k)) return 1;
			link[i]=k;
		}
	}
	return 0;
}


int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int i,j,k,t,ans;
	
	int T,ca=0;
	scanf("%d",&T);
	while(T--){
		scanf("%d%d",&n,&m);
		for(i=0;i<n;i++){
			for(j=0;j<m;j++) scanf("%d",&ft[i].a[j]);
		}
		sort(ft,ft+n);

		memset(map,0,sizeof(map));
		for(i=0;i<n;i++){
			for(j=0;j<n;j++){
				if(check(i,j)) map[i][j]=1;
			}
		}
		
		memset(link,-1,sizeof(link));
		ans=0;
		for(i=0;i<n;i++){
			memset(visit,0,sizeof(visit));
			if(find(i)) ans++;
		}
		

		printf("Case #%d: %d\n",++ca,n-ans);

	}
	return 0;
}