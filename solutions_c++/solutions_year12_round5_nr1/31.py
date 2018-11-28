#include<cstdio>
#include<algorithm>
#include<vector>
#define L 10000

using namespace std;

int l[L],p[L];
int xl[L];
int n;

bool cmp(int a,int b){
	int aa=100*(100-p[a])*l[a]+(100-p[b])*(100-p[a])*l[b];
	int bb=100*(100-p[b])*l[b]+(100-p[b])*(100-p[a])*l[a];
	if (aa<bb)
		return true;
	if (aa>bb)
		return false;
	return a<b;

}

void solve(){
	scanf("%d",&n);
	for (int i=0;i<n;++i)
		scanf("%d",&l[i]);
	for (int i=0;i<n;++i)
		scanf("%d",&p[i]);
	for (int i=0;i<n;++i){
		xl[i]=i;
	}
	sort(xl,xl+n,cmp);
	for (int i=0;i<n;++i){
		printf("%d ",xl[i]);
	}
	puts("");
}

int T,I=0;

int main(){
	scanf("%d",&T);
	while (T--){
		printf("Case #%d: ",++I);
		solve();
	}
}
