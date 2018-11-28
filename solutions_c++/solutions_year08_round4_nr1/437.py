#include <iostream>
#include <map>
#include <string>
#include <algorithm>
using namespace std;

int t, tt, V, M;
int inter[10001], change[5001];
int record[10005][2], mark[10005][2];

void input()
{
    scanf("%d %d", &M, &V);
    for (int i = 1; i <= (M -1) / 2; i++)
    {
        scanf("%d %d", &inter[i], &change[i]);
    }    
    for (int i = (M -1) / 2 + 1; i <= M; i++)
    {
        scanf("%d", &inter[i]);
    }    
    memset(mark, 0, sizeof(mark));
} 

int get(int x, int y)
{
    if (mark[x][y]) return record[x][y];
    if (x > (M - 1) / 2) 
    {
        if (inter[x] != y) { mark[x][y] = 1; return record[x][y] = -1; }
        if (inter[x] == y) { mark[x][y] = 1; return record[x][y] = 0; }
    }  
    else 
    {
        int x1 = get(x * 2, 0);
        int x2 = get(x * 2, 1);
        int x3 = get(x * 2 + 1, 0);
        int x4 = get(x * 2 + 1, 1);
        int y1 = x1 + x3;
        int y2 = x1 + x4;
        int y3 = x2 + x3;
        int y4 = x2 + x4;
        if (x1 < 0) y1  = -1, y2 = -1;
        if (x2 < 0) y3 = -1, y4 = -1;
        if (x3 < 0) y1 = -1, y3 = -1;
        if (x4 < 0) y2 = -1, y4 = -1;
        
        int ret = 100000;
        if (change[x])
        {
            if (y == 0)
            {
                if (inter[x] == 1) 
                {
                    if (y1 >= 0) if (y1 < ret) ret = y1;
                    if (y2 >= 0) if (y2 < ret) ret = y2;
                    if (y3 >= 0) if (y3 < ret) ret = y3;
                }  else
                {
                    if (y1 >= 0) if (y1 < ret) ret = y1;
                    if (y2 >= 0) if (y2 + 1 < ret) ret = y2 + 1;
                    if (y3 >= 0) if (y3 + 1 < ret) ret = y3 + 1;
                }      
            }
            else if (y == 1)
            {
                if (inter[x] == 1) 
                {
                    if (y4 >= 0) if (y4 < ret) ret = y4;
                    if (y2 >= 0) if (y2 + 1 < ret) ret = y2 + 1;
                    if (y3 >= 0) if (y3 + 1 < ret) ret = y3 + 1;
                }  else
                {
                    if (y4 >= 0) if (y4 < ret) ret = y4;
                    if (y2 >= 0) if (y2 < ret) ret = y2;
                    if (y3 >= 0) if (y3 < ret) ret = y3;
                } 
            }        
        } else 
        {
            if (y == 0)
            {
                if (inter[x] == 1) 
                {
                    if (y1 >= 0) if (y1 < ret) ret = y1;
                    if (y2 >= 0) if (y2 < ret) ret = y2;
                    if (y3 >= 0) if (y3 < ret) ret = y3;
                }  else
                {
                    if (y1 >= 0) if (y1 < ret) ret = y1;
                    //if (y2 >= 0) if (y2 + 1 < ret) ret = y2 + 1;
                    //if (y3 >= 0) if (y3 + 1 < ret) ret = y3 + 1;
                }      
            }
            else if (y == 1)
            {
                if (inter[x] == 1) 
                {
                    if (y4 >= 0) if (y4 < ret) ret = y4;
                    //if (y2 >= 0) if (y2 + 1 < ret) ret = y2 + 1;
                    //if (y3 >= 0) if (y3 + 1 < ret) ret = y3 + 1;
                }  else
                {
                    if (y4 >= 0) if (y4 < ret) ret = y4;
                    if (y2 >= 0) if (y2 < ret) ret = y2;
                    if (y3 >= 0) if (y3 < ret) ret = y3;
                } 
            }        
        }  
        if (ret == 100000) {mark[x][y] = 1; return record[x][y] = -1; }
        else {mark[x][y] = 1; return record[x][y] = ret;}      
    }      
}    

void solve()
{
    int x = get(1, V);
    if (x < 0)  printf("Case #%d: IMPOSSIBLE\n", t);
    else printf("Case #%d: %d\n", t, x);
}  

int main()
{
    //freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-large.in", "r", stdin);
    freopen("out2.txt", "w", stdout);
    scanf("%d", &tt);
    for (t = 1; t <= tt; t++)
    {
        input();
        solve();
    }  
}    
