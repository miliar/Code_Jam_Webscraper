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
#define vs vector<string>
#define vi vector<int>
#define pb push_back
#define pii pair<int, int>
#define ll long long
#define ERRO 1e-12
#define DEQ(X,Y) ( fabs((X) - (Y)) < ERRO)
    
int winning(int a, int b)
{
    if(a <= 0 || b <= 0) return 0;

    if(a == 1 && b == 1) return 0;

    if(a == 1 || b == 1) return 1;

    if(a == b) return 0;
    
    if(a > b) swap(a, b);

    bool win = false;
    int tira = a*(b/a);
    int times = b/a;
    
    //if(tira == b){ tira -= a; }
  
    bool one =  !winning(a, b - tira);
    bool two = false;
    if(b - tira + a < b) two = !winning(a, b - tira + a);

    return (one || two);
}


int solve(int a1, int a2, int b1, int b2)
{
    int resp = 0;

    for(int a = a1; a <= a2; a++){
        for(int b = b1; b <= b2; b++){
            if(winning(a, b)) resp++;
        }
    }

    return resp;
}

int main()
{
    int cases;
    scanf("%d", &cases);
    FOR(testcase, 0, cases){
        int a, aa, b, bb;
        scanf("%d %d %d %d", &a, &aa, &b, &bb);
        printf("Case #%d: %d\n", testcase + 1, solve(a, aa, b, bb));
    }

    return 0;
}

