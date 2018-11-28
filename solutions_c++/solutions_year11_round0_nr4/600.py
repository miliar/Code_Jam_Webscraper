#include<cstdio>

int main(){
	int t;
	scanf("%d",&t);
	for(int caso=1;caso<=t;caso++){
		int n;
		int v[1010];
		int m[1010];
		scanf("%d",&n);
		for(int i=1;i<=n;i++){
			scanf("%d",&v[i]);
			m[i]=0;
		}
		double r=0.0;
		for(int i=1;i<=n;i++){
			int cnt=0;
			for(int j=i;!m[j];j=v[j]){m[j]++;cnt++;}
			if(cnt>1)r+=cnt;
		}
		printf("Case #%d: %.6f\n",caso,r);
	}
	return 0;
}
