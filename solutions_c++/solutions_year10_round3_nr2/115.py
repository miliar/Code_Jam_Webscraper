#include<iostream>
#include <math.h>
using namespace std;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("outBB.txt","w",stdout);
	int t;
	scanf("%d",&t);
	__int64 l,p,c;
	int jishu=0;
	while(t--){
		jishu++;
		scanf("%I64d%I64d%I64d",&l,&p,&c);
		int ans=0;
		while(l<p){
			if(l*c<p) ans++;
			l*=c;
		}
		int yxc=0;
		while(ans>0){
			 ans=ans/2;
			yxc++;
		}
		printf("Case #%d: %d\n",jishu,yxc);

	}
	return 0;
}