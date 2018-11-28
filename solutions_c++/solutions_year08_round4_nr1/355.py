#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <iostream>
#include <map>
#include <math.h>
#include <set>
#include <queue>
using namespace std;
typedef long long LL;
#define INF 1000000000
#define SZ(v) ((int)(v).size())
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REP(i,n) FOR(i,0,n)
#define FORE(i,a,b) for(int i=(a);i<=(b);i++) 


struct node{
	bool leaf;
	int val;
	bool change;
};
node D [10010];
int mem[10010][2];

int go(int v,int val){
	if(mem[v][val]!=-1) return mem[v][val];
	
	if(D[v].leaf){
		if(val == D[v].val ) mem[v][val] = 0;
		else mem[v][val] = INF;
		
		return mem[v][val];
	}
	mem[v][val] = INF;
	
	int OR = INF;
	
	if(val==0){
		int a = go(v*2,0);
		int b = go(v*2+1,0);
		if(a+b<OR) OR = a+b;
	}
	else{
		int a = go(v*2,1);
		int b = go(v*2,0);
		int c = go(v*2+1,1);
		int d = go(v*2+1,0);
		if(a+c<OR) OR = a+c;
		if(a+d<OR) OR = a+d;
		if(c+b<OR) OR = c+b;
	}
		
	int AND = INF;
	
	if(val==1){
		int a = go(v*2,1);
		int b = go(v*2+1,1);
		if(a+b<AND) AND = a+b;
	}
	else{
		int a = go(v*2,1);
		int b = go(v*2,0);
		int c = go(v*2+1,1);
		int d = go(v*2+1,0);
		if(b+c<AND) AND = b+c;
		if(b+d<AND) AND = b+d;
		if(a+d<AND) AND = a+d;
	}
	
	if(D[v].val == 0){
		if(OR<mem[v][val]) mem[v][val] = OR;
		if(D[v].change && AND+1< mem[v][val] ) mem[v][val] = AND+1;
	}
	else{
		if(AND<mem[v][val]) mem[v][val] = AND;
		if(D[v].change && OR+1< mem[v][val] ) mem[v][val] = OR+1;
	}
	return mem[v][val];
}

int main(){
	int T;
	scanf("%d",&T);
	FORE(t,1,T){
		int m,v;
		scanf("%d%d",&m,&v);
		FORE(i,1,m){
			if(i<=(m-1)/2){
				int a,b;
				scanf("%d%d",&a,&b);
				D[i].leaf = false;
				D[i].val = a;
				if(b==1) D[i].change = true;
				else D[i].change = false;
			}
			else{
				int a;
				scanf("%d",&a);
				D[i].leaf = true;
				D[i].val = a;
			}
			mem[i][0]=-1;
			mem[i][1]=-1;
		}
		int ans = go(1,v);
		if(ans >= INF) printf("Case #%d: IMPOSSIBLE\n",t);
		else printf("Case #%d: %d\n",t,ans);
	}


}
