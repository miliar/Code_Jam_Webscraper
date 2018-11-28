#include<cstdio>
#include<cstring>
int n,t,b,m,ac,pb,po,tb,to,tmp;
int f(int x){return x>0?x:-x;}
char ch;
int main(){
	scanf("%d",&t);
	for (int z=1; z<=t; z++){
		ac=0; tb=to=0; pb=po=1;
		scanf("%d",&n);
		for (int i=1; i<=n; i++){
			scanf(" %c",&ch);
			scanf("%d",&m);
			if (ch=='O'){
				to+=f(m-po);
				po=m;
				if (to<=tb) to=tb;
				++to;
				ac=to;
			}
			else{
				tb+=f(m-pb);
				pb=m;
				if (tb<=to) tb=to;
				++tb;
				ac=tb;
			}
		}
		printf("Case #%d: %d\n",z,ac);
	}
	return 0;	
}
