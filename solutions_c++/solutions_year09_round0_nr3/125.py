#include<string>
#include<algorithm>
#include<memory>
#include<string>
using namespace std;
#define FOR(i,a,b) for(int i=(a); i<(b); ++i)
#define cs c_str()
#define sz size()
string need = "welcome to code jam";

int dp[502][20], m = need.sz;
string x;
int n;
int doit(int a, int b) {
	if(a<0 || b<0) return 0;
	if(b==0) return 1;
	int& ret = dp[a][b];
	if(ret!=-1) return ret;
	ret = 0;
	FOR(i,0,a) {
		if(x[i] == need[b-1]) {
			ret += doit(i, b-1);
			ret %= 10000;
		}
	}
	return ret;
}
string trimit(string x) {
	if(x.sz == 0) return x;
	if(x[x.sz - 1] == 10 || x[x.sz - 1] == 13)
		return trimit(x.substr(0, x.sz - 1));
	return x;
}
int main() {
	freopen("C.in","r",stdin);
	int T, e = 0;
	scanf("%d ",&T);	
	char buff[1024];
	while(T--) {
		memset(buff, 0, sizeof (buff));
		gets(buff);
		int ans = 0;
		x = trimit(buff);
		n = x.sz;
		memset(dp, -1, sizeof(dp));
		ans = doit(n, m);
		printf("Case #%d: %04d\n",++e, ans);
	}
	return 0;
}
