#include <cstdio>
#include <cstring>

using namespace std;

int Min(int a, int b){
	return a < b? a: b;
}
const int N = 11000;
int d[N], l[N], pre[N];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int cas=1; cas<=T; cas++){
        printf("Case #%d: ", cas);
        for(int i = 2; i < N; i ++) pre[i] = -1;
        int n;
        scanf("%d", &n);
        int nowd = 0;
        d[0] = 0;
        pre[1] = 0;
        for(int i = 1; i <= n; i++){
            scanf("%d%d", d+i, l+i);
		}
		int D;
		scanf("%d", &D);
		int reach = 0;
		bool flag = 0;
		for(int i = 1; i <= n; i ++){
			if(pre[i] == -1) break;
			reach = d[i] + Min(d[i] - d[pre[i]], l[i]);
			if(reach >= D){
				flag = true;
				break;
			}
			for(int j = i + 1; j <= n; j ++){
				if(pre[j] == -1 && d[j] <= reach){
					pre[j] = i;
				}
			}
		}

		if(flag) puts("YES");
		else puts("NO");
    }
    return 0;
}
