/*
 * Author: momodi
 * Created Time:  2009/9/13 0:05:03
 * File Name: b.cpp
 * Description: 
 */
#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>
#include <cstdlib>
#include <algorithm>
using namespace std;
#define out(x) fprintf(stderr, "%s: %I64d\n", #x, (long long)(x))
#define SZ(v) ((int)(v).size())
const int maxint=-1u>>1;
template <class T> bool get_max(T& a, const T &b) {return b > a? a = b, 1: 0;}
template <class T> bool get_min(T& a, const T &b) {return b < a? a = b, 1: 0;}
int main() {
    int ca;
    scanf("%d", &ca);
    for (int cc = 1; cc <= ca; ++cc) {
        char buf[100];
        scanf("%s", buf);
        vector<int> a;
        a.push_back(0);
        for (char *p = buf; *p; ++p) {
            a.push_back(*p - '0');
        }
        next_permutation(a.begin(), a.end());
        reverse(a.begin(), a.end());
        while (SZ(a) > 1 && a.back() == 0) {
            a.pop_back();
        }
        reverse(a.begin(), a.end());
        printf("Case #%d: ", cc);
        for (int i = 0; i < SZ(a); ++i) {
            printf("%d", a[i]);
        }
        puts("");
    }
    return 0;
}

