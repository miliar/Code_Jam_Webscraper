#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
#define MaxN 1000
int n;
int candy[MaxN+5];
void init(){
	int i;
	scanf("%d",&n);
	for (i=0;i<n;i++) scanf("%d",&candy[i]);
}
void solve(){
	int minc,i,tmp,sum;
	minc=candy[0];
	tmp=candy[0];
	sum=candy[0];
	for (i=1;i<n;i++){
		if (minc>candy[i]) minc=candy[i];
		sum+=candy[i];
		tmp=tmp^candy[i];
	}
	if (tmp) printf("NO\n");
	else printf("%d\n",sum-minc);
}
int main()
{
//	freopen("C-small-attempt0.in","r",stdin);
//	freopen("C-small-attempt0.out","w",stdout);
//	freopen("data.txt","r",stdin);
	int t,i;
	scanf("%d",&t);
    for (i=1;i<=t;i++){
		printf("Case #%d: ",i);
        init();
		solve();
    }
    return 0;
}