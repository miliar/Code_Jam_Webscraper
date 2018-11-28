#include<cstdio>
#include<cstring>
int a[10005];
int main(){
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	int cas,r=1; scanf("%d",&cas);
	while(cas--){
		int n,st,ed;
		scanf("%d%d%d",&n,&st,&ed);
		for(int i=0; i<n; i++) scanf("%d",&a[i]);
		int res;
		for(res=st; res<=ed; res++){
			int ok=1;
			for(int i=0; i<n && ok; i++){
				if(res>=a[i] && res%a[i]!=0) ok=0;
				if(res<a[i] && a[i]%res!=0) ok=0;
			}
			if(ok) break;
		}
		printf("Case #%d: ",r++);
		if(res>ed) puts("NO");
		else printf("%d\n",res);
	}
}
