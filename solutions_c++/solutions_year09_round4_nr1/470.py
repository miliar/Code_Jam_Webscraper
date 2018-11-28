#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;

const int maxn=1610;

int n;
char str[50][50];


void input()
{
    int i;
    scanf("%d", &n);
    memset(str, 0, sizeof(str));
    for(i=0; i<n; i++) scanf("%s", &str[i]);//, printf("%s\n", str[i]);
}

bool ok(int i, int r)
{
    int j;
    
    j=n-1;
    while(str[i][j]=='0' && j>=0) j--;
    //printf("r, i, j, %d %d %d\n", r, i, j);
    if(j<=r) return 1;
    return 0; 
}

void swp(int i, int j)
{
    int k; 
    for(k=0; k<n; k++) swap(str[i][k], str[j][k]);
}

int solve(int r)
{
    int i, j;
    
    for(i=r; i<n; i++){
        if(ok(i, r)) break;
    }
    //printf("%d %d\n", r, i);
    for(j=i-1; j>=r; j--) swp(j, j+1);
    return i-r;
}

int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);

    int ct, cc, ans, i;
    
    scanf("%d", &ct);
    for(cc=1; cc<=ct; cc++){
        input();
        ans=0;
        for(i=0; i<n; i++) ans+=solve(i);
        printf("Case #%d: %d\n", cc, ans);
    }
    
    return 0;
}
