#include <cstdio>
#include <cstring>
#include <string>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <cmath>
#include <numeric>
#include <iomanip>
#include <iostream>
#include <cassert>
#include <ext/hash_map>
#include <ext/hash_set>
#include <ext/rope>
#include <ext/slist>

using namespace std;
using namespace __gnu_cxx;

typedef vector<int>VI;
typedef vector<string>VS;
typedef long long LL;
#define SIZE(c) ((int)(c).size())
#define SEQ(c) (c).begin(),(c).end()
#define FOR(i,a,b) for(int _U(b),i=(a);i<_U;++i)
#define REP(i,n) FOR(i,0,n)
#define FORD(i,a,b) for(int _U(a),i=(b)-1;i>=_U;--i)
#define FORS(i,c) FOR(i,0,SIZE(c))
#define REPD(i,n) FORD(i,0,n)
template<class T>string tostr(T v){ostringstream o;o<<v;return o.str();}
const int inf = 1000100100; 

#define maxn 16

bool A[maxn][maxn];
int B1[maxn],B2[maxn];
int N,M;

int I[maxn];

int check(){
	int i;
	for (i=0;i<M-1;i++)
		if (A[I[B1[i]]][I[B2[i]]]==0) return 0;
	return 1;
}

int solve(int cas){
	int i,a,b;
	memset(A,0,sizeof(A));
	scanf("%d",&N);
	for (i=1;i<N;i++){
		scanf("%d%d",&a,&b);
		a--; b--;
		A[a][b]=A[b][a]=1;
	}
	scanf("%d",&M);
	for (i=0;i<M-1;i++){
		scanf("%d%d",&a,&b); a--; b--;
		B1[i]=a; B2[i]=b;
	}
	for (i=0;i<N;i++) I[i]=i;
	do{
		if (check()) return 1;
	}while (next_permutation(I,I+N));
	return 0;
}

int main(){
	int t,cas;
	scanf("%d",&t);
	for (cas=1;cas<=t;cas++)
		printf("Case #%d: %s\n",cas,solve(cas)?"YES":"NO");
	return 0;
}

