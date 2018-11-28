/*
Coder: Vlad Dumitriu
Email: vladut[dot]mail[at]gmail[dot]com
Quote: 'He is no fool who gives what he cannot keep,
to gain what he cannot lose.' - Jim Eliot

*/

//INCLUDE FILES -  inspiration.h
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
const long double eps = 1e-7;
typedef long long LL;
typedef long double LD;
#define PB push_back
#define NP next_permutation
#define MP make_pair
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()
#define FORE(it, v) for (typeof((v).begin()) it = (v).begin(); it != (v).end(); ++it)
#define STERGE(v) memset(v,0,sizeof v)
template<class A, class B> A i2s(B x){stringstream s; s<<x; A r; s>>r;return r;} //i2s<string, int>(X)
typedef istringstream iss;
/////////////////////THE CODE BEGINS HERE ////////////////////////////////////////////////////////


void go();
int main() 
{
    freopen("file.in", "r", stdin);
    freopen("file.out", "w", stdout);
    int T;
    scanf("%d", &T);
    while (T--) go();
    //fclose(stdin);
    //getchar();
    return 0;
}

int Case = 0;
int DP[500][500];
int R[500][500];
void go() {
     int n, m;
     cin >> n >> m;
     STERGE(DP);
     STERGE(R);
     int r;
     cin >> r;
     while (r--) {
           int x, y;
           cin >> x >> y;
           R[x][y] = 1;
           }
     if (R[1][1] == 0) DP[1][1] = 1;
     int i, j;
     for (i = 1; i <= n; ++i)
     for (j = 1; j <= m; ++j) {
         if (R[i][j]) {DP[i][j] = 0; continue;}
         if (i - 1 >= 1 && j - 2 >= 1) DP[i][j] += DP[i-1][j-2];
         if (i - 2 >= 1 && j - 1 >= 1) DP[i][j] += DP[i-2][j-1];
         DP[i][j] %= 10007;
         }
     cout << "Case #" << ++Case << ": ";
     cout << DP[n][m] << '\n';
     }
