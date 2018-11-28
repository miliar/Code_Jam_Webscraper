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

string tab[41];
int ones[41];
int n;

void troca(int a, int b)
{
    int tmp = ones[b];
    for(int i = b; i > a; i--)
        ones[i] = ones[i-1];
    ones[a] = tmp;
}

bool finished()
{
    FOR(i, 0, n)
        if(ones[i] > i) return false;
    return true;
}

int main()
{
    int t;
    scanf("%d", &t);
    FOR(test, 0, t){
        scanf("%d", &n);
        memset(ones, 0, sizeof(ones));
        FOR(i, 0, n)
            cin >> tab[i];
        FOR(i, 0, n)
            FOR(j, 0, n)
                if(tab[i][j] == '1') ones[i] = j;

        int resp = 0;
        while(!finished()){
            int f, l;
            //FOR(i, 0, n) printf("i %d ones[i] %d\n", i, ones[i]);
            FOR(i, 0, n)
                if(ones[i] > i){ f = i; break; }
            FOR(i, f + 1, n)
                if(ones[i] <= f){ l = i; break; }
            troca(f, l);
            resp += l - f;            
        }
        printf("Case #%d: %d\n", test + 1, resp);
    }
    return 0;
}

