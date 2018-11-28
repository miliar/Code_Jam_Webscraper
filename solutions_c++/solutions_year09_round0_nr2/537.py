#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

vector<int> set_no;
vector<int> set_size;

void init(int n) {
    set_no.resize(n);
    set_size.assign(n, 1);
    for (int i = 0; i < n; i++) {
        set_no[i] = i;
    }
}

int get(int p) {
    while (p != set_no[p]) {
        p = set_no[p] = set_no[set_no[p]];
    }
    return p;
}

void unite(int s1, int s2) {
    s1 = get(s1);
    s2 = get(s2);
    if (s1 == s2)
        return;
    if (set_size[s1] > set_size[s2]) {
        set_no[s2] = s1;
    } else {
        set_no[s1] = s2;
    }
}

#define mp make_pair

int main(void) {
    int T;
    scanf("%d", &T);
    for (int testCase = 1; testCase <= T; testCase++) {
        printf("Case #%d:\n", testCase);
        int h, w;
        scanf("%d%d", &h, &w);
        vector< vector<int> > grid(h+2, vector<int> (w+2, 100000));
        for (int i = 1; i <= h; i++) {
            for (int j = 1; j <= w; j++) {
                scanf("%d", &grid[i][j]);
            }
        }
        init((h+1)*(w+1));
        for (int i = 1; i <= h; i++) {
            for (int j = 1; j <= w; j++) {
                pair< int, pair<int, int> > c =
                    min(min(mp(grid[i-1][j], mp(i-1, j)), mp(grid[i+1][j], mp(i+1, j))),
                    min(mp(grid[i][j-1], mp(i, j-1)), mp(grid[i][j+1], mp(i, j+1))));
                if (c.first < grid[i][j]) {
                    unite(i*w + j, c.second.first*w + c.second.second);
                }
            }
        }
        char curch = 'a';
        map<int, char> mic;
        for (int i = 1; i <= h; i++) {
            for (int j = 1; j <= w; j++) {
                int q = get(i*w + j);
                if (mic[q] == '\0')
                    mic[q] = curch++;
                printf("%c ", mic[q]);
            }
            printf("\n");
        }
    }
    return 0;
}
