#include<cstdio>
#include<algorithm>
using namespace std;
int main(){
	int t;
	scanf("%d",&t);
	for(int caso=1;caso<=t;caso++){
		printf("Case #%d: ",caso);
		int n,r=0, po=1,pb=1,qo=0,qb=0;
		scanf("%d",&n);
		for(int i=0;i<n;i++){
			char q; int b;
			scanf(" %c %d",&q,&b);
			if(q=='O'){
				r+= max(0,abs(po-b)-qo)+1;
				qb+=max(0,abs(po-b)-qo)+1;
				qo=0;
				po=b;
			}
			else{
				r+= max(0,abs(pb-b)-qb)+1;
				qo+=max(0,abs(pb-b)-qb)+1;
				qb=0;
				pb=b;
			}
		}
		printf("%d\n",r);
	}
	return 0;
}
