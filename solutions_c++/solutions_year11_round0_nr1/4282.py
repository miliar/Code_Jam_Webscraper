/*
 * Author: momodi
 * Created Time:  2010/5/8 19:00:54
 * File Name: a.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <sstream>
#include <string>
#include <map>
#include <set>
#include <vector>
using namespace std;
#define out(v) cerr << #v << ": " << (v) << endl
#define SZ(v) ((int)(v).size())
const int maxint = -1u>>1;
template <class T> bool get_max(T& a, const T &b) {return b > a? a = b, 1: 0;}
template <class T> bool get_min(T& a, const T &b) {return b < a? a = b, 1: 0;}
#define take(a, b) (((a) >> (b)) & 1)
#define move(v) (1 << (v))

int main() {
    int ca;
    scanf("%d", &ca);
    for (int cc = 1; cc <= ca; ++cc) {
        printf("Case #%d: ", cc);
        int n;
        scanf("%d", &n);
        int Op = 1, Bp = 1;
        int Ot = 0, Bt = 0;
        int res = 0;
        for (int i = 0; i < n; ++i) {
            char s[10];
            int p;
            scanf("%s %d", s, &p);
            if (*s == 'O') {
                get_max(res, Ot + abs(p - Op));
                Op = p;
                ++res;
                Ot = res;
            } else {
                get_max(res, Bt + abs(p - Bp));
                Bp = p;
                ++res;
                Bt = res;
            }
            //out(res);
        }
        printf("%d\n", res);
    }
    return 0;
}

