#include<cstdio>
#include<algorithm>
#include<string>
using namespace std;
int t[256],cnt, ax[100];
bool vis[256], odv[256];
string a;
char buff[100];
int main() {
	int n;
	scanf("%d",&n);
	for(int x=1;x<=n;++x) {
		cnt = 0;
		a.clear(), scanf("%s",buff), a = string(buff);
		for(int i=0;i<256;++i) vis[i] = 0, odv[i] = 0;
		ax[0] = 1, vis[1] = 1, t[a[0]] = 1, odv[a[0]]=1;
		for(int i=1;i<a.size();++i)
			if(!odv[a[i]]) {
				while(vis[cnt]) ++cnt;
				ax[i] = cnt, vis[cnt] = 1, t[a[i]]=cnt, odv[a[i]]=1;
			} else
				ax[i] = t[a[i]];
		long long k=1, res=0;
		++cnt;
		cnt = max(cnt,2);
		for(int i=a.size()-1;i>=0;--i) {
			res += (long long)ax[i]*k, k*=(long long)cnt;
		}
		printf("Case #%d: %lld\n", x, res);
	}
	return 0;
}