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
#define MAX 1020
#define i64 __int64
int cases,caseno=0;
int S,Q;
int s[MAX][MAX];
//int q[MAX][MAX];
int a1[MAX],a2[MAX];
struct srch{
	char nm[MAX];
	int indx;
}qr[MAX];
struct engn{
	char nm[MAX];
	int first;
	int last;
}eng[MAX];
void init(){
	
}

int input(){
	scanf("%d%*c",&S);
	for(int i=0;i<S;i++){
		gets(eng[i].nm);
	}
	scanf("%d%*c",&Q);
	for(int i=0;i<Q;i++){
		gets(qr[i].nm);
		qr[i].indx=i;
	}
	return 1;	
}
int comp(const void *a,const void *b){
	srch  x=*(srch *)a;
	srch  y=*(srch *)b;
	int tmp= strcmp(x.nm,y.nm);
	if(!tmp)return x.indx-y.indx;
	else return tmp;
}
int cmp(const void *a,const void *b){
	engn  x=*(engn *)a;
	engn  y=*(engn *)b;
	return strcmp(x.nm,y.nm);
}
int cmp1(const void *a,const void *b){
	engn  x=*(engn *)a;
	engn  y=*(engn *)b;
	return x.first-y.first;
}

/*
void process(){
	init();
	qsort(eng,S,sizeof(engn),cmp);
	qsort(sr,Q,sizeof(srch),comp);
	int first;
	int last;
	int j=0;
	for(int i=0;i<S;i++){
		for(;j<Q;j++){
			if(!strcmp(eng[i].nm,sr[i].nm)){
				if(eng[i].first)
					eng[i].last=j;
				else eng[i].first=j;
			}
			else{
				j--;
				break;
			}
		}

	}

}
*/
void process(){
	int prn=0,end=0;
	int i=0,j=0,startj=0;
	while(!end){
		int first=0;
		int last=0;
		int mx=0;
		for(i=0;i<S;i++){
			first=0;
			last=0;
			eng[i].first=0;
			for(j=startj;j<Q;j++){
				if(!strcmp(eng[i].nm,qr[j].nm)){
					if(eng[i].first)eng[i].last=j+1;
					else eng[i].first=j+1;
					if(eng[i].first-1>mx)mx=eng[i].first-1;
				}
			}
			if(!eng[i].first){
				end=1;
				break;
			}
		}

		startj=mx;
		if(!end)prn++;
	}
	printf("Case #%d: %d\n",++caseno,prn);

}
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d%*c",&cases);
	while(cases--){
		input();
		process();	
	}
}