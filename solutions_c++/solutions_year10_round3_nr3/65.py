#include <iostream>
#include <cstring>
#include <string>
#include <cmath>
#include <queue>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
using namespace std;
#define	out(x) 		(cout << #x << ": " << x << endl)
#define	MM(m,what)	(memset(m, what, sizeof(m)))
template<class T>void show(T a, int l){for(int i = 0; i < l; ++i)cout << a[i] << ' '; cout << endl;}
template<class T>void show(T a, int l, int r){for(int i = 0; i < l; ++i)show(a[i], r); cout << endl;}
const int MAXN = 520;
bool maze[MAXN][MAXN];
bool flag[MAXN][MAXN];
int ans[MAXN];
bool check(int x1,int y1,int x2,int y2){
    int i,j;
    if(maze[x1][y1]==1){
        for(i = x1;i <= x2; i++){
            for(j = y1;j <= y2; j++){
                if(flag[i][j] == 0) return 0;
                if((i-x1+j-y1)%2 == 0 && maze[i][j] == 0) return  0;
                if((i-x1+j-y1)%2 == 1 && maze[i][j] == 1) return  0;
            }
        }
    }
    if(maze[x1][y1]==0){
        for(i = x1;i <= x2; i++){
            for(j = y1;j <= y2; j++){
                if(flag[i][j] == 0) return  0;
                if((i-x1+j-y1)%2 == 0 && maze[i][j]==1) return  0;
                if((i-x1+j-y1)%2 == 1 && maze[i][j]==0) return  0;
            }
        }        
    }
    return 1;
}
void cal(int x1,int y1,int x2,int y2){
    int i,j;
    for(i = x1;i <= x2; i++){
        for(j = y1 ;j <= y2; j++){
            flag[i][j]=0;
        }
    }
}
int main(){
    freopen("C-large.in","r",stdin);freopen("C-large.out","w",stdout);
    int T, i, j, k, a, M, N;
    scanf("%d",&T);
    char str[MAXN];
	for(int ks = 1; ks <= T; ++ks){
        scanf("%d%d", &M, &N);
        MM(flag, true);
		for(i = 1; i <= M; ++i){
			scanf("%s", str+1);
			for(j = 1; j <= N/4; ++j){
				if(str[j] >= '0' && str[j] <= '9')	a = str[j]-'0';
				else	a = 10+str[j]-'A';
				for(k = j*4; k >= j*4-3; --k, a /= 2)
					maze[i][k] = a&1;
			}
		}
        int L=M<N?M:N,res=0;
        MM(ans, 0);
        
        for(k = L;k >= 1; k--){
            for(i=1;i+k-1<=M;i++){
                for(j=1;j+k-1<=N;j++){
                    if(check(i,j,i+k-1,j+k-1)){
                        ans[k]++;
                        cal(i, j, i+k-1, j+k-1);
                    }
                }
            }
        }
        for(i = 1;i <= L; i++){
            if(ans[i] > 0) res++;
        }
        printf("Case #%d: %d\n", ks, res);
        for(i = L;i >= 1; i--){
            if(ans[i] > 0){
                printf("%d %d\n",i,ans[i]);
            }
        }
    }
    return 0;
}
