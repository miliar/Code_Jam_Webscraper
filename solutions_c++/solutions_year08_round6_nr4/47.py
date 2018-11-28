#include<stdio.h>
#include<string.h>
bool ed[110][110],ed2[110][110],ans,used[110];
int n,m,a[110];

void run(int d){
	if (d==m){
		bool b=true;
		for (int i=0; i<m; i++){
			for (int j=0; j<m; j++){
				if (ed2[i][j] && !ed[a[i]][a[j]]) b=false;
			}
		}
		if (b){
			ans=true;
		}
	}else{
		for (int i=0; i<n; i++){
			if (used[i]) continue;
			a[d]=i;
			used[i]=true;
			run(d+1);
			used[i]=false;
		}
	}
}

int main(){
	int ca; scanf("%d",&ca);
	for (int tt=1; tt<=ca; tt++){
		scanf("%d",&n);
		memset(ed,0,sizeof(ed));
		for (int i=0; i<n-1; i++){
			int x,y; scanf("%d%d",&x,&y); x--; y--;
			ed[x][y]=ed[y][x]=true;
		}
		scanf("%d",&m);
		memset(ed2,0,sizeof(ed2));
		for (int i=0; i<m-1; i++){
			int x,y; scanf("%d%d",&x,&y); x--; y--;
			ed2[x][y]=ed2[y][x]=true;
		}
		ans=false;
		memset(used,0,sizeof(used));
		run(0);
		printf("Case #%d: ",tt);
		if (ans) printf("YES\n");
		else printf("NO\n");
	}
	return 0;
}
