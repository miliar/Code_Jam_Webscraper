#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int TC,N,V[1005];
double X,S,R,T,ans,A[1005],B[1005],W[1005],tmp;

bool cmp(int a,int b){
	return W[a] < W[b];
}

inline double dist(int x){
	return B[x] - A[x];
}

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d",&TC);
	for(int testcase=1;testcase<=TC;++testcase){
		scanf("%lf%lf%lf%lf%d",&X,&S,&R,&T,&N);
		R -= S;
		ans = 0;
		for(int i=0;i<N;++i){
			scanf("%lf%lf%lf",&A[i],&B[i],&W[i]);
			W[i] += S;
			V[i] = i;
			X -= (B[i]-A[i]);
		}
		if(X > 0){
			A[N] = 0;
			B[N] = X;
			W[N] = S;
			V[N] = N;
			++N;
		}
		sort(V,V+N,cmp);
		for(int i=0;i<N;++i){
			tmp = (W[V[i]]+R)*T;
			if(T > 0 && tmp >= dist(V[i])){
				ans += dist(V[i])/(W[V[i]]+R);
				T -= dist(V[i])/(W[V[i]]+R);
			}
			else{
				ans += T + (dist(V[i])-T*(W[V[i]]+R))/W[V[i]];
				T = 0;
			}
		}
		printf("Case #%d: %.9lf\n",testcase,ans);
	}
}
