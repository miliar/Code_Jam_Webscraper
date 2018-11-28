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
#include "regex.h"

#define DEBUG(x) cerr << '>' << #x << ": " << x << endl;
#define CLEAR(x,c) memset(x,c,sizeof(x))
#define FOR(i,a,b) for(int i=(a),_b=(b);i<_b;i++)
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
//template<typename T> inline int Size(const T& c) { return (int)c.size(); }
template<typename T> inline void checkMin(T& a, T b) { if (b < a) a = b; }
template<typename T> inline void checkMax(T& a, T b) { if (b > a) a = b; }
template<typename T> inline bool isSet(T number, int bit) { return (number&(T(1)<<bit)) != 0; }
template<class T> T abs(T x){return x>0 ? x:(-x);}
/*template<class T> T& operator >?= (T& x, T y) {if(y>x) x=y; return x;}
template<class T> T& operator <?= (T& x, T y) {if(y<x) x=y; return x;}
template<class T> T operator >? (T x, T y) {return x>y?x:y;}
template<class T> T operator <? (T x, T y) {return x<y?x:y;}*/

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

string original = "welcome to code jam";
string cadena;

int dp[21][600];

int funcion(int i , int j){
    if (i >= original.sz) return 1;
    if (j >= cadena.sz) return 0;
    int& respuesta = dp[i][j];
    if (respuesta != -1) return respuesta;
    if (original[i] == cadena[j]) return respuesta = ((funcion(i+1,j+1)+funcion(i,j+1))%10000);
    if (original[i] != cadena[j]) return respuesta = funcion(i,j+1);
}

int main(){
    int casos;
    cin >> casos;
    getline(cin,cadena);
    FOR(caso,0,casos){
        CLEAR(dp,-1);
        getline(cin,cadena);
        string respuesta = cast<string>(funcion(0,0)%1000);
        while(respuesta.sz < 4) respuesta.insert(0,"0");
        cout << "Case #" << (caso+1) << ": " << respuesta << endl;
    }
    return 0;
}


