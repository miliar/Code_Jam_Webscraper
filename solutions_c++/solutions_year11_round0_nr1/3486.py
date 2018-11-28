#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cassert>
#include<string>
#include<algorithm>
#include<fstream>
#include<sstream>
#include<set>
#include<map>
#include<vector>
#include<queue>
#include<deque>
#include<complex>
#include<numeric>
using namespace std;

int P[10000],T[10000],dp[10000],pos[10000];
char A[100],B[100];
int run() {
	int N;
	scanf("%d", &N);
	vector<int> X[2],Y[2];
	X[0].push_back(1);
	X[1].push_back(1);
	Y[0].push_back(0);
	Y[1].push_back(0);
	dp[0]=0;
	for(int i=0;i<N;++i){
		int r;
		scanf("%s %d", A, &r);
		int t = (A[0]=='O');
		pos[i+1]=X[t].size();
		X[t].push_back(r);
		P[i+1]=r;T[i+1]=t;
		dp[i+1]=max(dp[i] + 1, 1 + Y[t].back() + abs(X[t].back() - X[t][pos[i+1]-1]));
		Y[t].push_back(dp[i+1]); 
	}
	return dp[N];
}

int main() {
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	
	int test;scanf("%d",&test);
	for(int no=1;no<=test;++no){
		printf("Case #%d: %d\n",no,run());
	}
}
