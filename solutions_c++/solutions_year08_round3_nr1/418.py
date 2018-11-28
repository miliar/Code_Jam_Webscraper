/*
	Title      :
	ACM No     :
	Algorithm  :
	Complexity :
	Status     :
	Author     : Debashis Maitra
*/

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <memory.h>
#include <queue>
#include <stack>
#include <algorithm>
#include <iostream>
#include <ctype.h>
#include <time.h>
#include <map>
#include <set>
#include <vector>
#include <string>

using namespace std;

#define CLR(x) memset((x),0,sizeof(x))
#define CLRn(a,x,n) memset((a),0,sizeof(x)*n) 
#define INF 2147483647
#define MAX 2000
#define i64 __int64
long long mxLt,ky,lt;
long long ltr[MAX];
long long uky[MAX];
void init(){
	CLR(uky);
}
int comp2(const void *a,const void *b){
	return *(long long *)b-*(long long *)a;
}
int input(){
	init();
	scanf("%lld %lld %lld",&mxLt,&ky,&lt);
	for(int i=0;i<lt;i++){
		scanf("%lld",&ltr[i]);
	}
	return 1;	
}

void process(){
	qsort(ltr,lt,sizeof(long long),comp2);
	long long cnt=0;
	int pre=0;
	for(long long i=0;i<lt;i++){
		long long mn=999999;
		long long k=0;
		for(long long j=0;j<ky;j++){
			if(uky[j]<=mn){
				mn=uky[j];
				k=j;
				if(!mn)break;
			}
		}
		if(uky[k]>=mxLt){
			puts("Impossible");
			return ;
		}
		uky[k]++;
		cnt+=ltr[i]*uky[k];
	}
	printf("%lld\n",cnt);
}
int main(){
	freopen("input.txt","r",stdin);
	freopen("outputA_lrg.txt","w",stdout);
	int cases,caseno=0;
	scanf("%d",&cases);
	while(cases--){
		printf("Case #%d: ",++caseno);
		input();
		process();	
	}
}