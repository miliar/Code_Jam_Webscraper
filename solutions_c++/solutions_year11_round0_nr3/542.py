#include<cstdio>
#include<algorithm>

#define rep(i,n) for(int i=0;i<(n);i++)

using namespace std;

const int INF=1<<29;

int main(){
	int T0; scanf("%d",&T0);
	for(int T=1;T<=T0;T++){
		int n; scanf("%d",&n);
		int sum=0,cmin=INF,XOR=0;
		rep(i,n){
			int c; scanf("%d",&c);
			sum+=c;
			cmin=min(cmin,c);
			XOR^=c;
		}
		if(XOR!=0) printf("Case #%d: NO\n",T);
		else       printf("Case #%d: %d\n",T,sum-cmin);
	}

	return 0;
}
