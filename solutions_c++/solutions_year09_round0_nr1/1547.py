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

VS diccionario;
VS partes;

bool pertenece(char c, int pos){
    //cerr << "Pertenece " << c << " " << partes[pos] << endl;
    FOR(i,0,partes[pos].sz) if (partes[pos][i] == c) return true;
    return false;
}

int match(string cadena){
    string temp;
    partes.clear();
    bool dentro = false;
    FOR(i,0,cadena.sz){
        if (cadena[i] >= 'a' && cadena[i] <= 'z'){
            if (!dentro){
                string nuevo;
                nuevo.pb(cadena[i]);
                partes.pb(nuevo);
            }else{
                temp.pb(cadena[i]);
            }
        }else if (cadena[i] == '('){
            dentro = true;
        }else{
            partes.pb(temp);
            temp = "";
            dentro = false;
        }
    }
    //FOR(i,0,partes.sz) DEBUG(partes[i]);
    int respuesta = 0;
    FOR(i,0,diccionario.sz){
        bool perteneceB = true;
        FOR(j,0,diccionario[i].sz){
            if (!pertenece(diccionario[i][j],j)){
                perteneceB = false;
            }
            //cerr << "Palabra " << i << " Paso " << j << " pertenece " << perteneceB << endl;
        }
        if (perteneceB){ ++respuesta; }//cerr << "SUMO\n";}
    }
    //cerr << "Acumulo " << respuesta << endl;
    return respuesta;
}

int main(){
    int l,d,casos;
    diccionario.clear();
    cin >> l >> d >> casos;
    string temp;
    FOR(i,0,d){ cin >> temp; diccionario.pb(temp);}
    FOR(caso,0,casos){
        cin >> temp;
        cout << "Case #" << (caso+1) << ": " << match(temp) << endl;
    }
    return 0;
}


