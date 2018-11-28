#include <cstdio>
#include <algorithm>
using namespace std;
int TC,P,Q,T,r1,r2,pos,n;
char cmd[5];
int main(){
	scanf("%d",&TC);
	for (int C=1;C<=TC;C++){
		scanf("%d",&n);
		
		P=Q=T=0;
		r1=r2=1;
		
		for (int i=1;i<=n;i++){
			scanf("%s%d",cmd,&pos);
			if (cmd[0]=='O'){
				
				P = max(T,P + abs(r1-pos)) + 1;
				r1 = pos;
				T = P;
				
			}
			else {
				Q = max(T,Q + abs(r2-pos)) + 1;
				r2 = pos;
				T = Q;
			}
		}
		printf("Case #%d: %d\n",C,T);
	}
	//scanf("\n");
	return 0;
}
