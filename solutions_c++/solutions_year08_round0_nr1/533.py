#include <stdio.h>
#include <map>
#include <string>
#define INF 1000000

using namespace std;

char buffer[2000];
map<string,int> mape;
int ar[2000];
int dp[2000][200];
int S,Q;

int go(int pos, int cur) {
	if (pos==Q) return 0;
	int &ans=dp[pos][cur];
	if (ans!=-1) return ans;
	ans=INF;
	if (ar[pos]==cur) {
		for (int i=0; i<S; i++) {
			if (i==cur) continue;
			int ta=go(pos+1,i);
			if (ta<ans) ans=ta;
		}
		ans++;
	}
	else {
		ans=go(pos+1,cur);
	}
	return ans;
}

int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t,T;
	int i;
	scanf("%d", &T);
	for (t=1; t<=T; t++) {
		mape.clear();
		memset(dp,-1,sizeof(dp));
		scanf("%d", &S); fgets(buffer,1000,stdin);
		for (i=0; i<S; i++) {
			fgets(buffer,1000,stdin); 
			string s=buffer;
			mape[s]=i;
		}
		scanf("%d", &Q); fgets(buffer,1000,stdin);
		for (i=0; i<Q; i++) {
			fgets(buffer,1000,stdin);
			string s=buffer;
			ar[i]=mape[s];
		}
		int ans=INF;
		for (i=0; i<S; i++) {
			int ta=go(0,i);
			if (ta<ans) ans=ta;
		}
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}