#include <algorithm>
#include <vector>
#include <string>
#include <deque>
#include <queue>
#include <map>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
using namespace std;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef vector<double> vd;
typedef queue<int> qi;

#define fori(i, n) for(i=0;i<n;i++)
#define fordi(i, n) for(int i=0;i<n;i++)
#define INF 0x7fffffff

char sc() {char r; if (scanf("%c", &r) != 1) {printf("-1"); exit(0);} return r;}
int si() {int r; if (scanf("%d", &r) != 1) {printf("-1"); exit(0);} return r;}
long long sli() {long long r; if (scanf("%lld", &r) != 1) {printf("-1"); exit(0);} return r;}
double sf() {double r; if (scanf("%lf", &r) != 1) {printf("-1"); exit(0);} return r;}

bool divall(int x,vi &f) {
    fordi(i,f.size())
        if ( x % f[i] != 0 && f[i] % x !=0) return false;
    return true;

}


main() {
    int t=si();
    fordi(ii,t) {
        printf("Case #%d: ", ii+1);
        int n=si(),l=si(),h=si();
        vi freq;
        freq.resize(n);
        fordi(j,n) freq[j]=si();
        int j;
        for(j=l;j<=h;j++) {
            if (divall(j,freq)) {
                printf("%d\n",j);
                break;
            }

        }
        if (j==h+1)
            printf("NO\n");
    }
}
