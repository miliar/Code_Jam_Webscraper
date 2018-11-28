#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;

int TC,N,S[10005],A[10005],B[10005],L1,L2,ans,t1;
int arr[10005];

int main(){
	freopen("B-large.in","r",stdin);
	freopen("B.out","w",stdout);
	scanf("%d",&TC);
	for(int testcase=1;testcase<=TC;++testcase){ 
		scanf("%d",&N);
		memset(S,0,sizeof(S));
		for(int i=0;i<N;++i){
			scanf("%d",&arr[i]);
			++S[arr[i]];
		}
		L1 = L2 = 0;
		for(int i=1;i<=10001;++i){
			if(S[i] - S[i-1] > 0){
				t1 = S[i]-S[i-1];
				while(t1--) A[L1++] = i;
			}
			if(S[i] - S[i-1] < 0){
				t1 = S[i-1] - S[i];
				while(t1--) B[L2++] = i;
			}
		}
		ans = N;
		for(int i=0;i<L1;++i){
			ans = min(ans,B[i]-A[i]);
		}
		printf("Case #%d: %d\n",testcase,ans);
	}
}
