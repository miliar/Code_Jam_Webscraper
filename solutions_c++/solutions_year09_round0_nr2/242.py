#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int tb[200][200];
char l[200][200];
int h, w;

typedef struct {
    int h;
    int x;
    int y;
} pos_t;

pos_t queue[20000];
int qn=0;


pos_t get(int x, int y) {
    pos_t r;
    r.x = x;
    r.y = y;
    if (x<0 || x>=w || y<0 || y>=h) {
        r.h = 999999999;
    } else {
        r.h = tb[y][x];
    }
    return r;
}

int sort_f(const void *a, const void *b) {
    pos_t *pa = (pos_t*)a;
    pos_t *pb = (pos_t*)b;
    int d = pa->h - pb->h;
    if (d!=0) return d;
    d = pa->y - pb->y;
    if (d!=0) return d;
    d = pa->x - pb->x;
    return d;
}

int paint(int x, int y, char label) {
    qn = 0;
    int ll;
    while (true) {
        //printf("> (%d,%d) %d\n", x,y, tb[y][x]);
        if (l[y][x]) {
            ll = l[y][x];
            break;
        }
        pos_t h = get(x,y);
        queue[qn++] = h;

        pos_t w = get(x-1,y);
        pos_t e = get(x+1,y);
        pos_t n = get(x,y-1);
        pos_t s = get(x,y+1);
        int sink = (h.h<=w.h && h.h<=e.h && h.h<=n.h && h.h<=s.h);
        if (sink) {
            ll = label;
            break;
        }
        pos_t p[4] = {w,e,n,s};
        qsort(p, 4, sizeof(pos_t), sort_f);
        x = p[0].x;
        y = p[0].y;
    }
    for (int i=0; i<qn; i++) {
        l[queue[i].y][queue[i].x] = ll;
    }
    return ll;
}


int main() {
    int t;
    scanf("%d", &t);
    for (int i=1; i<=t; i++) {
        scanf("%d%d", &h, &w);
        for (int j=0; j<h; j++) {
            for (int k=0; k<w; k++) {
                scanf("%d", &tb[j][k]);
            }
        }
        memset(l,0,sizeof(l));
        int label='a';
        for (int j=0; j<h; j++) {
            for (int k=0; k<w; k++) {
                int ll = paint(k,j,label);
                if (label == ll) {
                    label = ll+1;
                }
            }
        }
        printf ("Case #%d:\n", i);
        for (int j=0; j<h; j++) {
            printf("%c", l[j][0]);
            for (int k=1; k<w; k++) {
                printf(" %c", l[j][k]);
            }
            printf("\n");
        }
    }
}
