#include <cstdio>
using namespace std;

int T,a,b;

int main(){
	scanf("%d",&T);
	for (int cases=0;cases<T;++cases){
		scanf("%d%d",&a,&b);
		int ans=0,c=1,tmp=a;
		while (tmp/10>0) c*=10,tmp/=10;
		for (int i=a;i<b;++i){
			tmp=i;
			while (true){
				tmp=tmp/10+tmp%10*c;
				if (tmp==i) break;
				if ((i<tmp)&&(tmp<=b)) ++ans;
			}
		}
		printf("Case #%d: %d\n",cases+1,ans);
	}
	return 0;
}