#include <stdio.h>
#include <string.h>
#include <limits.h>
#include <math.h>
#include <stdlib.h>
#include <ctype.h>
#include <assert.h>

#define FOR(c, m) for(int c=0;c<(m);c++)
#define FORE(c, f, t) for(int c=(f);c<(t);c++)

#define FENCE 10000

struct {
    int colorCount;
    int colors[300];
} fence[FENCE], paintedColors;

struct {
    char name[100];
} colors[300];


int totalColors;

struct {
    int color;
    int first;
    int last;
} offers[300];

int n;

int addColor(char * color) {
    FOR(i, totalColors) {
        if (!strcmp(color, colors[i].name)) {
            return i;
        }
    }
    strcpy(colors[totalColors].name, color);
    return totalColors++;
}

void addFence(int pos, int color) {
    FOR(i, fence[pos].colorCount) {
        if (fence[pos].colors[i] == color) return;
    }
    fence[pos].colors[fence[pos].colorCount] = color;
    fence[pos].colorCount++;
}


void addPaintedColor(int color) {
    FOR(i, paintedColors.colorCount)
        if (paintedColors.colors[i] == color) return;
    paintedColors.colors[paintedColors.colorCount] = color;
    paintedColors.colorCount++;
    //printf("Added painted color %d\n", color);
}

int main(void) {
    int cases;
    scanf("%d", &cases);
    for(int c=1;c<=cases;c++) {
        scanf("%d", &n);
        totalColors = 0;
        FOR(i, n) {
            char color[100];
            scanf("%s %d %d", color, &offers[i].first, &offers[i].last);
            offers[i].first--;
            offers[i].last--;
            offers[i].color = addColor(color);
            //printf("Setting color %d\n", offers[i].color);
        }

        //printf("Total colors: %d\n", totalColors);

        int min = INT_MAX;
        FOR(i, 1<<n) {
            FOR(j, FENCE) fence[j].colorCount = 0;
            paintedColors.colorCount = 0;
            int x = i;
            int pos = 0;
            int totalOffers = 0;
            while (x) {
                if ((x&1) != 0) {
                    FORE(k, offers[pos].first, offers[pos].last + 1) {
                        addFence(k, offers[pos].color);
                    }
                    totalOffers++;
                    addPaintedColor(offers[pos].color);
                }
                pos++;
                x >>= 1;
            }

            bool ok = true;
            FOR(j, FENCE) {
                if (fence[j].colorCount == 0 || fence[j].colorCount > 3) {
                    ok = false;
                    //printf("Error on %d, count %d\n", j, fence[j].colorCount);
                    break;
                }
            }
            //printf("Testing %d, offers %d\n", i, totalOffers);
            //printf("Painted colors %d\n", paintedColors.colorCount);

            if (ok && totalOffers < min && paintedColors.colorCount <= 3) min = totalOffers;
        }

        printf("Case #%d: ", c);
        if (min != INT_MAX) printf("%d\n", min); else printf("IMPOSSIBLE\n");
    }
}
