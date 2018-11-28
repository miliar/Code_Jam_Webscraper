#include "stdafx.h"
#include <iostream>
#include <stdio.h>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <map>
#include <string>
#include <set>
#include <algorithm>
#include <functional>
#include <numeric>
#include <iterator>
#include <time.h>
#include <memory>
using namespace std;

typedef long long LL;
typedef long long uLL;
typedef unsigned int uint;
#define FOR(i, b, e) for(int i=(b); i<int(e); ++i)
#define dFOR(i, b, e) for(int i=(b); i>int(e); --i)
#define FORV(i, b, e) for(i=(b); i<(e); ++i)
#define dFORV(i, b, e) for(i=(b); i>int(e); --i)
#define GET(a) cin >> a
#define GET2(a, b) cin >> a >> b
#define GET3(a, b, c) cin >> a >> b >> c
#define GET4(a, b, c, d) cin >> a >> b >> c >> d
#define MAX(a, b) ((a) < (b) ? (b) : (a))
#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define PB(a) push_back(a)
#define SIZE(a) a.size()
#define PEEK(a) cout << " >> " #a " = " << a << endl
#define peek(a) _peek(#a, a)
template <typename T> void _peek(char name[], T &obj, size_t max_count=50){
    const size_t ipl = 10;
    cout << " >> " << name << " = ["; size_t _count = 0;
    for(typename T::iterator it=obj.begin(); it!=obj.end(); ++it){
        if(_count && _count%ipl == 0) cout << "      [";
        cout << *it; ++_count;
        if(_count%ipl == 0 || _count >= max_count || it == obj.end()-1) cout << " ]\n";
        else cout << ", ";
        if(_count >= max_count) break;
    }
}
template <typename T> ostream &operator << (ostream &cout, pair<T, T> &x){
    cout << "(" << x.first << "," << x.second << ")";
    return cout;
}
template <typename T> inline T GCD(T a, T b){
    if(b==0) return a;
    a %= b; while(a){ swap(a, b); a %= b; }; return b;
}
template <typename T> inline T LCM(T a, T b){
    if(a == 0 || b == 0) return -1;
    a /= GCD(a, b); T lcm = a * b;
    if(lcm < 0 || lcm/a != b ) return -1;
    return lcm;
}
//===========================================================
int T, test_case;
const int MAX_SIZE = 10010;
int N;
int d[MAX_SIZE];
int l[MAX_SIZE];
int D;

int result[MAX_SIZE][MAX_SIZE];



bool solve(){
    l[0] = d[0];

    if(l[0]+l[0] >= D)
        return true;

    memset( result, 0, sizeof(result) );

    dFOR(first, N-1, -1){
        dFOR(second, N-1, first){
            int dd = d[second] - d[first];
            if( l[second] < dd )
                dd = l[second];

            if( d[second] + dd >= D ){
                result[first][second] = 1;
                continue;
            }
            
            for(int next=second+1; next<N && d[next] <= d[second] + dd; ++next){
                if( result[second][next] == 1 ){
                    result[first][second] = 1; break;
                }
            }
        }
    }

    FOR(second, 1, N){
        if( d[second] <= l[0]+l[0] ){
            if( result[0][second] == 1 )
                return true;
        }
        else
            break;
    }

    return false;
}


int main()
{
    freopen("z:\\output.txt", "w", stdout);

    freopen("z:\\A-small-attempt0.in", "r", stdin);
    //freopen("z:\\A-large.in", "r", stdin);
    //freopen("z:\\input.txt", "r", stdin);

    GET(T);
    FORV(test_case, 1, T+1)
    {
        GET(N);
        FOR(i, 0, N) GET2(d[i], l[i]);
        GET(D);
        
        cout << "Case #" << test_case << ": ";
        if( solve() )
            cout << "YES\n";
        else
            cout << "NO\n";
    }

    return 0;
}


