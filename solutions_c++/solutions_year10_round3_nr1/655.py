#include<cstdio>
#include<algorithm>
#define FOR(a,b) for(int a=0;a<b;++a)
struct pair{
	int a,b;
};
bool comp(const pair& a, const pair& b){
	return a.a<b.a;
}
pair tab[1005];
int main(){
	int z,n,a,b;
	scanf("%d",&z);
	FOR(x,z){
		printf("Case #%d: ",x+1);
		scanf("%d",&n);
		FOR(i,n){
			scanf("%d %d",&a,&b);
			tab[i].a=a;
			tab[i].b=b;
		}
		int wyn=0;
		std::sort(tab,tab+n,comp);
		FOR(i,n){
			//printf("%d %d\n",tab[i].a, tab[i].b);
			for(int j=i+1;j<n;++j){
				if(tab[i].b>tab[j].b) ++wyn;
			}
		}
		printf("%d\n",wyn);
	}
}
/*



*/
