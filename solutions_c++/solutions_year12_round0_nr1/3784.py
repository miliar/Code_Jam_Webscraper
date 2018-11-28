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
#define ALL(x) (x).begin(), (x).end()
#define FORE(i, x) for (__typeof((x).begin()) i = (x).begin(); i != (x).end(); i++)
#define SZ(x) ((int) (x).size())
#define FOR(i, x) for (int i = 0; i <x; i++)
#define FORI(i,x,y) for (int i = x; i <y; i++)
#define MAXE 4

using namespace std;

int main(){
    freopen("A.in1","r",stdin);
    freopen("A.out","w",stdout);
    map<char,char> mapa;
    string source[MAXE], destination[MAXE];
    FOR (i,MAXE)
        getline(cin,source[i]);

    FOR (i,MAXE)
        getline(cin,destination[i]);

    FOR (i,MAXE)
        FOR (j,SZ(source[i]))
            mapa[source[i][j]]=destination[i][j];
    int casos;
    scanf("%d\n",&casos);
    FOR (i,casos){
        string cadena;
        getline(cin,cadena);
        printf("Case #%d: ",i+1);
        FOR (j,SZ(cadena))
            cout<<mapa[cadena[j]];
        cout<<endl;
    }
    return 0;
}
