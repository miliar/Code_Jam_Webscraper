#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <numeric>
using namespace std;
#define pb push_back
#define forn(i,n) for(int i=0; i<(n); i++)
int myadd(int a, int b) {return a ^ b;}
int myadd2(int a, int b) {return a + b;}

int main() {
    freopen("C-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int ncase; scanf("%d", &ncase);
    forn(icase, ncase) {
           int n; scanf("%d", &n);
           vector<int> a(n);
           forn(i, n) scanf("%d", &a[i]);
           sort(a.begin(),a.end());
           int mask = accumulate(a.begin(), a.end(), 0, myadd);
           int sum = accumulate(a.begin(), a.end(), -a[0], myadd2);    
           printf("Case #%d: ", icase+1);
           if(mask) printf("NO\n");
           else printf("%d\n", sum);
    }
}
