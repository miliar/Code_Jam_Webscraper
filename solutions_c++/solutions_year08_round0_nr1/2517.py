#include<stdio.h>
#include<string>
#include<map>
#include<algorithm>
using namespace std;

map<string,int> mm;
int dp[1024];
int a[1024];
int v[128];
int n,m;

void run(int T) {
	mm.clear();
	scanf("%d",&n);
	char tmp[128];
	gets(tmp);
	for(int i=0;i<n;i++) {
		gets(tmp);
		mm.insert(make_pair(string(tmp),i));
	}
	scanf("%d",&m);
	gets(tmp);
	for(int i=0;i<m;i++) {
		gets(tmp);
		a[i]=mm[tmp];
		int cnt=0,ret=1000000;
		memset(v,0,sizeof(v));
		v[a[i]]=1,cnt=1;
		for(int j=i;j>=0;j--) {
			ret=min(ret,dp[j]);
			if (!j) break;
			else if (!v[a[j-1]]) {
				v[a[j-1]]=1;
				cnt++;
				if (cnt==n) break;
			}
		}
		dp[i+1]=ret+1;
	}
	printf("Case #%d: %d\n",T,max(dp[m]-1,0));
}

int main() {
	int N,T=0;
	for(scanf("%d",&N);N--;)
		run(++T);
	return 0;
}
