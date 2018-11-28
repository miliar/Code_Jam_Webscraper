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

#define INF 100000

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

int mapa[101][101];
char respuesta[101][101];
int h, w;

int move[][2] = {{-1,0},{0,-1},{0,1},{1,0}};

bool valido(int x, int y){
    return x>=0 && y >= 0 && x < h && y < w;
}

pair<int,int> fluir(int x, int y){
    pair< int,int> respuesta = mp(INF,INF);
    FOR(i,0,4)
        if (valido(x+move[i][0],y+move[i][1])){
            if (respuesta.X == INF){
                if (mapa[x+move[i][0]][y+move[i][1]] < mapa[x][y])
                    respuesta = mp(x+move[i][0],y+move[i][1]);
            }else{
                if (mapa[x+move[i][0]][y+move[i][1]] < mapa[respuesta.X][respuesta.Y])
                    respuesta = mp(x+move[i][0],y+move[i][1]);
            }
        }
    return respuesta;
}

int main(){
    int casos;
    cin >> casos;
    FOR(caso,0,casos){
        cin >> h >> w;
        CLEAR(respuesta,0);
        FOR(i,0,h) FOR(j,0,w) cin >> mapa[i][j];
        char actual = 'b';
        respuesta[0][0] = 'a';
        pair<int,int> temp1,temp2;
        FOR(i,0,h){
            FOR(j,0,w){
                if (respuesta[i][j] == 0){
                    temp1 = fluir(i,j);
                    while(!(temp1.X == INF && temp1.Y == INF) && (respuesta[temp1.X][temp1.Y] == 0)) temp1 = fluir(temp1.X,temp1.Y);
                    if (temp1.X == INF && temp1.Y == INF){
                        respuesta[i][j] = actual;
                        temp1 = fluir(i,j);
                        while(!(temp1.X == INF && temp1.Y == INF) && (respuesta[temp1.X][temp1.Y] == 0)){
                            respuesta[temp1.X][temp1.Y] = actual;
                            temp1 = fluir(temp1.X,temp1.Y);
                        }
                        actual++;
                    }else{
                        respuesta[i][j] = respuesta[temp1.X][temp1.Y];
                        temp2 = fluir(i,j);
                        while(!(temp2.X == INF && temp2.Y == INF) && (respuesta[temp2.X][temp2.Y] == 0)){
                            respuesta[temp2.X][temp2.Y] = respuesta[temp1.X][temp1.Y];
                            temp2 = fluir(temp2.X,temp2.Y);
                        }
                    }
                }else{
                    temp1 = fluir(i,j);
                    while(!(temp1.X == INF && temp1.Y == INF) && (respuesta[temp1.X][temp1.Y] == 0)){
                        respuesta[temp1.X][temp1.Y] = respuesta[i][j];
                        temp1 = fluir(temp1.X,temp1.Y);
                    }
                }
            }
        }
        cout << "Case #" << (caso+1) << ":\n";
        FOR(i,0,h){
            FOR(j,0,w-1) cout << respuesta[i][j] << " ";
            cout << respuesta[i][w-1] << endl;
        }
    }
    return 0;
}


