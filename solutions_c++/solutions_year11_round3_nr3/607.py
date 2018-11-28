#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;
int n, N,L,H;
int Case = 0;

bool check(int A, int B) {
    return (A % B == 0) || (B % A == 0);

}

int main() {
	scanf("%d", &n);
	while(n--) {
        ++Case;
		scanf("%d %d %d", &N, &L, &H);
        int Z[N];

        for(int i = 0; i < N; ++i)
            scanf("%d", Z + i);

        int ans = -1;
        for(int f = L; f <= H; ++f) {
            bool ok = true;        
            for(int i = 0; i < N; ++i) {
                if(!check(f, Z[i])) {
                    ok = false;
                    break;
                }


            }
            if(ok) { ans = f; break; }
        }        



        printf("Case #%d: ", Case);
        if(ans != -1) {
            printf("%d\n", ans);
        } else {
            printf("NO\n");
        }

	}
	return 0;
}
