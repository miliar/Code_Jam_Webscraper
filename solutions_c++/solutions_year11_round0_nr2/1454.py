/*
 * Author: WHHeV
 * Created Time:  2011/5/7 11:49:35
 * File Name: b.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std;
#define out(v) cerr << #v << ": " << (v) << endl
#define SZ(v) ((int)(v).size())
const int maxint = -1u>>1;
template <class T> bool get_max(T& a, const T &b) {return b > a? a = b, 1: 0;}
template <class T> bool get_min(T& a, const T &b) {return b < a? a = b, 1: 0;}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T, C, D, N;
    int al[26];
    int ca = 0;
    char co[40][5];
    char op[30][5];
    char s[110];
    int slen;
    scanf("%d", &T);
    while (T--) {
        memset(co, 0, sizeof(co));
        memset(op, 0, sizeof(op));
        memset(s, 0, sizeof(s));
        ca++;
        scanf("%d", &C);
        for (int i = 0; i < C; i++) {
            scanf("%s", co[i]);
        }
        scanf("%d", &D);
        for (int i = 0; i < D; i++) {
            scanf("%s", op[i]);
        }
        scanf("%d", &slen);
        scanf("%s", s);
        memset(al, 0, sizeof(al));
        char ma[110];
        int len = 0;
        //for (int i = 0; i < C; i++) {
            //printf("%s\n", co[i]);
        //}
        //for (int i = 0; i < D; i++) {
            //printf("%s\n", op[i]);
        //}
        //printf("%s", s);
        for (int i = 0; i < slen; i++) {
            ma[len++] = s[i];
            al[s[i] - 'A']++;
            while (len > 1) {
                bool flag = 0;
                for (int j = 0; j < C; j++) {
                    if ((ma[len-2] == co[j][0] && ma[len-1] == co[j][1]) || (ma[len-1] == co[j][0] && ma[len-2] == co[j][1])) {
                        flag = 1;
                        al[ma[len-1] - 'A']--;
                        al[ma[len-2] - 'A']--;
                        al[co[j][2] - 'A']--;
                        ma[len-2] = co[j][2];
                        len--;
                        break;
                    }
                }
                if (!flag) break;
            }
            for (int j = 0; j < D; j++) {
                if (al[op[j][0] - 'A'] > 0 && al[op[j][1] - 'A'] > 0) {
                    len = 0;
                    memset(al, 0, sizeof(al));
                    break;
                }
            }
            //for (int j = 0; j < len; j++)
                //printf("%c ", ma[j]);
            //printf("\n");
        }
        printf("Case #%d: [", ca);
        for (int i = 0; i < len; i++) {
            if (i < len - 1)
                printf("%c, ", ma[i]);
            else
                printf("%c", ma[i]);
        }
        printf("]\n");
    }
    return 0;
}

