#include<iostream>

using namespace std;

typedef pair<int,int> pii;
#define x first
#define y second

int n;
int a[1001], b[1001];
int sol;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("t1.out", "w", stdout);
    int T, Ti;
    scanf("%d", &T);
    for(Ti = 1; Ti <= T; ++Ti)
    {
        sol = 0;
        int i, j;
        scanf("%d", &n);
        for(i = 0; i < n; ++i)
            scanf("%d %d", a+i, b+i);
        for(i = 0; i < n - 1; ++i)
            for(j = i + 1; j < n; ++j)
                if(a[i] > a[j] && b[i] < b[j] || a[i] < a[j] && b[i] > b[j])
                    ++sol;
        printf("Case #%d: %d\n", Ti, sol);
    }
    return 0;
}
