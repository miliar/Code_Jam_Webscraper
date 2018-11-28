#include <cstdio>
#include <cstdlib>
#include <vector>
#include <cmath>

using namespace std;
inline int xabs(const int a) { return (a<0)?-a:a;}
int bitcount(int x){
	int ret=0;
	while(x!=0) {
		ret++;
		x&=(x-1);
	}
	return ret;
}
int biggest_diff(int* candy, int len){
	int max_diff=0;
	int ans=-1;
	for(int state=1;state<(1<<len)-1;state++){
		int my_A=0,my_B=0, his_A=0, his_B=0;
		
		for(int i=0;i<len;i++){
			if (state&(1<<i)){
				my_A+=candy[i];
				his_A^=candy[i];
			}
			else{
				my_B+=candy[i];
				his_B^=candy[i];
			}
		}
		if (his_A==his_B){
			int diff=xabs(my_A-my_B);
			ans=max(ans,max(my_A,my_B));
		
		}
	}
	return ans;
}
int C[41];

int main(){
	int T;
	scanf("%d", &T);
	for(int cas=1;cas<=T;cas++){
		fprintf(stderr,"case=%d %d\n",cas,T);
		int N;
				scanf("%d", &N);
		for(int i=0;i<N;i++){
			scanf("%d",C+i);
		}
		int ans=biggest_diff(C,N);
		printf("Case #%d: ",cas);
		if (ans==-1) printf("NO\n");
		else printf("%d\n",ans);
	}
	return 0;
}
