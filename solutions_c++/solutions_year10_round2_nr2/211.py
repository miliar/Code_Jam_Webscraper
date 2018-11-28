#include <stdio.h>
#include <algorithm>
using namespace std;

int main(){
	int good,bad,c,n,k,b,t,kk,res,x[100],v[100],can[100];

	scanf("%d",&c);
	for (int cc=1;cc<=c;cc++){
		res=0;
		kk=0;
		scanf("%d %d %d %d",&n,&k,&b,&t);
		memset(x,0,sizeof(x));
		memset(v,0,sizeof(v));
		memset(can,0,sizeof(can));
		for (int i=0;i<n;i++)
			scanf("%d",&x[i]);
		for (int i=0;i<n;i++)
			scanf("%d",&v[i]);
		for (int i=0;i<n;i++)
			if (b-x[i]<=t*v[i]) can[i]=1;
		for (int i=0;i<n;i++)
			if (can[i]==1)
				kk++;
		if (kk<k) res=-1;
		else{
			res=0;
			good=0;
			bad=0;
			for (int i=n-1;i>=0;i--){
				if (good>=k) break;
				if (can[i]==0){
					bad++;
				}
				else{
					good++;
					res+=bad;
				}
			}
		}
		if (res==-1) printf("Case #%d: IMPOSSIBLE\n",cc);
		else printf("Case #%d: %d\n",cc,res);
	}
	return 0;
}