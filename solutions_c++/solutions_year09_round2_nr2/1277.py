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
int digi[12];

bool count(int num)
{
    int dig[12];
    memset(dig, 0, sizeof(dig));
    while(num > 0){
        dig[num%10] += 1;
        num /= 10;
    }
    FOR(i, 1, 10){
        if(dig[i] != digi[i])
            return false;
    }
    return true;
}

int main()
{
    int t;
    scanf("%d", &t);

    FOR(test, 0, t){
        scanf("%d", &n);
        memset(digi, 0, sizeof(digi));
        int nn = n;
        while(nn > 0){
            digi[nn%10] += 1;
            nn /= 10;
        }
        int res;
        for(res = n + 1; ; res++){
            if(count(res))
                break;
        }
        printf("Case #%d: %d\n", test + 1, res);
    }
    return 0;
}

