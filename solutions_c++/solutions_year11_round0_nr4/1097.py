#include<cstdio>

int t,n,ileok;

int main(){
	scanf("%d",&t);
	for(int y=1; y<=t; y++){
		scanf("%d",&n);
		ileok=0;
		for(int i=1; i<=n; i++){
			int x;
			scanf("%d",&x);
			if(x!=i) ileok++;
		}
		printf("Case #%d: %d.000000\n",y,ileok);
	}
}

