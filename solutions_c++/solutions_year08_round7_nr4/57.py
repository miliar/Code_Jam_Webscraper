/*###################START INCLUDE-urile#########################/*/
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
#include <fstream>
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

/*###################STOP INCLUDE-urile#########################/*/
using namespace std;
/*######################START PRECODE#############################*/
const long double eps = 1e-7; // marja de eroare
const long double pi=acos(-1.0);//valoarea lui PI
typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;
typedef pair<int,int> PII;
#define PB push_back  //vector<> v.PB(X);
#define NP next_permutation //v.NP()
#define MP make_pair //MP
#define X first //.X 
#define Y second //.Y
#define ALL(a) (a).begin(), (a).end() //sort(ALL(v))
#define RALL(a) (a).rbegin(), (a).rend()//sort(RALL(v)) //sens invers
#define FORIT(it, v) for (typeof((v).begin()) it = (v).begin(); it != (v).end(); ++it) //parcurg cu iteratoru//FORIT(it, V) {cout << *it << '\n';}
#define STERGE(v) memset(v,0,sizeof v) //set 0 on something
#define INF 0x3f3f3f3f
#define STERGEI(v) memset(v,0x3f, sizeof(v)) //set cu infinit
//memcmp
typedef stringstream iss; //iss f(string); f>>X; sau f << X;//sau de output
/*#####################TEMPLATES##################################*/

template<class A, class B> inline A i2s(B x){stringstream s; s<<x; A r; s>>r;return r;} //string x = i2s<string, int>(X);
template<class A> inline A abs(A a) {if (a < 0) return -a; return a;} //
//__gcd(A, B) - euclidu
template<class A> inline A euclid(A a, A b, A &x, A &y) {
               if (!b) {x=1, y = 0; return a;} 
               A ret = euclid(b, a%b, x, y);
               A aux = x; 
               x = y; y = aux - (a/b)*y;
               return ret;
               } ///euclid(556, 21, A, B); si A * 556 + B * 21 = gcd-ul
//de verificad daca e prim
template<class A> inline int isPrime(A X) {
               if (X <= 1 || (X % 2 == 0 && X != 2)) return 0;
               for (A i = 3; i * i <= X; i+=2) if (X % i == 0) return 0;
               return 1;
               } ///isPrime(22531);

/*######################STOP PRECODE#############################*/
void go_fish();
int main() { 
      freopen("4.in", "r", stdin);freopen("4.out", "w", stdout);
//    freopen("4-small.in", "r", stdin);freopen("4-small.out", "w", stdout);
//    freopen("4-large.in", "r", stdin);freopen("4-large.out", "w", stdout);
    int ceamailungavariabila;
    int ceamailungavariabila2 = 1;
    for (scanf("%d\n", &ceamailungavariabila); ceamailungavariabila--;) {
        printf("Case #%d: ", ceamailungavariabila2++);
        go_fish();
        }
    }
int n, m;
int get_bit(int x, int y) {
    return x * m + y;
    }
map<int, int> M[4][4];
int dy[] = {0, 0, 1, -1, 1,-1,  1, -1};
int dx[] = {1,-1, 0,  0, 1, 1, -1, -1};
int go(int x, int y, int msk) {
    if (msk & (1 << get_bit(x, y))) return 1;
    if (M[x][y][msk]) return M[x][y][msk] - 1;
    //make a move    
    for (int d = 0; d < 8; ++d) {
        int mx = x + dx[d], my = y + dy[d];
        if (mx < 0 || my < 0 || mx >= n || my >= m) continue;
        //acopera
        int msk2 = msk;
        msk2|=(1 << get_bit(x, y));
        if (msk & (1 << get_bit(x, y))) continue;
        if (!go(mx, my, msk2)) {
                    M[x][y][msk] = 2;
                   // cout << x << ' ' << y <<' ' << msk << ' ' << 1 << '\n';
                    return 1;
                    }
        }
    M[x][y][msk] = 1;
    return 0;
    }
void go_fish() {
     cin >> n >> m;
     int i, j;
     int msk = 0;
     int ax, ay;
     for (i = 0; i < n; ++i)
     for (j = 0; j < m; ++j) {
         M[i][j].clear();
         char c;
         cin >> c;
         if (c == 'K') {c = '.'; ax = i; ay = j;}
         if (c == '#')  { msk|=(1 << get_bit(i, j));
         
         }
         }
     if (go(ax, ay, msk)) cout << "A\n";
     else cout << "B\n";
     }
