#include <iostream>
#include <algorithm>

using namespace std;

int T; 
int N;
int ans;

typedef struct node
{
     int l, r;
}node;

node wire[2000];

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
	int i, j;
	
    for(i = 1; i <= N; i++)
        for(j = i + 1; j <= N; j++)
            if(wire[i].l < wire[j].l && wire[i].r > wire[j].r)
                ans++;

}

int main()
{
    freopen("rope.in", "r", stdin);
    freopen("rope.out", "w", stdout);
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
