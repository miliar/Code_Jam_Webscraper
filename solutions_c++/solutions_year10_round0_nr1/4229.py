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

bool mat[31];
int T,N,K;
bool simul(){
	for(int i=0;i<K;++i){
		for(int j=0;j<N;++j){
			if(mat[j]){
				mat[j]=false;
			}else{
				mat[j]=true;
				break;
			}
		}
	}
	for(int j=0;j<N;++j) 
		if(!mat[j]) return false;
	return true;
}
int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&T);
	for(int ca=1;ca<=T;++ca){
		memset(mat,false,sizeof(mat));
		scanf("%d %d",&N,&K);
		if(simul()){
			printf("Case #%d: ON\n",ca);
		}else{
			printf("Case #%d: OFF\n",ca);
		}
	}
	return 0;
}