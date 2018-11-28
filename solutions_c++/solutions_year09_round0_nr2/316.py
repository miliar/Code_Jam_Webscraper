#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include<iostream>
#include<iomanip>
#include<cstdio>
#include<cstdlib>
#include<cctype>
#include<climits>
#include<cmath>
#include<fstream>
#include<sstream>
#include<algorithm>
#include<vector>
#include<list>
#include<map>
#include<set>
#include<deque>
#include<stack>
#include<bitset>
#include<functional>
#include<numeric>
#include<utility>
#include<ctime>
#include<queue>
#include<ext/hash_map>
#include<ext/hash_set>
using namespace std;
using namespace __gnu_cxx;
 
#define ForEach(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
typedef long long int i64;
template<class T,class U> T cast (U x) {T y;ostringstream a;a<<x;istringstream b(a.str());b>>y;return y;}
 
int dx[]={-1,0,0,1};
int dy[]={0,-1,1,0};
int M,N;
const int MAX=1<<7;
int A[MAX][MAX];
int B[MAX][MAX];
bool V[MAX][MAX];
char c,e;

void f(int x, int y){
	if (V[x][y]){
		e=B[x][y];
		return;
	}
	V[x][y]=1;
	int best=A[x][y];
	int ux=-1,uy=-1;
	for (int i=0;i<4;++i){
		int nx=x+dx[i],ny=y+dy[i];
		if (nx<0||nx>M-1||ny<0||ny>N-1) continue;
		if (A[nx][ny]<best){
			best=A[nx][ny]; ux=nx,uy=ny;
		}
	}
	if (ux<0){ B[x][y]=++c;e=c;return;}
	f(ux,uy);
	B[x][y]=e;
}

int main(){	
	int ncases;	scanf("%d",&ncases);
	for (int ncase=1;ncase<=ncases;++ncase){
		scanf("%d%d",&M,&N); for (int i=0;i<M;++i) for (int j=0;j<N;++j) scanf("%d",&A[i][j]);
		memset(B,-1,sizeof B); memset(V,0,sizeof V);
		c='a'-1;
		for (int i=0;i<M;++i) for (int j=0;j<N;++j){
			f(i,j);
		}
		printf("Case #%d:\n",ncase);
		for (int i=0;i<M;++i){
			for (int j=0;j<N;++j){
				if (j) printf(" ");
				printf("%c",B[i][j]);
			}
			printf("\n");
		}
	}
	return 0;
}
