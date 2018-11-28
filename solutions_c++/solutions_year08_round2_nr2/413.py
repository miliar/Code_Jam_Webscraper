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

#define M 1001

int v[M];
bool pp[M];


int pai(int x) {
    while(v[x] != x)
        x = v[x];
    return x;
}

int vamo(int a, int b, int p) {
    int i,j;
    for(i=0;i<=b;i++)
        v[i] = i;
    memset(pp,true,sizeof(pp));
    for(i=2;i<=b;i++) {
        for(j=i;!pp[j];j++) if(j>b) break;
        i = j;
        for(j=j+j;j<=b;j+=i) {
            pp[j] = false;
        }        
    }

    for(i=a;i<=b;i++) {
        v[i] = i;
    }

    int r = 0;

    for(i=p;i<=b;i++) {
        if(pp[i]) {
            for(j=i;j<=b;j+=i) {
                if(j<a) continue;
                int g1 = pai(i);
                int g2 = pai(j);                
                v[g2] = g1;
//                printf("junta %d %d no grupo %d %d\n" , i,j,g1,g2);
           }
        }
    }

    set<int> tenho;
    tenho.clear();

    for(i=a;i<=b;i++) {
        int g = pai(i);
//        printf("%d tah no grupo %d\n" , i , g);
        tenho.insert(g);
    }

    return (int) tenho.size();
}

int main() {
    int N,I;
    scanf("%d" , &N);
    for(I=1;I<=N;I++) {
        int a,b,p,i,j;
        scanf("%d %d %d" , &a, &b ,&p);

        int res = vamo(a,b,p);

/*        t.clear();
        for(i=a;i<=b;i++) {
            t.insert(v[i]);
            printf("%d pertence a %d\n" , i, v[i]);
        } */

        printf("Case #%d: "  , I);
        printf("%d\n" ,res);
    }
    return 0;
}

