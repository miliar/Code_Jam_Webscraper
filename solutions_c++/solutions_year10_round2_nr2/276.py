#include<stdio.h>
#include<memory.h>
#include<algorithm>
#include<math.h>
#include<stdlib.h>

int T;
int n,k,b,t,x[1111],v[1111],col=0,sum=0,bad=0;

int main(void){
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d\n",&T);
	for(int _=1;_<=T;_++){
		scanf("%d%d%d%d",&n,&k,&b,&t);
		for(int i=0;i<n;i++){
			scanf("%d",&x[i]);
		}
		for(int i=0;i<n;i++){
			scanf("%d",&v[i]);
		}
		col=0;
		sum=0;
		bad=0;
		for(int i=n-1;i>=0 && col<k;i--){
			if(x[i]+t*v[i]>=b){
				col++;
				sum+=bad;
			}else bad++;
		}
		if(col!=k) printf("Case #%d: IMPOSSIBLE\n",_);else
			printf("Case #%d: %d\n",_,sum);
	}
	return 0;
}
