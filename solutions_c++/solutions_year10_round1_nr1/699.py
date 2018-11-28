#include <stdio.h>

const int N = 100;

char t[N][N], map[N][N];

int dx[] = {0, -1, -1, -1, 0, 1, 1, 1};
int dy[] = {-1, -1, 0, 1, 1, -1, 0, 1};

void rotate(int n)
{
    int i, j;
    for(i = 0; i < n; ++i) {
        for(j = 0; j < n; ++j)
            map[j][n - 1 - i] = t[i][j];
    }
}

void legal(int n)
{
    int i, j, low;
    bool flag = false;
    for(j = 0; j < n; ++j) {
        flag = false;
        for(i = n - 1; i >= 0; --i) {
            if(map[i][j] == '.' && !flag) {
                flag = true;
                low = i;
            }
            else if(map[i][j] != '.'){
                if(flag) {
                    map[low][j] = map[i][j];
                    map[i][j] = '.';
                    --low;
                }
            }
        }
    }
}

bool win(int x, int y, int n, int k, char ch)
{
    int i, tx, ty, cnt;
    for(i = 0; i < 8; ++i) {
        tx = x, ty = y, cnt = 0;
        while(1) {
            if(tx >= 0 && tx < n && ty >= 0 && ty < n &&
                map[tx][ty] == ch) {
                ++cnt;
            }
            else
                break;
            if(cnt == k)
                return true;
            tx += dx[i];
            ty += dy[i];
        }
    }
    return false;
}

int main()
{
    int re, rep, n, i, j, k;
    bool winb, winr;
    freopen("A-large.in.txt", "r", stdin);
    freopen("out1.txt", "w", stdout);
    scanf("%d", &rep);
    for(re = 1; re <= rep; ++re) {
        scanf("%d%d", &n, &k);
        for(i = 0; i < n; ++i)
            scanf("%s", t[i]);
        rotate(n);
        /*for(i = 0; i < n; ++i) {
            for(j = 0; j < n; ++j)
                printf("%c", map[i][j]);
            printf("\n");
        }
        printf("\n\n");*/
        legal(n);
        /*for(i = 0; i < n; ++i) {
            for(j = 0; j < n; ++j)
                printf("%c", map[i][j]);
            printf("\n");
        }
        printf("\n\n");
        */
        winb = winr = false;
        for(i = 0; i < n; ++i) {
            for(j = 0; j < n; ++j) {
                if(map[i][j] != 'R')
                    continue;
                if(win(i, j, n, k, 'R')) {
                    winr = true;
                    break;
                }
            }
            if(j < n)
                break;
        }
        for(i = 0; i < n; ++i) {
            for(j = 0; j < n; ++j) {
                if(map[i][j] != 'B')
                    continue;
                if(win(i, j, n, k, 'B')) {
                    winb = true;
                    break;
                }
            }
            if(j < n)
                break;
        }
        printf("Case #%d: ", re);
        if(winr && winb)
            printf("Both\n");
        else if(winr)
            printf("Red\n");
        else if(winb)
            printf("Blue\n");
        else
            printf("Neither\n");
    }
    return 0;
}
