/*
 * Author  : Pallab
 * Program : C
 *
 * 2012-04-14 12:48:46
 * I have not failed, I have just found 10000 ways that won't work.
 *
 */
#include <iostream>
#include <algorithm>
#include <vector>
#include <sstream>
#include <fstream>
#include <string>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <functional>
#include <bitset>
#include <iomanip>

#include <ctime>
#include <cassert>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <climits>
#include <cstring>
#include <cstdlib>

using namespace std;


#define foR(i1,st,ed) for(int i1 = st , j1 = ed ; i1 < j1 ; ++i1 )
#define fo(i1,ed) foR( i1 , 0 , ed )
#define foE(i1,st,ed) foR( i1, st, ed+1 )
#define foit(i, x) for (typeof((x).begin()) i = (x).begin(); i != (x).end(); i++)
#define bip system("pause")
#define Int long long
#define pb push_back
#define SZ(X) (int)(X).size()
#define LN(X) (int)(X).length()
#define mk make_pair
#define SET( ARRAY , VALUE ) memset( ARRAY , VALUE , sizeof(ARRAY) )
#define line puts("")

template<class T1>
inline void debug(T1 _x) {
    cout<<_x<<'\n';
}
template<class T1, class T2>
inline void debug(T1 _x,T2 _y) {
    cout<<_x<<' '<<_y<<'\n';
}
template<class T1, class T2, class T3>
inline void debug(T1 _x,T2 _y,T3 _z) {
    cout<<_x<<' '<<_y<<' '<<_z<<'\n';
}
template<class T1, class T2, class T3, class T4>
inline void debug(T1 _x,T2 _y,T3 _z,T4 _zz) {
    cout<<_x<<' '<<_y<<' '<<_z<<' '<<_zz<<'\n';
}
template< class T1>
inline void debug(T1 _array,int _size) {
    cout<<"[";
    for (int i=0;i<_size;++i) {
        cout<<' '<<_array[i];
    }
    puts(" ]");
}
inline bool CI(int &_x) {
    return scanf("%d",&_x)==1;
}
inline bool CI(int &_x, int &_y) {
    return CI(_x)&&CI(_y) ;
}
inline bool CI(int &_x, int &_y, int &_z) {
    return CI(_x)&&CI(_y)&&CI(_z) ;
}
inline bool CI(int &_x, int &_y, int &_z, int &_zz) {
    return CI(_x)&&CI(_y)&&CI(_z)&&CI(_zz) ;
}

inline int toI(string _str) {
    int var;
    sscanf(_str.c_str(),"%d",&var);
    return var;
}
inline string toS(int var) {
    char _buff[50];
    sprintf( _buff,"%d",var);
    return (string)_buff;
}
inline bool f2(int A, int B) {
    string a = toS(A);
    string b = toS(B);
    for (int i=1;i<LN(a);++i) {
        string aa = a.substr(0,i);
        string ab = a.substr(i);
        for (int j=1;j<LN(b);++j) {
            string ba = b.substr(0,j);
            string bb = b.substr(j);
            if (aa==bb&&ab==ba)return true;
        }
    }
    return false;
}
inline void Solve(int A,int B) {
    int cnt=0;
    //line;
    set<pair<int,int> >st;
    for (int n=A;n<=B;++n) {
	string a = toS(n);
	for (int i=1;i<LN(a);++i) {
	  string aa = a.substr(0,i);
	  string ab = a.substr(i);
	  int m = toI(ab+aa);
	  if( m>n && m<=B){ 
	    st.insert(mk(n,m));
	  }
	}
    }
    cout<<SZ(st);
    line;
}
int main() {

    int tt,A,B;
    CI(tt);
    foE(i,1,tt) {
        cout<<"Case #"<<i<<": ";
        CI(A,B);
        Solve(A,B);
    }
    return 0;
}
