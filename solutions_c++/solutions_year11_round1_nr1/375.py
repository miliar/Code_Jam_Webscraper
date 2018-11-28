#include <cstdio>
using namespace std;

typedef long long int64;

int D, G;
int64 N;

bool solve(){
	if(G==100){
		return D==100;
	}
	if(D==100){
		return G!=0;
	}
	if(G==0){
		return D==0;
	}
	if(N>=100){
		return true;
	}
	else{
		for(int i=1; i<=N; i++){
			for(int j=0; j<=i; j++){
				if(D*i == j*100){
					return true;
				}
			}
		}
	}
	return false;
}

int main(){
	int T;
	scanf("%d",&T);
	for(int c=1; c<=T; c++){
		scanf("%lld%d%d",&N,&D,&G);
		printf("Case #%d: %s\n",c, solve()?"Possible":"Broken");
	}
	return 0;
}
