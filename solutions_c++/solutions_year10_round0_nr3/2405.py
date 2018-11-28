#include <iostream>
#include <algorithm>
#include <cstdio>
#include <string.h>
#include <queue>

using namespace std;

int dd[1001];
int main(){
	
	int T,cas,n,k,r,i,ans,tmp,J;
	freopen("C-small-attempt1.in","r",stdin);
	freopen("C-small-attempt1.out","w",stdout);
	scanf("%d",&T);
	for(cas=1;cas<=T;cas++){
		scanf("%d%d%d",&r,&k,&n);
		for(i=0;i<n;i++)
			scanf("%d",&dd[i]);
		
		ans=0;
		i=0;
		J=0;
		while(r--){
			J=i;
			tmp=dd[i];
			i++;
			if(i==n)
				i=0;
			while(tmp+dd[i]<=k&&i!=J){
				tmp+=dd[i];
				i++;
				if(i==n) i=0;
			}
			ans+=tmp;
			
		}
		printf("Case #%d: %d\n",cas,ans);
	}
	

}
