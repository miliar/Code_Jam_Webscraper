#include<cstdio>

using namespace std;

int C,n,m,i,out,ans,j,len,a,b,tot,I;
int al[1000],need[1000];

main(){
	scanf("%d",&C);
	while (C--){
		scanf("%d",&n);
		scanf("%d",&m);
		for (i=0;i<m;++i){
			scanf("%d",&len);
			need[i]=-1;
			al[i]=0;
			for (j=0;j<len;++j) {
				scanf("%d%d",&a,&b);
				a--;
				if (b==1) need[i]=a;
				else al[i]|=(1<<a);
			}
		}
		out=-1;ans=n+1;
		for (i=0;i<(1<<n);++i){
			tot=0;
			for (j=0;j<n;++j)
				if ((1<<j)&i)
					++tot;
			if (tot>=ans) continue;
			bool bt=true;
			for (j=0;j<m;++j)
				if (need[j]>=0 && ((1<<need[j])&i) || (((1<<n)-1)^i)&al[j]) continue;
				else {bt=false;break;}
			if (bt) ans=tot,out=i;
		}
		printf("Case #%d:",++I);
		if (out<0) printf(" IMPOSSIBLE\n");
		else{
			for (i=0;i<n;++i)
			    if (out&(1<<i)) printf(" 1");
			    else printf(" 0");
			printf("\n");
		}
	}
}
