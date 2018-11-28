#include<cstdio>
#include<algorithm>
#define FOR(a,b) for(int a=0;a<b;++a)
int licz(int l, int q, int c){
	int p=q;
	while(l<p){
		l*=c;
		p/=c;
		if(p*c<q) ++p;
		q=p;
	}
	return l;
}
int main(){
	int z,l,p,c;
	scanf("%d",&z);
	FOR(x,z){
		int wyn;
		printf("Case #%d: ",x+1);
		scanf("%d %d %d",&l,&p,&c);
		wyn=0;
		while(l*c<p){
			p=licz(l,p,c);
			//printf("%d.",p);
			++wyn;
		}
		printf("%d\n",wyn);
	}
}
/*



*/
