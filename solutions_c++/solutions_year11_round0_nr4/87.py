#include <cstdio>
#include <cstring>
#include <cstdlib>
using namespace std;
int fac[10];
int memo[1001];
int prob(int n){
	int &ret=memo[n];
	if (ret!=-1) return ret;
	if (n==0) return 0;
	if (n==1) return 1;
	ret=2*n;
	for (int i=1;i<10;i++)
		ret<?=fac[i]+prob(n-i);
	return ret;
}
int main(){
	freopen("d-large.in","r",stdin);
	freopen("d-large.out","w",stdout);
	memset(memo,-1,sizeof(memo));
	fac[1]=1;
	for (int i=2;i<10;i++)
		fac[i]=fac[i-1]*i;
	int T;
	scanf("%d",&T);
	for (int test=1;test<=T;test++){
		int n;
		scanf("%d",&n);
		int tot=0;
		for (int i=1;i<=n;i++){
			int x;
			scanf("%d",&x);
			if (i!=x) tot++;
		}
		printf("Case #%d: %.9lf\n",test,(double)prob(tot));
	}
//	system("pause");
	return 0;
}
