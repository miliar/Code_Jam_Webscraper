#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#define SIZE 64

using namespace std;

char board[SIZE][SIZE];
int n, k;
void change1();
void change2();
inline bool legal(int x, int y)
{
    return x >= 0 && x < n && y >= 0 && y < n;
}
bool check(char col);

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int C = 0, T;

    scanf("%d", &T);
    while (T--)
    {
        scanf("%d %d", &n, &k);
        for (int i = 0; i < n; i++)
            scanf("%s", board[i]);
        change1();
        change2();
        bool rw = check('R'), bw = check('B');
        if(rw && bw)printf("Case #%d: Both\n", ++C);
        else if(rw)printf("Case #%d: Red\n", ++C);
        else if(bw)printf("Case #%d: Blue\n", ++C);
        else printf("Case #%d: Neither\n", ++C);
    }


    return 0;
}

void change1()
{
    for (int i = 0; i < n; i++)
    {
        int p1 = n - 1, p2 = n - 1;
        for (; p2 >= 0; p2--)
        {
            if (board[i][p2] != '.')
            {
                swap(board[i][p2], board[i][p1]);
                p1--;
            }
        }
    }
}
void change2()
{
    for (int i = 0; i < n; i++)
    {
        int p1 = n - 1, p2 = n - 1;
        for (; p2 >= 0; p2--)
        {
            if (board[p2][i] != '.')
            {
                swap(board[p2][i], board[p1][i]);
                p1--;
            }
        }
    }
}
bool check(char col)
{
    for (int i = 0; i < n; i++)
    {
        int j = 0;
        while (j < n)
        {
            int t = j, cnt = 0;
            while (cnt < k && t < n && board[i][t] == col)
                t++, cnt++;
            if (cnt == k)return true;
            j = t + 1;
        }
    }
    for (int i = 0; i < n; i++)
    {
        int j = 0;
        while (j < n)
        {
            int t = j, cnt = 0;
            while (cnt < k && t < n && board[t][i] == col)
                t++, cnt++;
            if (cnt == k)return true;
            j = t + 1;
        }
    }
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < n; j++)
        {
            if(board[i][j] != col)continue;
            int cnt = 1;
            while(cnt < k)
            {
                int x = i + cnt, y = j + cnt;
                if(!legal(x, y) || board[x][y] != col)break;
                cnt++;
            }
            if(cnt == k)return true;
            cnt = 1;
            while(cnt < k)
            {
                int x = i + cnt, y = j - cnt;
                if(!legal(x, y) || board[x][y] != col)break;
                cnt++;
            }
            if(cnt == k)return true;
        }
    }
    return false;
}
