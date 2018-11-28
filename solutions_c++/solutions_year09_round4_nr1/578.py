#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

#define CLR(a) memset(a, 0, sizeof(a))

const int N = 50;
/*
//二分图最大匹配,hungary算法,邻接阵形式,复杂度O(m*m*n)
//返回最大匹配数,传入二分图大小m,n和邻接阵mat,非零元素表示有边
//match1,match2返回一个最大匹配,未匹配顶点match值为-1
#include <string.h>
#define MAXN N
#define _clr(x) memset(x,0xff,sizeof(int)*MAXN)

int hungary(int m,int n,int mat[][MAXN],int* match1,int* match2){
	int s[MAXN],t[MAXN],p,q,ret=0,i,j,k;
	for (_clr(match1),_clr(match2),i=0;i<m;ret+=(match1[i++]>=0))
		for (_clr(t),s[p=q=0]=i;p<=q&&match1[i]<0;p++)
			for (k=s[p],j=0;j<n&&match1[i]<0;j++)
				if (mat[k][j]&&t[j]<0){
					s[++q]=match2[j],t[j]=k;
					if (s[q]<0)
						for (p=j;p>=0;j=p)
							match2[j]=k=t[j],p=match1[k],match1[k]=j;
				}
	return ret;
}
*/
int _mat[N][N], _match[2][N];
int _pos[N];

int main() {
    freopen("a.large.in.txt", "r", stdin);
    freopen("a.large.out.txt", "w", stdout);
    int tc;
    scanf("%d", &tc);
    int n, i, j, in;
    for (int ti = 1; ti <= tc; ++ti) {
        CLR(_mat);
        scanf("%d", &n);
        char s[N];
        for (i = 0; i < n; ++i) {
            scanf("%s", s);
            for (j = 0; j < n; ++j) {
                _mat[i][j] = s[j] - '0';
            }
            for (j = n - 1; j > -1; --j) {
                if (_mat[i][j]) break;
            }
            _pos[i] = j;
            // fill(_mat[i] + j, _mat[i] + n, 1);
            // fill(_mat[i], _mat[i] + j, 0);
        }
        int ans = 0;
        for (;;) {
            for (i = 0; i < n; ++i) {
                if (_pos[i] > i) break;
            }
            if (i == n) break;
            for (j = i + 1; j < n; ++j) {
                if (_pos[j] <= i) break;
            }
            for (; j > i; --j) {
                swap(_pos[j], _pos[j - 1]);
                ++ans;
            }
        }
        printf("Case #%d: %d\n", ti, ans);
    }
    return 0;
}
