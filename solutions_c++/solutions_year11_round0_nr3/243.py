#include<cstdio>
int a[100];
int main(){
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int i,s,m,n,t,tt=1;
	scanf("%d",&t);
	while(t--){
		printf("Case #%d: ",tt++);
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%d",&a[i]);
		m=0;
		for(i=0;i<n;i++)
			m^=a[i];
		if(m!=0){
			puts("NO");
			continue;
		}
		m=s=a[0];
		for(i=1;i<n;i++){
			if(m>a[i])m=a[i];
			s+=a[i];
		}
		printf("%d\n",s-m);
	}
	return 0;
}