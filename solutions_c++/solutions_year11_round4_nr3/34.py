#include <stdio.h>
#include <string.h>
#define maxm 1000000
typedef long long LL;
LL pr[200000],pn;
int tag[maxm];
int tn,cp;
LL n;
LL ans;
int main(){
	int i,j,k;
	pn=0;
	for (i=2;i<maxm;i++)
		if (!tag[i]){
			pr[pn++]=i;
			for (j=i+i;j<maxm;j+=i) tag[j]=1;
		}
	for (scanf("%d",&tn),cp=1;cp<=tn;cp++){
		scanf("%lld",&n);
		ans=1;
		for (i=0;i<pn && pr[i]*pr[i]<=n;i++){
			k=0;
			LL tmp=pr[i];
			while (tmp*pr[i]<=n){
				tmp*=pr[i];
				k++;
			}
			ans+=k;
		}
		if (n==1) ans=0;
		printf("Case #%d: %d\n",cp,ans);
	}
	return 0;
}