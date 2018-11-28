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

int n;
int candies[1111];

int main()
{
    int t;
    scanf("%d", &t);
    FOR(testcase, 0, t){
        printf("Case #%d: ", testcase + 1);
        
        scanf("%d", &n);
        FOR(i, 0, n)
            scanf("%d",  &candies[i]);

        int bits[22];
        memset(bits, 0, sizeof(bits));

        int mini = 1<<25;
        int total = 0;
        FOR(i, 0, n){
            mini = min(mini, candies[i]);
            total += candies[i];
            FOR(j, 0, 22) 
                if((candies[i]>>j) & 1)
                    bits[j]++;
        }        
        
        bool can_divide = true;
        FOR(i, 0, 22) if(bits[i]&1) can_divide = false;

        if(can_divide) printf("%d\n", total - mini);
        else printf("NO\n");

    }
    return 0;
}

