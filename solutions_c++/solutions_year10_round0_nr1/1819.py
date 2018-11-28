#include<iostream>
using namespace std;

void solve(int pos)
{
    int n, k;
    scanf("%d%d", &n, &k);
    
    int all = 1 << n;
    
    if( ( k % all ) == all - 1 ) printf("Case #%d: ON\n",pos);
    else printf("Case #%d: OFF\n",pos);
}
int main()
{
    int t, ;
    scanf("%d", &t);
    for(int i = 1; i <= t; ++i)solve(i);
    return 0;
}
