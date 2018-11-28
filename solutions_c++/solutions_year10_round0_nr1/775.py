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

bool solve(int n, int k)
{
    return ((k + 1) % (1<<n) ) == 0;
}

int main()
{
    int testcases;
    scanf("%d", &testcases);
    for(int testcase = 0; testcase < testcases; testcase++){
        int n, k;
        scanf("%d %d", &n, &k);
        printf("Case #%d: %s\n", testcase + 1, solve(n, k) ? "ON" : "OFF");
    }
    return 0;
}

