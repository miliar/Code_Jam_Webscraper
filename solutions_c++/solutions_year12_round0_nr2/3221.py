#include <cstdio>
#include <cstring>
#define MAXN 102
int n,s,p,d[MAXN];
void Main(int Case){
	scanf("%d%d%d",&n,&s,&p);
	int ans=0;
	for (int i=1;i<=n;++i){
		scanf("%d",&d[i]);
	}
	int sc1=p*3-2,sc2=p*3-4;
	if (sc1<0) sc1=0;
	if (sc2<0) sc2=0;
	for (int i=1;i<=n;++i){
		if (sc1<=d[i]) {ans++;d[i]=-5;}
	}
	if (p>=2){
		for (int i=1;i<=n;++i){
			if (!s) break;
			if (sc2<=d[i]){
				ans++;
				s--;
			}
		}
	}
	printf("Case #%d: %d\n",Case,ans);

}
int main(){
	int T;
	scanf("%d",&T);
	for (int i=1;i<=T;++i){
		Main(i);
	}
	return 0;
}
