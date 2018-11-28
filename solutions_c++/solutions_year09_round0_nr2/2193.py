#include <cstdio>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <cstring>
#include <string>
using namespace std;


int main() {
    int t;
    scanf("%d", &t);
    for (int cas = 0; cas < t; cas++) {
        printf("Case #%d:\n", cas+1);
        int h, w;
        scanf("%d %d", &h, &w);
        vector<vector<int> > elev(w, h);
        for (int j = 0; j < h; j++) {
            for (int i = 0; i < w; i++) {
                scanf("%d", &elev[i][j]);
            }
        }
        
        vector<vector<int> > labels(w, h);
        vector<vector<pair<int, int> > > flowTo(w, h);
        int nl = 0;
        for (int i = 0; i < w; i++) {
            for (int j = 0; j < h; j++) {
                int delta = 0;
                if (j > 0) {
                    if (elev[i][j-1] < elev[i][j]) {
                        delta = elev[i][j] - elev[i][j-1];
                        flowTo[i][j] = make_pair(i, j-1);
                    }
                }
                if (i > 0) {
                    if ( (elev[i][j]- elev[i-1][j]) > delta ) {
                        delta = elev[i][j] - elev[i-1][j];
                        flowTo[i][j] = make_pair(i-1, j);
                    }
                }
                if (i < w-1) {
                    if ( (elev[i][j] - elev[i+1][j]) > delta) {
                        delta = elev[i][j] - elev[i+1][j];
                        flowTo[i][j] = make_pair(i+1, j);
                    }
                }
                if (j < h-1) {
                    if ((elev[i][j] - elev[i][j+1]) > delta) {
                        delta = elev[i][j] - elev[i][j+1];
                        flowTo[i][j] = make_pair(i, j+1);
                    }
                }
                if (delta == 0) {
                    flowTo[i][j] = make_pair(-1, -1);
                    labels[i][j] = ++nl;
                }
            }
        }
        
        bool done = false;
        while (!done) {
            done = true;
            for (int i = 0; i < w; i++) {
                for (int j = 0; j < h; j++) {
                    if (!labels[i][j] && labels[flowTo[i][j].first][flowTo[i][j].second]) {
                        labels[i][j] = labels[flowTo[i][j].first][flowTo[i][j].second];
                        done = false;
                    }
                }
            }
        }

        vector<char> labelMap(27);
        char next = 'a';
        for (int j = 0; j < h; j++) {
            for (int i = 0; i < w; i++) {
                if (!labelMap[labels[i][j]]) {
                    labelMap[labels[i][j]] = next++;
                }
                printf("%s%c", i ? " " : "", labelMap[labels[i][j]]);
            }
            printf("\n");
        }
    }
}
