#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<vector>
#include<string>
#include<algorithm>
#include<queue>
using namespace std;

#define min(a,b) (((a)<(b))?(a):(b))
#define max(a,b) (((a)>(b))?(a):(b))
#define rep(i,n) for(i=0;i<(n);i++)
#define MAX 105

int a[1005];
bool flag[1005];

int main() {
	int T,kase=1;
	int i,n,len,x,res;
	scanf(" %d",&T);
	while(T--) {
		printf("Case #%d: ",kase++);
		scanf(" %d",&n);
		rep(i,n) { scanf(" %d",&a[i]); a[i]--; }
		memset(flag,0,sizeof(flag));
		res = 0;
		rep(i,n) {
			if(flag[i]) continue;
			if(i == a[i]) { flag[i] = 1; continue; }
			x = a[i];
			len = 2;
			flag[i] = flag[a[i]] = 1;
			while(1) {
				if(a[x] == i) break;
				len++;
				flag[a[x]] = 1;
				x = a[x];
			}
			//res += (len-1) * 2;
			res += len;
		}
		printf("%d\n",res);
	}
	return 0;
}