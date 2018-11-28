#include <cstdio>
#include <vector>
#include <string>
#include <map>
using namespace std;

const int INFTY = 1000000000;

int main(){
	char buf[1024];
	int N;
	gets(buf);
	N=atoi(buf);
	for(int k=1; k<=N; k++){
		int best=INFTY;
		int S,Q;
		map<string,int> m;
		gets(buf);
		S=atoi(buf);
		for(int i=0; i<S; i++){
			gets(buf);
			m[string(buf)]=i;
		}
		gets(buf);
		Q=atoi(buf);
		if(Q==0){
			printf("Case #%d: %d\n",k,0);
			continue;
		}
		vector<vector<int> > dp(Q,S);
		gets(buf);
		int t=m[string(buf)];
		dp[0][t]=INFTY;
		for(int i=1; i<Q; i++){
			int lo=INFTY;
			for(int j=0; j<S; j++){
				if(dp[i-1][j]<lo) lo=dp[i-1][j];
			}
			lo++;
			for(int j=0; j<S; j++){
				dp[i][j]=min(dp[i-1][j],lo);
			}
			gets(buf);
			t=m[string(buf)];
			dp[i][t]=INFTY;
		}
		for(int j=0; j<S; j++){
			if(dp[Q-1][j]<best) best=dp[Q-1][j];
		}
		printf("Case #%d: %d\n",k,best);
	}
	return 0;
}
