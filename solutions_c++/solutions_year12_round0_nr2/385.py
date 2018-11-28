#include <cstdio>

int max(int a,int b){return (a>b)?a:b;}

int main(){
	int ncases;
	scanf("%d", &ncases);
	for(int cas=1;cas<=ncases;cas++){
		int n,s,p,x;
		int res=0;
		scanf("%d %d %d",&n,&s,&p);
		for(int i=0;i<n;i++){
			scanf("%d", &x);
			if(x >= (p+2*max(p-1,0))) res++; else if(s && x>= (p+2*max(p-2,0)) ){res++;s--;}
		}
		printf("Case #%d: %d\n",cas,res);
	}	
	return 0;
}