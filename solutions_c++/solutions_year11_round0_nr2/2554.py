#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

char m[128][128];
char e[128][128];

bool analiza(vector<char> &v){
    char p = v[ v.size()- 2 ];
    char q = v[ v.size()- 1 ];
    if( m[p][q] != 0 || m[q][p] != 0 ) return 1;
    return 0;
}

bool analiza2(vector<char> &v ){
    char p = v[ v.size()- 1 ];
    for(int i = 0 ; i < v.size() - 1 ; i++){
        if( e[v[i]][p] != 0 || e[p][v[i]] != 0 ) return 1;
    }
    return 0;
}

void solve(int test){
    int tam;
    string s;
    scanf("%d",&tam);
    cin >> s;
    vector<char> v;
    for(int i = 0 ; i < s.length() ; i++){
        v.push_back( s[i] );
        if( v.size() == 1 ) continue;
        if( analiza( v ) ){
            char p = v[ v.size()- 2 ];
            char q = v[ v.size()- 1 ];
            v.pop_back();
            v.pop_back();
            v.push_back( m[p][q] );
        }
        else if( analiza2( v ) ){
            v.erase( v.begin() , v.end() );
        }
    }
    printf("Case #%d: [",test);
    for(int i = 0 ; i < v.size() ; i++ ){
        if(i == v.size()-1)cout<<v[i];
        else cout<<v[i]<<", ";
    }
    puts("]");
    //v.pop_back();
}

void doit(int test){
    int c;
    scanf("%d",&c);
    memset(m , 0 , sizeof(m));
    for(int i = 0 ; i < c; i++){
        string s;
        cin >> s;
        m[s[0]][s[1]] = s[2];
        m[s[1]][s[0]] = s[2];
    }
    int d;
    scanf("%d",&d);
    memset(e , 0 , sizeof(e));
    for(int i = 0 ; i < d; i++){
        string s;
        cin >> s;
        e[s[0]][s[1]] = 1;
        e[s[1]][s[0]] = 1;
    }
    solve(test);
}

int main(){
    int t;    
    scanf("%d",&t);
    for(int i = 1 ; i <= t ; i++) doit(i);
}
