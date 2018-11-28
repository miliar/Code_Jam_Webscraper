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
    freopen("A.in", "r", stdin);
    freopen("file.out", "w", stdout);
    int T;
    scanf("%d", &T);
    while (T--) go();
    //fclose(stdin);
    //getchar();
    return 0;
}

int Case = 0;
int DP[20000][2];
int OP[20000];
int OP2[20000];
int tree[20000];
void go() {
     int M, V;
     cin >> M >> V;
     int i, j, k;
     for (i = 0; i < (M-1)/2; ++i) {
         int X;
         cin >> X;
         if (X!= 1) X = 0;
         OP[i+1] = X; // 1 AND 0 OR
         cin >> X;
         if (X != 1) X = 0;
         OP2[i+1] = X; //1 daca se schimba
         }
     j = M - (M+1)/2 + 1;
     for (; j<= M; ++j) {
         int X;
         cin >> X;
         if (X != 1) X = 0;
         DP[j][X] = 0;
         DP[j][(X+1)%2] = -1;
         }
     j = M - (M+1)/2;
     for (; j >= 1; --j) {
         int p1, p2;
         DP[j][0] = DP[j][1] = -1;
         for (p1 = 0; p1 <= 1; ++p1)
         for (p2 = 0; p2 <= 1; ++p2) if (DP[j*2][p1] != -1 && DP[j*2+1][p2] != -1) {
             int R = p1;
             if (OP[j] == 1) R = p1 & p2;
             else R = p1 | p2;
             if (DP[j][R] == -1 || DP[j][R] > DP[j*2][p1] + DP[j*2+1][p2]) DP[j][R] = DP[j*2][p1] + DP[j*2+1][p2];
             R = p1;
             if (OP2[j] != 1) continue;
             if (OP[j] == 1) R = p1 | p2;
             else R = p1 & p2;
             if (DP[j][R] == -1 || DP[j][R] > DP[j*2][p1] + DP[j*2+1][p2] + 1) DP[j][R] = DP[j*2][p1] + DP[j*2+1][p2] + 1;
             }
         }

     cout << "Case #" << ++Case << ": ";
     if (DP[1][V] == -1) cout << "IMPOSSIBLE\n";
     else     cout << DP[1][V] << '\n';
     
     }
