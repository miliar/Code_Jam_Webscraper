#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>

#include <string>
#include <vector>
#include <queue>
#include <list>
#include <map>
#include <set>
#include <algorithm>

#define INFINITO 0x3f3f3f3f

using namespace std;

#define MAX 128

int pai[MAX * MAX];
int altura[MAX][MAX];
int r, c;

int gera (int x, int y) {
    return MAX * x + y;
}

int find (int x) {
    int tmp = x;

    while (x != pai[x])
        x = pai[x];
    int resp = x;

    x = tmp;
    while (x != pai[x]) {
        tmp = x;
        x = pai[x];
        pai[tmp] = resp;
    }

    return resp;
}

void do_union (int x, int y) {
    pai[find(x)] = find(y);
}

int delta[4][2] = {
    {-1, 0},
    { 0,-1},
    { 0, 1},
    { 1, 0}
};

void rec (int x, int y) {

    int i;
    int menor = INFINITO;
    int xe=x, ye=y;

    for (i=0; i<4; ++i) {
        int nx = x + delta[i][0];
        int ny = y + delta[i][1];

        if (nx>=0 and ny>=0 and nx<r and ny<c and altura[nx][ny] < altura[x][y] and altura[nx][ny] < menor) {
            menor = altura[nx][ny];
            xe = nx, ye = ny;
        }
    }

    if (xe == x and ye == y)
        return;

    if (find(gera(xe,ye)) == gera(xe,ye)) {
        do_union(gera(x,y), gera(xe,ye));
        rec(xe,ye);
    }
    else
        do_union(gera(x,y), gera(xe,ye));
}

int main (void) {

    int caso = 1;
    int casos;
    int i, j, x;

    scanf("%d", &casos);

    while (casos--) {
        scanf("%d %d", &r, &c);

        for (i=0; i<r; ++i)
            for (j=0; j<c; ++j) {
                scanf("%d", &altura[i][j]);
                
                x = gera(i,j);
                pai[x] = x;
            }

        for (i=0; i<r; ++i) {
            for (j=0; j<c; ++j) {
                x = gera(i,j);
                if ( find(x) != x )
                    continue;
                else
                    rec(i,j);
            }
        }

        char id = 'a';
        map<int, char> dict;

        printf("Case #%d:\n", caso++);

        for (i=0; i<r; ++i) {
            for (j=0; j<c; ++j) {

                if (j)
                    putchar(' ');

                x = gera(i,j);
                if ( ! dict[find(x)] )
                    dict[find(x)] = id++;

                printf("%c", dict[find(x)]);
            }
            putchar('\n');
        }
    }

    return 0;
}
