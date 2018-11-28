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


using namespace std;

int main(){
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    int A,B,casos;
    scanf("%d",&casos);
    FOR(cases,casos){
        set<pair<int,int> > pares;
        scanf("%d%d",&A,&B);
        FORI (i,A,B){
            int M;
            char cadena[100];
            sprintf(cadena,"%d",i);
            string cad=cadena;
            FOR (j,SZ(cad)-1){
                rotate(cad.begin(),cad.begin()+1,cad.end());
                sscanf(cad.c_str(),"%d",&M);
                if (i<M && M<=B){
                    pares.insert(make_pair(i,M));
                    //cout<<i<<", "<<M<<endl;
                }
            }
        }
        printf("Case #%d: %d\n",cases+1,SZ(pares));
    }

    return 0;
}
