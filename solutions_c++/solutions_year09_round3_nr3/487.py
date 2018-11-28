#include <iostream>
#include <algorithm>
#include <cstdio>
#include <string.h>

using namespace std;

int use[10];
int pp[105];
int q,n;
int dd[10];
int ans;
void dfs(int cnt,int nn){
	if(cnt==q){
		if(nn<ans)
			ans=nn;
		return ;
	}
	int i,J;
	for(i=0;i<q;i++){
		if(!pp[dd[i]]){
			pp[dd[i]]=1;
		//	int tmp=n-cnt-1;
			
			int tmp=0;
			for(J=dd[i]-1;J>=1;J--){
				if(pp[J]==1) break;
				else tmp++;
			}
			for(J=dd[i]+1;J<=n;J++){
				if(pp[J]==1) break;
				else tmp++;
			}
		
			
			dfs(cnt+1,nn+tmp);
			pp[dd[i]]=0;
		}
	}
}

int main(){
	int i,J,ncase;
	
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	scanf("%d",&ncase);
	for(J=1;J<=ncase;J++){
		
		memset(pp,0,sizeof(pp));
		
		scanf("%d%d",&n,&q);
		for(i=0;i<q;i++)
		scanf("%d",&dd[i]);
		ans=99999;
		dfs(0,0);
		printf("Case #%d: %d\n",J,ans);
	}
}
				
				
