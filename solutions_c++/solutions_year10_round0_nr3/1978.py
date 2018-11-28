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
typedef long long int i64;
int mask;
long long int T,R,K,G;
int q[10000001];
pair<int,int> mark[10000001];
bool mark2[10000001];
i64  simul(){
	i64 gan=0;
	vector<int> cant;
	memset(mark2,false,sizeof(mark2));
	int pos=0,pmark=0;
	for(int i=0;i<R;++i){
		if(mark2[pos]){
			pmark=mark[pos].first;
			pos=mark[pos].second;
			gan+=cant[pmark];
		}else{
			mark2[pos]=true;
			pair<int,int> &pp=mark[pos];
			pp.first=cant.size();
			int cap=0;
			int cont=0;
			while(true){
				int &v=q[pos];
				if(K>=cap+v){
					cont++;
					if(cont>G) break;
					pos=(pos+1)%G;
					cap+=v;
					gan+=v;
				}else break;
			}
			pp.second=pos;
			cant.push_back(cap);
		}
	}
	return gan;
}
int main(){
	freopen("C-large.in","r",stdin);
	//FILE *f=fopen("C-small-attempt0.out","w");
	scanf("%d",&T);
	int tmp;
	for(int ca=1;ca<=T;++ca){
		scanf("%d %d %d",&R,&K,&G);
		for(int i=0;i<G;++i) {
			scanf("%d",&q[i]);
		}
		i64 sol=simul();
		printf("Case #%d: %lld\n",ca,sol);
		//fprintf(f,"Case #%d: %lld\n",ca,sol);
	}
	//fclose(f);
	return 0;
}