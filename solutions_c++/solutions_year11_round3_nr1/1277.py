#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <bitset>
#include <list>
#include <algorithm>
#include <cassert>


using namespace std;

#define rep(i, a, b) for(typeof(a) i=(a); i<(typeof(a))(b); ++i)
#define trav(v, it) for(typeof((v).begin()) it = (v).begin(); it != (v).end(); ++it)

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;

char m[50][51];
int r, c;
bool replace(){
    rep(i, 0, r-1){
        rep(j, 0, c-1){
            if(m[i][j] == '#'){
                if( m[i+1][j] == '#' && m[i][j+1] == '#' && m[i+1][j+1]== '#'){
                    m[i][j] = '/';
                    m[i+1][j] = '\\';
                    m[i][j+1] = '\\';
                    m[i+1][j+1] = '/';
                }
                else{
                    return false;
                }
            }
        }
    }
    rep(j,0,c){
        if(m[r-1][j] == '#')
            return false;
    }
    rep(i,0,r){
        if(m[i][c-1] == '#')
            return false;
    }
    return true;
}

inline bool solve(int tc){
    scanf("%d%d", &r, &c);
    rep(i, 0, r){
        scanf("%s", m[i]);
    }
    printf("Case #%d:\n", tc);
    if( replace() ) {
        rep(i, 0, r)
            printf("%s\n", m[i]);
    }
    else{
        printf("Impossible\n");
    }
    return true;
}

int main (int argc, char const *argv[]) {
    int n; scanf("%d",&n);
    for(int k=1; solve(k) && k<n; k++);
    return 0;
}