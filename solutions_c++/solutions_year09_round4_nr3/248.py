#include <cstdio>
#include <cstring>
#include <cctype>
#include <algorithm>
#include <vector>
#include <string>
#include <cmath>
#include <cstdlib>

using namespace std;

int a[100][100];
int g[100][100];
int match1[100], match2[100];

int match(int n,int m)
{
	int s[1000],t[1000];
	int p,q,i,j,k,ret=0;
	memset(match1,0xff,sizeof(match1));
	memset(match2,0xff,sizeof(match2));
	for(i=0;i<n;ret+=(match1[i]>=0),i++){
		memset(t,0xff,sizeof(t));
		s[p=q=0]=i;
		for(;p<=q&&match1[i]<0;p++) {
			for(k=s[p],j=0;j<m&&match1[i]<0;j++) {
				if (g[k][j]&&t[j]<0){
					s[++q]=match2[j],t[j]=k;
					if (s[q]<0)
						for(p=j;p>=0;j=p)
							match2[j]=k=t[j],p=match1[k],match1[k]=j;
				}
			}
		}
	}
	return ret;
}

int main() {
	int i, j, k, t, n;
	int testcase;

	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);

	scanf("%d", &testcase);
	for (int TT = 1; TT <= testcase; TT++) {
		scanf("%d%d",&n,&k);
		for (i = 0; i < n; i++) {
			for (j = 0; j < k; j++) {
				scanf("%d", &a[i][j]);
			}
		}
		memset(g, 0, sizeof(g));
		for (i = 0; i < n; i++) {
			for (j = 0; j < n; j++) {
				for (t = 0; t < k; t++) {
					if (a[i][t] <= a[j][t]) break;
				}
				if (t == k) g[i][j] = 1;
			}
		}
		printf("Case #%d: %d\n", TT, n - match(n, n));
	}

	return 0;
}
