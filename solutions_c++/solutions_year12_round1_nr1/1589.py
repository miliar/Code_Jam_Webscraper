#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <set>
#include <stack>
#include <deque>
#include <queue>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <iomanip>
#include <climits>
#include <cfloat>
#include <cstdio>
#define x first
#define y second
#define IN(x, n) (0 <= (x) && (x) < n)
#define MAX 100010
#define MOD 1000000007
#define INF 9223372036854775807LL
using namespace std;

typedef long long int entero;
typedef pair<int, int> Point;

double v[MAX], pos[MAX];

int busca_mala(int i){
    int a = 1, b = -1;
    while(i>0){
        if(i&1)
            b = a;
        a++;
        i>>=1;
    }
    return b;
}

int main(){
    int a, b, i, j, k, A, B, T, lim, teclas;
    double p, suma, minimo;
    cin >> T;
    for(k = 1; k <= T; k++){
        cin >> A >> B;
        for(j = 0; j < A; j++)
            scanf("%lf", &v[j]);
        lim = (1<<A);
//        printf("%d\n", lim);
        for(i = 0; i < lim; i++){
            for(a = i, j = A-1, p = 1.0; j >= 0; j--, a>>=1){
                if((a&1) == 0)
                    p*=v[j];
                else
                    p*=(1.0-v[j]);
            }
            pos[i] = p;
//            printf("p%d = %lf\n", i, p);
        }
//        printf("\n");
        minimo = B+2.0;
        for(a = 0; a <= A; a++){//cuantas presiono
            for(i = 0, suma = 0; i < lim; i++){
                b = busca_mala(i);
                if(b <= a){
                    teclas = a+(B-A+a)+1;
                }
                else{
                    teclas = a+(B-A+a)+1+B+1;
                }
//                printf("%d %d %lf\n", a, teclas, pos[i]);
                suma+=teclas*pos[i];
            }
//            printf("suma = %lf\n", suma);
            if(suma < minimo)
                minimo = suma;
        }
        printf("Case #%d: %lf\n", k, minimo);
    }
    return 0;
}
