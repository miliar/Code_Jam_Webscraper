// @BEGIN_OF_SOURCE_CODE
/*
victord2exp!!!
victord2exp.blogspot.com
victord2exp.tk
*/
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <list>
#include <vector>
#include <map>
#include <sstream>
#include <cmath>
#include <bitset>
#include <utility>
#include <set>
#include <numeric>

#define INF_MAX 2147483647
#define INF_MIN -2147483647
#define pi acos(-1.0)
#define N 1000000
#define LL long long

#define For(i, a, b) for( int i = (a); i < (b); i++ )
#define Fors(i, sz) for( size_t i = 0; i < sz.size (); i++ )
#define Fore(it, x) for(typeof (x.begin()) it = x.begin(); it != x.end (); it++)
#define Set(a, s) memset(a, s, sizeof (a))
#define Read(r) freopen(r, "r", stdin)
#define Write(w) freopen(w, "w", stdout)
using namespace std;
vector<string> v(4);
bool winFila(int f,char X){
    bool sw=true;
    for(int i=0;i<4 && sw;i++){
        if(!(v[f][i]==X ||v[f][i]=='T'))
            sw=false;
    }
    return sw;
}
bool winColumna(int c,char X){
    bool sw=true;
    for(int i=0;i<4 && sw;i++){
        if(!(v[i][c]==X ||v[i][c]=='T'))
            sw=false;
    }
    return sw;
}
bool win(char X){
    bool sw=false;
    for(int i=0;i<4 && !sw;i++){
        if(winFila(i,X))
            sw=true;
        if(!sw && winColumna(i,X))
            sw=true;
    }
    if(!sw){
        bool sw2=true;
        for(int i=0;i<4 && sw2;i++){
            if(!(v[i][i]==X || v[i][i]=='T'))
                sw2=false;
        }
        if(!sw2){
            sw2=true;
            int r = 3;
            for(int i=0;i<4 && sw2 && r>=0;i++){
                if(!(v[r][i]==X || v[r][i]=='T'))
                    sw2=false;
                r--;
            }
        }
        if(sw2)
            sw=true;
    }
    return sw;
}
bool existe(char X){
    for(int i=0;i<4;i++){
        for(int j=0;j<4;j++)
            if(v[i][j]==X)
                return true;
    }
    return false;
}
int main ()
{
    Read("A-large.in");
    Write("SalidaA_L.out");
    int t;

    cin>>t;
    for(int i=1;i<=t;i++){
        for(int j=0;j<4;j++)
            cin>>v[j];
        if(win('X')){
            cout<<"Case #"<<i<<": X won"<<endl;
        }else if(win('O')){
            cout<<"Case #"<<i<<": O won"<<endl;
        }else if(!existe('.')){
            cout<<"Case #"<<i<<": Draw"<<endl;
        }else
            cout<<"Case #"<<i<<": Game has not completed"<<endl;
    }
	return 0;
}
