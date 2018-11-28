#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int T,N,x,tmp;


int main(){
	freopen("D-large.in","r",stdin);
	freopen("D.out","w",stdout);
	scanf("%d",&T);
	for(int cn=1;cn<=T;++cn){
		scanf("%d",&N);
		x = 0;
		for(int i=1;i<=N;++i){
			scanf("%d",&tmp);
			if(tmp != i) ++x;
		}
		printf("Case #%d: %d\n",cn,x);
	}
}
