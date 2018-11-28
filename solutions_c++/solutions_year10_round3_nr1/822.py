#include <iostream>
#include <algorithm>

using namespace std;

int T; 
int N;
int ans;

class node
{
    public:
        int l, r;
}wire[1001];

int cmp(node a, node b)
{
    if(a.l < b.l) return 1;
    else
        if(a.l > b.l) return 0;
        else
        {
            if(a.r < b.r) return 1;
            else return 0;
        }
}

void work()
{
    for(int i = 1; i <= N; i++)
        for(int j = i + 1; j <= N; j++)
            if(wire[i].l < wire[j].l && wire[i].r > wire[j].r)
                ans++;

}

int main()
{
    freopen("1.in", "r", stdin);
    freopen("1.out", "w", stdout);
    scanf("%d", &T);
    for(int i = 1; i <= T; i++)
    {
        scanf("%d", &N);   
        ans = 0; 
        for(int j = 1; j <= N; j++)
            scanf("%d%d", &wire[j].l, &wire[j].r);    
        sort(wire + 1, wire + N + 1, cmp);
        work();
        printf("Case #%d: %d\n", i, ans);
    }
    return 0;
}
