#include <iostream>
#include <map>
#include <string>
#include <algorithm>
using namespace std;

int H, W, R;
int record[101][101];
int B[101][101];

int get(int x, int y)
{
    if (x > H) return 0;
    if (y > W) return 0;
    if (record[x][y] >= 0) return record[x][y];    
    int &ret = record[x][y];
    if (B[x][y]) return ret = 0;
    if (x == H && y == W) return ret = 1;
    return ret = (get(x + 1, y + 2) + get (x + 2, y + 1)) % 10007;
}    

void solve()
{
    memset(record, -1, sizeof(record));
    printf("%d\n", get(1, 1));
}  

   

int main()
{
    freopen("D-small-attempt0.in", "r", stdin);
    //freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t; scanf("%d", &t);
    for (int i = 1; i <= t; i++)
    {
        printf("Case #%d: ", i);
        scanf("%d %d %d", &H, &W, &R);
        memset(B, 0, sizeof(B));
        for (int j = 0; j < R; j++) {int a, b; scanf("%d %d", &a, &b); B[a][b] = 1; }
        solve();
    }      
}    
