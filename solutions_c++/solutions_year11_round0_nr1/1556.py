/*
 * Author: WHHeV
 * Created Time:  2011/5/7 9:52:53
 * File Name: F:\Dropbox\Dropbox\Programs\GCJ2011\a.cpp
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

struct sequence {
    bool co;
    int bu;
    int di;
} seq[110];

int T, N;
int a[110], b[110];

int main() {
    freopen("A-large.in", "r", stdin);
freopen("A-large.out", "w", stdout);

    scanf("%d", &T);
    int ca = 0;
    while (T--) {
        ca++;
        scanf("%d", &N);
        int na = 1, nb = 1;
        a[0] = 1, b[0] = 1;
        int pa = 1, pb = 1, numa = -1, numb = -1;
        for (int i = 0; i < N; i++) {
            char ch;
            scanf("%c", &ch);
            scanf("%c", &ch);
            if (ch == 'O') {
                seq[i].co = 0;
                scanf("%d", &seq[i].bu);
                if (numa < 0) {
                    numa = i;
                }
                else if (seq[i].bu >= seq[numa].bu) {
                    seq[numa].di = 1;
                    numa = i;
                } else {
                    seq[numa].di = -1;
                    numa = i;
                }
                //scanf("%d", &a[na++]);
            } else {
                seq[i].co = 1;
                scanf("%d", &seq[i].bu);
                if (numb < 0)
                    numb = i;
                else if (seq[i].bu >= seq[numb].bu) {
                    seq[numb].di = 1;
                    numb = i;
                } else {
                    seq[numb].di = -1;
                    numb = i;
                }
                //scanf("%d", &b[nb++]);
            }
            //scanf("%d", &seq[i].bu);
        }
        //int sum1 = 0, sum2 = 0;
        //for (int i = 1; i < na; i++) {
            //sum1 += abs(a[i] - a[i-1]);
        //}
        //sum1 += (na - 1);
        //for (int i = 1; i < nb; i++) {
            //sum2 += abs(b[i] - b[i-1]);
        //}
        //sum2 += (nb - 1);
        int po1 = 1, po2 = 1, but = 0, time = 0, di1 = 1, di2 = 1;
        while (but < N) {
            time++;
            //po1++; po2++;
            //printf("%d %d\n", po1, po2);
            if (!seq[but].co) {
                if (di1 == 1 && po1 >= seq[but].bu) {
                    po1 = seq[but].bu;
                    di1 = seq[but].di;
                    po2 += di2;
                    but++;
                } else if (di1 == -1 && po1 <= seq[but].bu) {
                    po1 = seq[but].bu;
                    di1 = seq[but].di;
                    po2 += di2;
                    but++;
                } else {
                    po1 += di1;
                    po2 += di2;
                }
            } else {
                if (di2 == 1 && po2 >= seq[but].bu) {
                    di2 = seq[but].di;
                    po2 = seq[but].bu;
                    po1 += di1;
                    but++;
                } else if (di2 == -1 && po2 <= seq[but].bu) {
                    po2 = seq[but].bu;
                    di2 = seq[but].di;
                    po1 += di1;
                    but++;
                } else {
                    po1 += di1;
                    po2 += di2;
                }
            }
        }
        printf("Case #%d: %d\n", ca, time);
    }
    return 0;
}

