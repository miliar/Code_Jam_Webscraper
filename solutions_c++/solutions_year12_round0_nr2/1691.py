#include <cstdio>
#include <cstring>
#include <cctype>
#include <climits>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <cstdarg>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <sstream>
#include <exception>
#include <stdexcept>
#include <memory>
#include <locale>
#include <bitset>
#include <deque>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <vector>
#include <algorithm>
#include <iterator>
#include <functional>
#include <string>
#include <complex>
#include <valarray>

#define rep(i, n) for (int i = 0; i < n; ++ i)
#define mp make_pair
#define pb push_back
#define x first
#define y second
#define ll long long
#define cmplxd complex <long double>
#define pi 3.14159265358979323846264338327950288


using namespace std;

const int maxn = 101 + 10;

int ntest;
int n,s,p;
int t[maxn];
int f[maxn][maxn];

int check(int num,int dis) {

    if (num < p) return 0;
    if (num >= 3*p) return 1;

    num = num - p;

    if (num %2 == 1) {

        int num1 = (num+1)/2;
        int num2 = (num-1)/2;
        if ( (abs(p-num1)<=dis) && (abs(p-num2)<=dis) ) return 1;

    } else {
        if ( abs(p - num/2) <= dis ) return 1;

        if (num >=2 && dis == 2) {
            int num1 = (num+2)/2;
            int num2 = num - num1;
            if ( (abs(p-num1)<=1) && (abs(p-num2)<=1) ) return 1;
        }
    }

    return 0;
}

int main() {

    freopen("B-large.in","r",stdin);
    freopen("B.txt","w",stdout);

    cin >> ntest;

    for(int test=0; test<ntest; test++) {
        cin >> n >> s >> p;
        for(int i=1; i<=n; i++) {
            cin >> t[i];
            //cout << t[i] << " ";
        }

        memset(f,0,sizeof(f));

        for(int i=1; i<=n; i++)
         for(int j=0; j<=min(i,s); j++) {
                f[i][j]   = max( (f[i-1][j] + check(t[i],1)) ,f[i][j]);
                f[i][j+1] = max( (f[i-1][j] + check(t[i],2)) ,f[i][j+1]);
         }

         cout << "Case #" << test+1 << ": ";
         cout << f[n][s] << endl;
    }

    return 0;
}
