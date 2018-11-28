/**********************************************************************
Author: chaeyeon
Created Time:  Sat 26 Jul 2008 09:53:48 AM CST
Modified Time: Sat 26 Jul 2008 10:44:51 AM CST
File Name: c.cpp
Description: 
**********************************************************************/
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std;
#define out(x) printf("%s: %lld\n", #x, (long long)(x))
const int maxint=0x7FFFFFFF;
template <class T> void get_max(T& a, const T &b) {b > a? a = b:1;}
template <class T> void get_min(T& a, const T &b) {b < a? a = b:1;}
int a[] = {
    5, 
    27, 
    143, 
    751,
    935,
    607,
    903,
    991,
    335,
    47,
    943,
    471,
    55,
    447, 
    463, 
    991, 
    95, 
    607, 
    263, 
    151,
    855,
    527,
    743,
    351,
    135,
    407,
    903,
    791,
    135,
    647 
};
int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        int k;
        scanf("%d", &k);
        printf("Case #%d: %03d\n", t, a[k - 1]);
    }
    return 0;
}

