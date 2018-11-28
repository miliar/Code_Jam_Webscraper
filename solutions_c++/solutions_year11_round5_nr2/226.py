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
#define MAXN 1005

int a[MAXN];
bool f[MAXN];
bool stflag[MAXN], enflag[MAXN];

int main() {
	int n,i,j,k,r,prev;
	int T,kase=1;
	bool flag,ft;
	scanf(" %d",&T);
	while(T--) {
		printf("Case #%d: ",kase++);
		scanf(" %d",&n);
		if(n == 0) {
			printf("0\n");
			continue;
		}
		rep(i,n) {
			scanf(" %d",&a[i]);
		}
		sort(a, a+n);

		for(r=n;r>=2;r--) {
			memset(f,0,sizeof(f));
			memset(stflag,0,sizeof(stflag));
			memset(enflag,0,sizeof(enflag));
			flag = true;
			while(1) {
				ft=0;
				rep(i,n) if(f[i] == 0) {
					f[i] = 1;
					prev = a[i];
					for(j=i+1,k=1;j<n && k<r;j++) {
						if(f[j] == 0 && a[j] > prev) {
							if(a[j] - prev > 1) { flag = false; goto label; }
							f[j] = 1;
							k++;
							prev = a[j];
							if(k == r) break;
						}
					}
					if(k != r) {
						flag = false;
						goto label;
					}
					ft = 1;
					break;
				}
				if(!ft) break;
label:			if(flag == false) {
					j = i-1;
					while(j>=0) {
						if(a[j] + 1 < a[i]) break;
						if(a[j] + 1 == a[i] && enflag[j] == 1) {
							enflag[j] = 0;
							enflag[i] = 1;
							flag = true;
							break;
						}
						j--;
					}

					j = i+1;
					while(j<n) {
						if(a[i] + 1 > a[j]) break;
						if(a[i] + 1 == a[j] && stflag[j] == 1) {
							stflag[j] = 0;
							stflag[i] = 1;
							flag = true;
							break;
						}
						j++;
					}
					if(!flag) break;
				}
				else {
					stflag[i] = 1;
					enflag[j] = 1;
				}

			}
			if(flag) break;
		}
		printf("%d\n",r);
	}
	return 0;
}