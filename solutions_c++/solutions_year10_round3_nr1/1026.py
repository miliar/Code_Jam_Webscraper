#include<stdio.h>
#include<algorithm>
struct G{
	int a,b;
}g[10001];
bool cmp1(G aa,G bb){
	return aa.a<bb.a;
}
bool cmp2(G aa,G bb){
	return aa.b<bb.b;
}
main(){
	int i,j,k;
	int n,T,kk,aa;
	
	scanf("%d",&T);
	kk=0;
	while(T--){
		kk++;
		scanf("%d",&n);
		for(i=0;i<n;i++){
			scanf("%d%d",&g[i].a,&g[i].b);
		}
		std::sort(g,g+n,cmp1);
		aa=0;
		for(i=0;i<n;i++){
			for(j=i+1;j<n;j++){
				if(g[i].b>g[j].b){
					aa++;
				}
			}
		}
		printf("Case #%d: %d\n",kk,aa);
	}
}
