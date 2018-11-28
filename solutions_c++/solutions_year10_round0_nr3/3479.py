// BEGIN CUT HERE
#pragma warning(disable:4018)  // signed/unsigned mistatch
#pragma warning(disable:4244)  // w64 to int cast
#pragma warning(disable:4267)  // big to small -- possible loss of data
#pragma warning(disable:4786)  // long identifiers
#pragma warning(disable:4800)  // forcing int to bool
#pragma warning(disable:4996)  // deprecations
// END CUT HERE
#include "assert.h"
#include "ctype.h"
#include "float.h"
#include "math.h"
#include "stdio.h"
#include "string.h"
#include "stdlib.h"
#include "stdarg.h"
#include "time.h"
#include "algorithm"
#include "numeric"
#include "functional"
#include "utility"
#include "bitset"
#include "vector"
#include "list"
#include "set"
#include "map"
#include "queue"
#include "stack"
#include "string"
#include "sstream"
#include "iostream"
using namespace std;

int mask;
int T,R,K,G;
queue<int> q;
int simul(){
	int gan=0;
	queue<int> dq;
	for(int i=0;i<R;++i){
		int cap=K;
		while(!q.empty()){
			int v=q.front();
			if(v<=cap){
				dq.push(v);
				cap-=v;
				gan+=v;
				q.pop();
			}else break;
		}
		while(!dq.empty()){
			q.push(dq.front());
			dq.pop();
		}
	}
	return gan;
}
int main(){
	freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	FILE *f=fopen("out.txt","w");
	scanf("%d",&T);
	int tmp;
	for(int ca=1;ca<=T;++ca){
		scanf("%d %d %d",&R,&K,&G);
		q=queue<int>();
		for(int i=0;i<G;++i) {
			scanf("%d",&tmp);
			q.push(tmp);
		}
		int sol=simul();
		printf("Case #%d: %d\n",ca,sol);
		fprintf(f,"Case #%d: %d\n",ca,sol);
	}
	fclose(f);
	return 0;
}