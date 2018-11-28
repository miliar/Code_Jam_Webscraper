#include<cstdio>

int main(){
	int t;
	scanf("%d",&t);
	for(int caso=1;caso<=t;caso++){
		int n;
		scanf("%d",&n);
		int x=0,m=1<<30,y,s=0;
		for(int i=0;i<n;i++){
			scanf("%d",&y);
			x ^= y;
			if(y<m)m=y;
			s+=y;
		}
		if(x==0)printf("Case #%d: %d\n",caso,s-m);
		else	printf("Case #%d: NO\n",caso);
	}
	return 0;
}
