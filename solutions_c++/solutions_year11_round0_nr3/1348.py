#include <iostream>
#include <cstdio>
using namespace std;

int T,S,MIN,N,tmp,x;

int main(){
	freopen("C-large.in","r",stdin);
	freopen("C.out","w",stdout);
	scanf("%d",&T);
	for(int cn=1;cn<=T;++cn){
		S = tmp = 0;
		MIN = 1000001;
		scanf("%d",&N);
		for(int i=0;i<N;++i){
			scanf("%d",&x);
			S += x;
			tmp ^= x;
			MIN = min(x,MIN);
		}
		if(tmp > 0) printf("Case #%d: NO\n",cn);
		else printf("Case #%d: %d\n",cn,S-MIN);
	}
}
