#include <stdio.h>
#include <algorithm>
#include <string.h>
#include <memory.h>
#include <queue>
#include <vector>
#include <math.h>
int o_o;
#define N 55
double t,v[N],x[N],b;
int n,ans,k;

int main(void) {
	freopen(".in","r",stdin);
	freopen(".out","w",stdout);
	
	scanf("%d",&o_o);
	for (int O_o=1;O_o<=o_o;O_o++) {
		scanf("%d%d%lf%lf",&n,&k,&b,&t);
                for (int i=0;i<n;i++) {
                	scanf("%lf",&x[i]);

                }
                for (int i=0;i<n;i++) {
                	scanf("%lf",&v[i]);

                }
		
		int kol=0; ans = 0;
                for (int i=n-1;i>=0;i--) {
                	if ((b-x[i])/v[i]<=t) {
                		if (!k) break;
                		ans += kol;
                		k--;
                	} else kol++;
                }

		printf("Case #%d: ",O_o);
		if (!k) printf("%d\n",ans);
		else puts("IMPOSSIBLE");
	}

	return 0;
} 
