#include<cstdio>
#include<cstring>
int n,t,k,m,a,ans;
int main(){
	freopen("C-large.in","r",stdin);
	freopen("2.txt","w",stdout);
	scanf("%d",&t);
	for(int i=0;i<t;++i){
		scanf("%d",&n);
		k=0,m=10000000,ans=0;
		for(int j=0;j<n;++j){
			scanf("%d",&a);
			k^=a;
			if(a<m)
				m=a;
			ans+=a;
		}
		if(k)
			printf("Case #%d: NO\n",i+1);
		else
			printf("Case #%d: %d\n",i+1,ans-m);
	}
	return 0;
}
