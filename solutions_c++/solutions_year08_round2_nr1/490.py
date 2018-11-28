#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;

#define vs vector<string>
#define vi vector<int>
#define ll long long
#define erro 1e-12
#define igual(X,Y) ( fabs((X) - (Y)) < erro)

struct X {
    ll x;
    ll y;
};

vector<X> v;

int EH(X a, X b , X c) {
    ll x = (a.x+b.x+c.x);
    ll y = (a.y+b.y+c.y);

    if(x%3==0 && y%3==0) return 1;
    return 0;

}

int main() {
    int N,I;
    scanf("%d" , &N);
    for(I=1;I<=N;I++) {
        ll n,i;
        ll A,B,C,D,x0,y0,M;
        scanf("%lld" , &n);        
        scanf("%lld %lld %lld %lld %lld %lld %lld" , &A,&B,&C,&D,&x0,&y0,&M);

        v.clear();

        X aux;
        aux.x = x0;
        aux.y = y0;
        v.push_back(aux);

        //    printf("%d %d\n" , aux.x , aux.y);
        int j;
        for(j=1;j<n;j++) {
            aux.x = ( A  * aux.x + B) % M;
            aux.y = (C * aux.y + D) % M;
          //  printf("%d %d\n" , aux.x , aux.y);
            v.push_back(aux);
        }

        int res = 0;
        int k;
        for(i=0;i<n;i++) {
            for(j=i+1;j<n;j++) {
                for(k=j+1;k<n;k++) {
                    if(EH(v[i],v[j],v[k]))
                        res++;
                }
            }
        }


        printf("Case #%d: "  , I);
        printf("%d\n" , res);
    }
    return 0;
}

