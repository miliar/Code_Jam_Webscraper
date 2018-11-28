#include <iostream>
#include <cstdio>
#include <algorithm>
#define MIN -(1ll<<60);
#define MAX (1ll<<60);
using namespace std;

int T,N,A[205];
long long int D,S[205],P[205],lo,hi,mid,ans,cur,t1,t2;
bool win;

bool cmp(int a,int b){
	return P[a] < P[b];
}

int main(){
	scanf("%d",&T);
	for(int testcase=1;testcase<=T;++testcase){
		scanf("%d%lld",&N,&D);
		D *= 2ll;
		for(int i=0;i<N;++i){
			A[i] = i;
			scanf("%lld%lld",&P[i],&S[i]);
			P[i] *= 2ll;
			--S[i];      //TAKE NOTE OF THIS!!!!!!!!!
		}
		sort(A,A+N,cmp);
		lo = 0;
		hi = MAX;
		while(hi >= lo){
//			printf("lo = %lld hi = %lld\n",lo,hi);
			mid = (hi+lo)/2ll;
			cur = MIN;
			win = 1;
			for(int i=0;i<N;++i){
				if(win == 0) break;
				t1 = max(cur+D,P[i]-mid);
				t2 = t1+D*S[i];
				if(t2-P[i] > mid) win = 0;
				else cur = t2;
			}
			if(win == 1){
				ans = mid;
				hi = mid-1;
			}
			else lo = mid+1;
		}
		printf("Case #%d: %lld.%d\n",testcase,ans/2ll,((ans&1ll) == 0)?0:5);
	}
}
