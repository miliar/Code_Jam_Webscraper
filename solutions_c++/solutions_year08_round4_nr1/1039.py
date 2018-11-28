
#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <list>
#include <math.h>
#include <queue>
using namespace std;


#define LLI long long
#define INF 21474836
#define FOR(i,start,end) for(int i=(start); i<(end); ++i)
//#define FORALL(it,A) for(typeof((A).begin()) it=(A).begin(); it!=(A).end(); ++it)
#define FORALL(tp,it,A) for(tp::iterator it=(A).begin(); it!=(A).end(); ++it)
#define DEB(x) cout << #x << ":" << x << endl


const double eps=1e-11;



vector<bool> isAnd,isChang;
vector<int> min1,min0;
int N;



int getMM(int node, int v, int a, int b, int p, int q){

	int result = INF;
	if (v)
		if (isAnd[node])
			result = min(b+q,result);
		else
			result = min( min(b,q),result);
	else
		if (isAnd[node])
			result = min( min(a,p),result);
		else
			result = min(a+p,result);
	return result;
}


int getMin(int node, int v){
	if (node > (N-1)/2)
		if (v) return min1[node];
		else return min0[node];
	int a = getMin(2*node,0);
	int b = getMin(2*node,1);
	int p = getMin(2*node+1,0);
	int q = getMin(2*node+1,1);
	
	int result=getMM(node,v,a,b,p,q);
	if (isChang[node]){
		isAnd[node] = !isAnd[node];
		result = min(result,1+getMM(node,v,a,b,p,q));
		isAnd[node] = !isAnd[node];
	}
	return result;
}


int main(){

	int D,Node0,Nnodes;
	scanf("%d",&D);
	FOR(dd,1,D+1){
		scanf("%d%d",&Nnodes,&Node0);

		isAnd.clear(); isChang.clear();
		min1.clear(); min0.clear();
		isAnd.assign(Nnodes*2+5,false);
		isChang.assign(Nnodes*2+5,false);
		min1.assign(Nnodes*2+5,INF);
		min0.assign(Nnodes*2+5,INF);
		N = Nnodes;
		FOR(n,0,(Nnodes-1)/2){
			int a,b;
			scanf("%d%d",&a,&b);
			if (a) isAnd[n+1] = true;
			if (b) isChang[n+1] = true;
		}
		FOR(n,(Nnodes-1)/2,Nnodes){
			int a;
			scanf("%d",&a);
			if (a) min1[n+1] = 0;
			else min0[n+1] = 0;
		}
		int result = getMin(1,Node0);
		if (result==INF) printf("Case #%d: IMPOSSIBLE\n",dd);
		else printf("Case #%d: %d\n",dd,result);
	}


	return 0;
}

