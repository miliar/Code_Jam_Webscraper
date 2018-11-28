#define MD(x) if (0) {x;}
#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <sstream>
void MyAssert(int p){ while (!p) printf("error\n"); };
#define O1(S,A,n) MD(cout<<S<<":";for (int i=0; i<n; i++)cout<<A[i]<<" ";cout<<endl;)
#define O2(S,A,n) MD(cout<<S<<"\n";for (int i=0; i<n; i++){for (int j=0; j<n; j++)cout<<A[i][j]<<" ";cout<<endl;})
using namespace std;

const int maxN = 218;

int G[maxN][maxN],MY[maxN],Used[maxN];
int NX,NY;

bool dfs(int x) {
	Used[x] = true;
	for (int y = 0; y<NY; y++) if (G[x][y])
		if (MY[y]==-1){
			MY[y] = x;
			return true;
		}
		else{
			int tx = MY[y];
			MY[y] = x;
			if (!Used[tx] && dfs(tx))return true;
			MY[y] = tx;
		}
	return 0;
}

int match(){
	memset(MY,-1,sizeof(MY));
	int ret = 0;
	for (int i=0; i<NX; i++){
		memset(Used,0,sizeof(Used));
		ret += dfs(i);
	}        
	return ret;
}

int A[maxN][maxN];

int main(){
	int tc;
	scanf("%d",&tc);
	for (int ti=1; ti<=tc; ti++){
		printf("Case #%d: ",ti);
		// TODO
		int N,K;
		scanf("%d%d",&N,&K);
		for (int i=0; i<N; i++)
			for (int j=0; j<K; j++)
				scanf("%d",&A[i][j]);
		memset(G,0,sizeof(G));
		for (int i=0; i<N; i++)
			for (int j=0; j<N; j++)if (j!=i){
				bool ok = true;
				for (int r=0; r<K; r++)
					if (A[i][r]>=A[j][r]) ok = false;
				if (ok) G[i][j] = true;
			}
		NX = NY = N;
		O2("G",G,N);
		printf("%d\n", N - match() );
	}
	
	return 0;
}
