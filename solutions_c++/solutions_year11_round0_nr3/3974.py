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
        int sum = 0;
        int tot_xor = 0;
        vector<int> dt;
        map<int, int> dpa, dpb;
        dpa[0] = 0;
        for (int i = 0; i < n; ++i) {
            int v;
            scanf("%d", &v);
            sum += v;
            tot_xor ^= v;
            dpb = dpa;
            for (map<int, int>::iterator it = dpa.begin(); it != dpa.end(); ++it) {
                get_max(dpb[it->first ^ v], it->second + v);
            }
            dpa.swap(dpb);
        }
        int res = 0;
        for (map<int, int>::iterator it = dpa.begin(); it != dpa.end(); ++it) {
            if (((it->first) ^ (it->first)) == tot_xor && it->second != 0 && it->second != sum) {
                get_max(res, it->second);
            }
        }
        if (res == 0) {
            printf("NO\n");
        } else {
            printf("%d\n", res);
        }
    }
    return 0;
}


