#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#define MAXP 1000005
using namespace std;

int T,L,ans;
long long int t1,t2,N,P[100005];
bool prime[1000005],call = 0;

int main(){
	freopen("C-large.in","r",stdin);
	freopen("C.out","w",stdout);
	for(int i=2;i<=MAXP;++i)
		if(!prime[i]){
			P[L++] = i;
			if((long long int)(i)*(long long int)(i) <= (long long int)(MAXP))
				for(int j=i*i;j<=MAXP;j+=i) prime[j] = 1;
		}
	scanf("%d",&T);
	for(int testcase=1;testcase<=T;++testcase){
		scanf("%lld",&N);
		if(N == 1){
			printf("Case #%d: 0\n",testcase);
			continue;
		}
		ans = 1;
		for(int i=0;i<L && P[i]*P[i] <= N;++i){
			t1 = P[i];
			t2 = 0;
			while(t1 <= N){
				t1 *= P[i];
				++t2;
			}
			ans += (t2-1);
		}
		printf("Case #%d: %d\n",testcase,ans);
	}
}
