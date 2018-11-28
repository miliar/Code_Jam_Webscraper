#include <cstring>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <map>
using namespace std;

char dict[10000][11];
int n;

int g, *p, *q, group1[10000], group2[10000], score[10000], pat[10000];
bool nonzero[1000];
map<int, int> allocid[10000];

void initgroup() {
    p = group1;
    q = group2;
    g = 0;
    for (int i = 0; i < n; ++i) {
        int l = strlen(dict[i]);
        if (allocid[0].find(l) != allocid[0].end()) group1[i] = allocid[0][l];
        else {
            allocid[0][l] = g;
            group1[i] = g++;
        }
        score[i] = 0;
    }
    allocid[0].clear();
}

inline int pattern(const char *s, char ch) {
    int rtn = 0;
    for (; *s; ++s) {
        if (*s == ch) rtn |= 1;
        rtn <<= 1;
    }
    return rtn;
}

bool move(char ch) {
    bool rtn = false;
    int ng = 0;
    for (int i = 0; i < g; ++i)
        nonzero[i] = false;
    for (int i = 0; i < n; ++i) {
        int gid = p[i];
        pat[i] = pattern(dict[i], ch);
        if (pat[i] != 0) nonzero[gid] = true;
        if (allocid[gid].find(pat[i]) != allocid[gid].end()) {
            q[i] = allocid[gid][pat[i]];
            rtn = true;
        }
        else {
            allocid[gid][pat[i]] = ng;
            q[i] = ng++;
        }
    }
    for (int i = 0; i < n; ++i)
        if (pat[i] == 0 && nonzero[p[i]])
            ++score[i];
    for (int i = 0; i < g; ++i)
        allocid[i].clear();
    g = ng;
    int *tmp = p;
    p = q;
    q = tmp;
    return rtn;
}

int main() {
    FILE *fin = fopen("B-small-attempt0.in", "r");
    FILE *fout = fopen("out.txt", "w");
    int t;
    fscanf(fin, "%d", &t);
    for (int i = 1; i <= t; ++i) {
        fprintf(fout, "Case #%d:", i);
        int m;
        char tmp[27];
        fscanf(fin, "%d%d", &n, &m);
        for (int j = 0; j < n; ++j)
            fscanf(fin, "%s", dict[j]);
        for (int j = 0; j < m; ++j) {
            fscanf(fin, "%s", tmp);
            initgroup();
            for (int k = 0; k < 26; ++k)
                if (!move(tmp[k])) break;
            int max = -1, pos;
            for (int k = 0; k < g; ++k)
                if (score[k] > max) {
                    max = score[k];
                    pos = k;
                }
            fprintf(fout, " %s", dict[pos]);
        }
        fprintf(fout, "\n");
    }
    fclose(fout);
    fclose(fin);
    return 0;
}
