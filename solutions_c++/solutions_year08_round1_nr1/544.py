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
#define MAX 10000
#define i64 __int64
int n;
long long n1[MAX];
long long n2[MAX];
int comp1(const void *a,const void *b){
	return *(long long *)a-*(long long *)b;
}
int comp2(const void *a,const void *b){
	return *(long long *)b-*(long long *)a;
}
void init(){

}

int input(){
	scanf("%d",&n);
	for(int i=0;i<n;i++)scanf("%lld",&n1[i]);
	for(int i=0;i<n;i++)scanf("%lld",&n2[i]);
	return 1;	
}

void process(){
	long long sum=0;
	qsort(n1,n,sizeof(long long),comp1);
	qsort(n2,n,sizeof(long long),comp2);
	for(int i=0;i<n;i++){
		sum+=n1[i]*n2[i];
	}
	printf("%lld\n",sum);
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