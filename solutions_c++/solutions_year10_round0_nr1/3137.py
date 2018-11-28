#include<iostream>
#include<math.h>
#include<stdlib.h>
#include<algorithm>
#include<stdio.h>
using namespace std;
int main(){
	freopen("A-large.in","r",stdin);
	freopen("data.out","w",stdout);
	int T;
	int N,K;
	int k = 1;
	scanf("%d",&T);
	while(T--){
		scanf("%d%d",&N,&K);
		printf("Case #%d:",k);
		if(K!=0&&(K+1)%(int)pow(2.,N)==0)
			printf(" ON\n");
		else
			printf(" OFF\n");
		k++;
	}
	return 0;
}