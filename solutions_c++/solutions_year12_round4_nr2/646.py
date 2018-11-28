#include<iostream>
#include<queue>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<string>
#include<cstring>
#include<map>
#include<numeric>
#include<sstream>
#include<cmath>
using namespace std;
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define pb push_back
#define f(i,x,y) for(int i = x; i<y; i++ )
#define FOR(it,A) for(typeof A.begin() it = A.begin(); it!= A.end(); it++)
#define quad(x) (x) * (x)
#define mp make_pair
#define clr(x, y) memset(x, y, sizeof x)
#define fst first
#define snd second
typedef pair<int, int> pii;
typedef long long ll;
typedef long double ld;
#define inf (1 << 30)
int r[10000];
double x[10000], y[10000];
int W, L; int n;
double eps = 1e-9;
void mete(int lado, double d, int i){
   if(lado == 0) x[i] = 0, y[i] = d;
   if(lado == 1) x[i] = d, y[i] = L;
   if(lado == 2) x[i] = W, y[i] = L - d;
   if(lado == 3) x[i] = W - d, y[i] = 0;
}
int aux = 9999;
double dist(int lado, double d, int j){
   int i = aux;
   if(lado == 0) x[i] = 0, y[i] = d;
   if(lado == 1) x[i] = d, y[i] = L;
   if(lado == 2) x[i] = W, y[i] = L - d;
   if(lado == 3) x[i] = W - d, y[i] = 0;
   return hypot(x[j] - x[i], y[j] - y[i]);
}
int main(){
   int tt; cin >> tt;
   f(caso, 1, tt + 1){
      cin >> n >> W >> L;
      f(i, 0, n) scanf("%d", r + i);
      printf("Case #%d:", caso);
      int lado = 0;
      f(i, 0, n) x[i] = -1;
      f(i, 0, n){
         double le = 0, ri = lado % 2 == 0 ? L : W;
            while(fabs(le - ri) > eps){
               double me = (le + ri) / 2;
               bool puede = true;
               f(j, 0, i) if(dist(lado, me, j) < r[j] + r[i]) puede = false;
               if(puede) ri = me;
               else le = me;
            }
            bool puede = true;
            f(j, 0, i) if(dist(lado, ri, j) < r[j] + r[i]) puede = false;
            if(!puede){
               i--; lado++; continue;
            }
            mete(lado, ri, i);
      }
      f(i, 0, n) f(j, 0, n) if(i != j && hypot(x[i] - x[j], y[i] - y[j]) < r[i] + r[j]){
         cout << "MAL" << endl;
         return 0;
      }
      f(i, 0, n) if(x[i] < 0 || x[i] > W || y[i] > L){
         cout << "MAL2" << endl;
         return 0;
      }
      f(i, 0, n) printf(" %.12f %.12f", x[i], y[i]);
      cout << endl;
   }
}

