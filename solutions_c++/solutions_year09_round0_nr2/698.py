#include<iostream>
using namespace std;

int heigh[120][120];
char mark[120][120];

int T, H, W;
char cc;
char now;

const int dx[] = {-1, 0, 0, 1};
const int dy[] = {0, -1, 1, 0};

void search(int h, int w) {
    if (mark[h][w] != 0) {
        now = mark[h][w];
        return;
    }

    int lo = -1;
    for (int k=0;k<4;++k) {
        int x = h + dx[k];
        int y = w + dy[k];
        if ((x < 0) || (x >= H)) continue;
        if ((y < 0) || (y >= W)) continue;
        if (heigh[x][y] < heigh[h][w]) {
            if ((lo == -1) || (heigh[h + dx[lo]][w + dy[lo]] > heigh[x][y]))
                lo = k;
        }
    }

    if (lo == -1) {
        now = cc++;
        return;
    }

    search(h+dx[lo], w+dy[lo]);
}

void fill(int h, int w) {
    if (mark[h][w] != 0) return;
    mark[h][w] = now;

    int lo = -1;
    for (int k=0;k<4;++k) {
        int x = h + dx[k];
        int y = w + dy[k];
        if ((x < 0) || (x >= H)) continue;
        if ((y < 0) || (y >= W)) continue;
        if (heigh[x][y] < heigh[h][w]) {
            if ((lo == -1) || (heigh[h + dx[lo]][w + dy[lo]] > heigh[x][y]))
                lo = k;
        }
    }

    if (lo == -1) {
        return;
    }

    fill(h+dx[lo], w+dy[lo]);
}


int main() {
    FILE* fin = freopen("input.in", "r", stdin);
    scanf("%d", &T);
    for (int i=0;i<T;++i) {
        scanf("%d %d", &H, &W);
        for (int h=0;h<H;++h) {
            for (int w=0;w<W;++w) {
                scanf("%d", &heigh[h][w]);
            }
        }

        memset(mark, 0, sizeof(mark));
        cc = 'a';
        for (int h=0;h<H;++h)
            for (int w=0;w<W;++w) {
                search(h, w);
                fill(h, w);
            }

        printf("Case #%d:\n", i+1);
        for (int h=0;h<H;++h) {
            for (int w=0;w<W;++w) {
                if (w!=0) printf(" ");
                printf("%c", mark[h][w]);
            }
            printf("\n");
        }
    }
    return 0;
}
