#include<cstdio>
#include<cstring>
int abs(int x){
	if(x<0)
		return -x;
	return x;
}
int main(){
	freopen("A-large.in","r",stdin);
	freopen("2.txt","w",stdout);
	int t,n,m;
	char c[2];
	scanf("%d",&t);
	for(int k=1;k<=t;++k){
		scanf("%d",&n);
		int a1=1,a2=1,ans=0,b1=0,b2=0;
		for(int i=0;i<n;++i){
			scanf("%s%d",&c,&m);
			ans++;
			if(c[0]=='O'){
				if(b1+abs(m-a1)+1>ans)
					ans=b1+abs(m-a1)+1;
				a1=m;
				b1=ans;
			}else{
				if(b2+abs(m-a2)+1>ans)
					ans=b2+abs(m-a2)+1;
				a2=m;
				b2=ans;
			}
		}
		printf("Case #%d: %d\n",k,ans);
	}
	return 0;
}
