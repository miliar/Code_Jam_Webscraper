#include <cstdio>
#include <cstdlib>

const int MAX = 60;
const int INF = 1<<29;

int t, k, cas = 0;

int calMax(int x, int y, int k){
    return k+abs(x-k)+abs(y-k);
}

bool outOfRange(int x, int size){
    if (x <= 0 || x >= size) return 1;
    return 0;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d", &t);
    while (t--){
        char arr[MAX*2][MAX*2]={};
        bool invalid[MAX*2][MAX*2]={};
        int tot = 0;

        scanf("%d", &k);
        for (int i = 1; i <= k; ++i){
            int pos = k-i+1;
            for (int j = 1; j <= i; ++j){
                scanf(" %c", &arr[i][pos]);
                ++tot;
                pos += 2;
            }
        }
        for (int i = k+1; i < 2*k; ++i){
            int pos = i-k+1;
            for (int j = 1; j <= 2*k-i; ++j){
                scanf(" %c", &arr[i][pos]);
                ++tot;
                pos += 2;
            }
        }
        for (int v = 1; v < 2*k; ++v)
            for (int i = 1; i <= 2*k; ++i)
                for (int j = 1; j <= 2*k; ++j)
                    if (arr[i][j]){
                        int x = 2*v-i;
                        if (!outOfRange(x, 2*k) && arr[x][j] && arr[i][j] != arr[x][j]){
                            for (int y = 1; y <= 2*k; ++y) invalid[v][y] = 1;
                        }
                    }
        for (int v = 1; v < 2*k; ++v)
            for (int i = 1; i <= 2*k; ++i)
                for (int j = 1; j <= 2*k; ++j)
                    if (arr[j][i]){
                        int x = 2*v-i;
                        if (!outOfRange(x, 2*k) && arr[j][x] && arr[j][i] != arr[j][x]){
                            for (int y = 1; y <= 2*k; ++y) invalid[y][v] = 1;
                        }
                    }
//        for (int i = 1; i < 2*k; ++i){
//            for (int j = 1; j < 2*k; ++j)
//                printf("%c", arr[i][j]);
//                putchar('\n');
//        }
//        for (int i = 1; i < 2*k; ++i){
//            for (int j = 1; j < 2*k; ++j)
//                printf("%c", invalid[i][j] ? '0' : '1');
//                putchar('\n');
//        }

        int ans = INF;
        for (int i = 1; i < 2*k; ++i)
            for (int j = 1; j < 2*k; ++j){
                if (invalid[i][j]) continue;
                int size = calMax(i, j, k);
//                printf("size = %d\n", size);
                int tmp = size*size - tot;
                if (ans > tmp) ans = tmp;
            }
        printf("Case #%d: %d\n", ++cas, ans);
    }
    return 0;
}
