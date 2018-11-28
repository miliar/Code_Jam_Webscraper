#include <iostream>
#include <algorithm>
#include <string.h>
#include <math.h>
using namespace std;

int n,m,p,q;

int main(){
	freopen("1.in","r",stdin);
	freopen("3.out","w",stdout);
	
	int T;
	scanf("%d",&T);
	for (int cas=1;cas<=T;++cas){
		scanf("%d%d%d",&n,&p,&q);
		if (q==100 && p!=100){
			printf("Case #%d: Broken\n",cas);
			continue;
		}
		if (q==0 && p!=0){
			printf("Case #%d: Broken\n",cas);
			continue;
		}
		
		int a=p,b=100;
		while (b^=a^=b^=a%=b);
		if (100/a <= n) printf("Case #%d: Possible\n",cas);
		else printf("Case #%d: Broken\n",cas);
	}
	return 0;
}
