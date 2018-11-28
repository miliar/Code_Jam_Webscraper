#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <set>


using namespace std;


int l[1146], p[1146], ans[1146];


bool cmp(const int & a, const int & b)
{
    if(p[a] != p[b])
        return p[a] > p[b];
    if(l[a] != l[b] && p[a] != 0)
        return l[a] > p[b];
    return a < b;
}


void solve(int tc)
{
    int n;
    scanf("%d", &n);
    for(int i = 0; i < n; i++)
        scanf("%d", &l[i]);
    for(int i = 0; i < n; i++)
        scanf("%d", &p[i]);
    for(int i = 0; i < n; i++)
        ans[i] = i;
    sort(ans, ans + n, cmp);
    printf("Case #%d:", tc + 1);
    for(int i = 0; i < n; i++)
        printf(" %d", ans[i]);
    printf("\n");
}


int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int n;
    scanf("%d", &n);
    for(int i = 0; i < n; i++)
        solve(i);
}
