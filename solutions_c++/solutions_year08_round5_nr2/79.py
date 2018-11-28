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
int n, m;
vector<string> v;
int px, py;
int cx, cy;
int DP[500][500];
int INF = 9999999;
void go() {
     v.resize(0);
     v.clear();
     cin >> n >> m;
     scanf("\n");
     int i, j;
     for (i = 0; i < n; ++i) {
         string line;
         cin >> line;
       
         v.PB(line);
         }
     //X cacke, O eu
     for (i = 0; i < n; ++i)
     for (j = 0; j < m; ++j) {
         
         if (v[i][j] == 'O') {v[i][j] = '.'; px = i; py = j;}
         if (v[i][j] == 'X') {v[i][j] = '.'; cx = i; cy = j;}
         
         }
       
     for (i = 0; i < n; ++i) for (j = 0; j < m; ++j) DP[i][j] = INF;
     DP[px][py] = 0;

     while (1) {
           int ok = 0;
           for (i = 0; i < n; ++i) 
           for (j = 0; j < m; ++j) if (DP[i][j] < INF && v[i][j] == '.') {
               int mx = i, my = j, Mx = i, My = j;
               while (mx >= 0 && v[mx][j] == '.') {mx--;}++mx;
               while (my >= 0 && v[i][my] == '.') {my--;}++my;
               while (Mx < n && v[Mx][j] == '.') {Mx++;} Mx--;
               while (My < m && v[i][My] == '.') {My++;} My--;
               int d = abs(i - mx);
               d <?= abs(i - Mx);
               d <?= abs(j - my);
               d <?= abs(j - My);
               d++;
               if (DP[mx][j] > DP[i][j] + d) {ok = 1; DP[mx][j] = DP[i][j] + d;}
               if (DP[Mx][j] > DP[i][j] + d) {ok = 1; DP[Mx][j] = DP[i][j] + d;}
               if (DP[i][my] > DP[i][j] + d) {ok = 1; DP[i][my] = DP[i][j] + d;}
               if (DP[i][My] > DP[i][j] + d) {ok = 1; DP[i][My] = DP[i][j] + d;}
               d = 1;
               mx = max(mx, i-1);
               my = max(my, j-1);
               My = min(My, j + 1);
               Mx = min(Mx, i + 1);
               if (DP[mx][j] > DP[i][j] + d) {ok = 1; DP[mx][j] = DP[i][j] + d;}
               if (DP[Mx][j] > DP[i][j] + d) {ok = 1; DP[Mx][j] = DP[i][j] + d;}
               if (DP[i][my] > DP[i][j] + d) {ok = 1; DP[i][my] = DP[i][j] + d;}
               if (DP[i][My] > DP[i][j] + d) {ok = 1; DP[i][My] = DP[i][j] + d;}
               }
           if (ok == 0) break;
           }
     cout << "Case #" << ++Case << ": ";
     if (DP[cx][cy] >= INF) cout << "THE CAKE IS A LIE\n";
     else cout << DP[cx][cy] << '\n';
     }
