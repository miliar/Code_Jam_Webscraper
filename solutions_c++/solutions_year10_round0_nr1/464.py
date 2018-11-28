#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;

int N,T,K;
bool work(int n,int k){
	for(int i=0;i<n;i++){
		if(!(k &(1<<i))) return false;
	}
	return true;
}
int main() {
	freopen("f:\\a-small.in","r",stdin);
	freopen("f:\\a_small.out","w",stdout);
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		scanf("%d%d",&N,&K);
		bool plug = work(N,K);
		if(plug)
			printf("Case #%d: ON\n",t);
		else
			printf("Case #%d: OFF\n",t);

	}
	return 0;
}

