#include<cstdio>

#define rep(i,n) for(int i=0;i<(n);i++)

using namespace std;

int main(){
	int T0; scanf("%d",&T0);
	for(int T=1;T<=T0;T++){
		int n; scanf("%d",&n);
		int difcnt=0;
		rep(i,n){
			int a; scanf("%d",&a);
			if(a!=i+1) difcnt++;
		}
		printf("Case #%d: %.9f\n",T,(double)difcnt);
	}

	return 0;
}
