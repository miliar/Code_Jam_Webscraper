#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <complex>
#include <cstdio>
#include <cassert>
#include <cmath>
#include <numeric>

#define DEBUG(x) cerr << '>' << #x << ": " << x << endl;
#define CLEAR(x,c) memset(x,c,sizeof(x))
#define FOR(i,a,b) for(int i=(a),_b=(b);i<_b;i++)
#define FORM(it,v) for( typeof((v).begin()) it = (v).begin(); it != (v).end(); ++it )
#define FORD(i,a,b) for(int i=(b)-1,_b=(a);i>=_b;i--)
#define FORF(i,a,b,c) for(double i=(a),_b=(b);i<_b;i+=c)
#define sz size()
#define mp make_pair
#define X first
#define Y second
#define pb push_back
#define SORT(x) sort(all(x))
#define REVERSE(x) reverse(all(x))
#define CLEAR(x,c) memset(x,c,sizeof(x))
#define all(x) (x).begin(),(x).end()

#define pi acos(-1.)
#define eps 1e-7
#define aprox(a,b) (fabs((a)-(b))<eps)
#define FIND_MAX(type) (type)(~(1 << ((sizeof(type) * 8) - 1)))

template<typename T> inline T sqr(T a) { return a*a; }
template<typename T> inline int Size(const T& c) { return (int)c.size(); }
template<typename T> inline void checkMin(T& a, T b) { if (b < a) a = b; }
template<typename T> inline void checkMax(T& a, T b) { if (b > a) a = b; }
template<typename T> inline bool isSet(T number, int bit) { return (number&(T(1)<<bit)) != 0; }
template<class T> T abs(T x){return x>0 ? x:(-x);}

using namespace std;

 template<typename T, typename S> T cast(S s) {
    stringstream ss;
    ss << s;
    T res;
    ss >> res;
    return res;
 }

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef vector<long> VL;

char volteado[100][100];
string original[100];
int n,k;
int move[][2]={{0,1},{0,-1},{1,0},{-1,0},{1,1},{-1,1},{-1,-1},{1,-1}};

bool valido(int x, int y,char c){
   return (x>=0 && y>= 0 && x < n && y < n && volteado[x][y] == c);
}

char cerca(int col, int j){
   FORD(i,0,j){
      if (volteado[i][col]!='.'){
         char tmp =volteado[i][col];
        // cout << "Columna "<< i << " " << "(" << i << " , " << col << endl;
         volteado[i][col]='.';
         return tmp; 
      }
   }
   return '.';
}

int donde(int col){
   FORD(i,0,n){
      if (volteado[i][col]=='.'){
         //cout << "Returno " << i << endl;
         return i;
      }
   }
   assert(false);
}

void imprimir(){
   FOR(i,0,n){
      FOR(j,0,n) cout << volteado[i][j];
      cout << endl;
   }
   cout << endl;
}

void voltear(){
  //imprimir();
   FOR(i,0,n) FOR(j,0,n){
      volteado[i][j]=original[n-1-j][i];
   }
   char c;
      //imprimir();
   FORD(i,0,n){
      int j = n;
      while((c=cerca(i,j)) != '.'){
         //imprimir();
         int posicion = donde(i);
         j = posicion;
         volteado[posicion][i] = c;
         //cout << "Adentro " << posicion << " , " << i << "  = " << c << " " << volteado[posicion][i] << endl;

      }
   }
        //imprimir();
}

bool ganar(char c, int tam, int x, int y, int dir){
   //cout << "Ganar "<< c << " , " << tam << "," << x << "," << y << "," << dir << endl;
   if (tam == k-1){
      //cout << "Gano " << endl;
      return true;
   }
   bool respuesta = false;
   if (volteado[x][y] == c){
      if (valido(x+move[dir][0],y+move[dir][1],c)){
         respuesta = respuesta || ganar(c,tam+1,x+move[dir][0],y+move[dir][1],dir);
      }
   }
   return respuesta;
}

int main(){
   int casos;
   cin >> casos;
   FOR(caso,0,casos){
      cin >> n >> k;
      FOR(i,0,n) cin >> original[i];
      voltear();
      bool ganaAzul = false;

         FOR(i,0,n) FOR(j,0,n)      FOR(kk,0,8)
            ganaAzul = ganaAzul || ganar('B',0,i,j,kk);
      
      bool ganaRojo=false;

         FOR(i,0,n) FOR(j,0,n)      FOR(kk,0,8)
         ganaRojo = ganaRojo || ganar('R',0,i,j,kk);
   
      cout << "Case #" << (caso+1) << ": ";
      if (ganaAzul && ganaRojo){
         cout << "Both" << endl;
      }else if (ganaAzul && !ganaRojo){
         cout << "Blue" << endl;
      }else if (!ganaAzul && ganaRojo){
         cout << "Red" << endl;  
      }else{
         cout << "Neither" << endl;
      }
   }
   return 0;
}


