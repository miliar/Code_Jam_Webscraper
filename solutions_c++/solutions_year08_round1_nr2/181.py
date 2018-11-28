#include<stdio.h>
#include<string.h>

bool mal[2010],luv[2010][2010],ko[2010];
int luvm[2010],cnt[2010];
int n,m,k;
int main(){
	int ca; scanf("%d",&ca);
	for (int tt=1; tt<=ca; tt++){
		scanf("%d%d",&n,&m);
		memset(mal,0,sizeof(mal));
		memset(luv,0,sizeof(luv));
		memset(luvm,-1,sizeof(luvm));
		memset(cnt,0,sizeof(cnt));
		for (int i=0; i<m; i++){
			int k; scanf("%d",&k);
			for (int j=0; j<k; j++){
				int x,y; scanf("%d%d",&x,&y); x--;
				if (y==0) luv[i][x]=true,cnt[i]++;
				else luvm[i]=x;
			}
		}
		bool fin=false;
		memset(ko,0,sizeof(ko));
		while (!fin){
			fin=true;
			for (int i=0; i<m; i++){
				if (cnt[i]==0 && luvm[i]!=-1){
					fin=false;
					mal[luvm[i]]=true;
					ko[i]=true;
					for (int j=0; j<m; j++){
						if (luv[j][luvm[i]]){
							luv[j][luvm[i]]=false;
							cnt[j]--;
						}
					}
					luvm[i]=-1;
				}
			}
		}
		bool pp=true;
		for (int i=0; i<m; i++){
			if (ko[i]) continue;
			if (cnt[i]==0) pp=false;
		}
		if (pp){
			printf("Case #%d: ",tt);
			for (int i=0; i<n-1; i++) printf("%d ",mal[i]); printf("%d\n",mal[n-1]);
		}else printf("Case #%d: IMPOSSIBLE\n",tt);
	}
	return 0;
}
