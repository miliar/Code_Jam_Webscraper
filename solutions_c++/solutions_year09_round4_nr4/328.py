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

#define FOR(A, I, B) for(int A = (int)I; A < (int)B; A++)
#define SZ(A) (int)(A).size()
#define vi vector<int>
#define pb push_back
#define ll long long
#define ERRO 1e-12
#define DEQ(X,Y) ( fabs((X) - (Y)) < ERRO)

int n;
int X[5];
int Y[5];
int R[5];

double dist(int i, int j)
{
    return sqrt( (X[i]-X[j])*(X[i]-X[j]) + (Y[i]-Y[j])*(Y[i]-Y[j]));
}

int main()
{
    int t;
    scanf("%d", &t);
    FOR(test, 0, t){
        scanf("%d", &n);
        FOR(i, 0, n)
            scanf("%d %d %d", &X[i], &Y[i], &R[i]);

        double resp = 1e12;
        if(n == 1){
            resp = (double)R[0];
        } else if(n == 2){
            resp  = ((double)(R[0] + R[1]) + dist(0, 1))/2.0;
            resp = min(resp, max((double)R[0], (double)R[1]));
        } else {
        FOR(i, 0, n)
            FOR(j, i + 1, n){
                int unused;
                FOR(k, 0, n) if(k != i && k != j) { unused = k; break; }
                double rad = ((double)(R[i] + R[j]) + dist(i, j))/2.0;
                if(rad >= (double)R[unused])
                    resp = min(resp, rad);
            }
        }
        printf("Case #%d: %lf\n", test + 1, resp);    

    }
    return 0;
}

