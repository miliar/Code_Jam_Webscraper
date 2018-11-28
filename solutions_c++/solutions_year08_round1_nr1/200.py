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
#define INF 2147483600
#define FOR(i,start,end) for(int i=(start); i<(end); ++i)
//#define FORALL(it,A) for(typeof((A).begin()) it=(A).begin(); it!=(A).end(); ++it)
#define FORALL(tp,it,A) for(tp::iterator it=(A).begin(); it!=(A).end(); ++it)
#define DEB(x) cout << #x << ":" << x << endl


const double eps=1e-11;


int main(){


	int D;
	scanf("%d",&D);
	FOR(d,1,D+1){
		int N;
		scanf("%d",&N);
		vector<LLI> A(N),B(N);
		FOR(i,0,N) scanf("%lld",&A[i]);
		FOR(i,0,N) scanf("%lld",&B[i]);
		LLI res=0;
		sort(A.begin(),A.end());
		sort(B.begin(),B.end());
		FOR(i,0,N) res+=(LLI)A[i]*B[N-i-1];
		printf("Case #%d: %lld\n",d,res);
	}



	return 0;
}
