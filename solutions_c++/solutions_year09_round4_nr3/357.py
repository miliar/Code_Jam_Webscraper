#include <stdio.h>
#include <string.h>
#include <assert.h>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

#define REP(i,n) for (int i=0,_n=n; i<_n; i++)

bool cross(vector<int> &a, vector<int> &b){
	REP(i,a.size()){
		if (a[i]==b[i]) return true;
		if (i==0) continue;
		if (a[0] < b[0]){
			if (a[i] >= b[i]) return true;
		} else {
			if (a[i] <= b[i]) return true;
		}
	}
	return false;
}

vector<int> can;
int con[101][101];
int memo[1<<16];
int T,N,K;

int rec(int mask){
	if (mask==(1<<N)-1) return 0;

	int &ret = memo[mask];
	if (ret!=-1) return ret;
	ret = N*N;

	REP(i,can.size()){
		if (mask & can[i]) continue;
		ret = min(ret, 1 + rec(mask|can[i]));
	}
	return ret;
}

int main(){
	scanf("%d",&T);	
	REP(TC,T){
		scanf("%d %d",&N,&K);
		vector<vector<int> > arr(N, vector<int>(K,0));
		REP(i,N) REP(j,K) scanf("%d",&arr[i][j]);
		REP(i,N) REP(j,N) con[i][j] = !cross(arr[i],arr[j]);

		can.clear();
		REP(i,1<<N){
			REP(a,N) if (i&(1<<a))
				REP(b,N) if (i&(1<<b))
					if (a!=b && !con[a][b]) goto next;
			can.push_back(i);
			next:;
		}

		memset(memo,-1,sizeof(memo));
		printf("Case #%d: %d\n",TC+1,rec(0));
	}
}
