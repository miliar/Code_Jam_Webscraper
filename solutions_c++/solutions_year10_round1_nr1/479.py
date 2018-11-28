#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<algorithm>

using namespace std;

#define FOR(_i, _times) for(int _i = 1; _i <= (_times); _i++)
#define FORV(_i, _times) for(int _i = 0; _i < (_times); _i++)
#define FORR(_i, _st, _ed) for(int _i = (_st); _i >= (_ed); _i--)
#define FORE(_i, _st, _ed) for(int _i = (_st); _i <= (_ed); _i++)

int T, n, k;
bool red, blue;
char board[60][60];

int shift(int r, int st)
{
    FORE(c, st, n)
    {
        if(board[r][c] != '.')
        {
            return c - 1;
        }
    }
    return n;
}

inline bool chk(int rs, int cs, char ch)
{
    bool yes;
    if(rs + k - 1 <= n)
    {
        yes = 1;
        FORV(i, k)
        {
            if(board[rs + i][cs] != ch)
            {
                yes = 0;
                break;
            }
        }
        if(yes) return 1;
    }
    if(rs - k + 1 >= 1)
    {
        yes = 1;
        FORV(i, k)
        {
            if(board[rs - i][cs] != ch)
            {
                yes = 0;
                break;
            }
        }
        if(yes) return 1;
    }
    if(cs + k - 1 <= n)
    {
        yes = 1;
        FORV(i, k)
        {
            if(board[rs][cs + i] != ch)
            {
                yes = 0;
                break;
            }
        }
        if(yes) return 1;
    }
    if(cs - k + 1 >= 1)
    {
        yes = 1;
        FORV(i, k)
        {
            if(board[rs][cs - i] != ch)
            {
                yes = 0;
                break;
            }
        }
        if(yes) return 1;
    }
    if(rs + k - 1 <= n and cs + k - 1 <= n)
    {
        yes = 1;
        int i = 0;
        while(i < k)
        {
            if(board[rs + i][cs + i] != ch)
            {
                yes = 0;
                break;
            }
            i++;
        }
        if(yes) return 1;
    }
    if(rs + k - 1 <= n and cs - k + 1 >= 1)
    {
        yes = 1;
        int i = 0;
        while(i < k)
        {
            if(board[rs + i][cs - i] != ch)
            {
                yes = 0;
                break;
            }
            i++;
        }
        if(yes) return 1;
    }
    if(rs - k + 1 >= 1 and cs + k - 1 <= n)
    {
        yes = 1;
        int i = 0;
        while(i < k)
        {
            if(board[rs - i][cs + i] != ch)
            {
                yes = 0;
                break;
            }
            i++;
        }
        if(yes) return 1;
    }
    if(rs - k + 1 >= 1 and cs - k + 1 >= 1)
    {
        yes = 1;
        int i = 0;
        while(i < k)
        {
            if(board[rs - i][cs - i] != ch)
            {
                yes = 0;
                break;
            }
            i++;
        }
        if(yes) return 1;
    }
    return 0;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    scanf("%d", &T);
    FOR(ttt, T)
    {
        red = blue = 0;
        scanf("%d %d", &n, &k);
        FOR(i, n)
        {
            scanf("%s", board[i] + 1);
        }
        FORR(c, n, 1)
        {
            FOR(r, n)
            {
                if(board[r][c] != '.')
                {
                    int shift_to = shift(r, c + 1);
                    if(shift_to != c)
                    {
                        board[r][shift_to] = board[r][c];
                        board[r][c] = '.';
                    }
                }
            }
        }
        /*printf(">>>>>>\n");
        FOR(i, n)
        {
            printf("%s\n", board[i] + 1);
        }*/
        FOR(r, n)
        {
            FOR(c, n)
            {
                if(chk(r, c, 'R'))
                {
                    red = 1;
                }
                if(chk(r, c, 'B'))
                {
                    blue = 1;
                }
                if(red and blue)
                {
                    break;
                }
            }
        }
        printf("Case #%d: ", ttt);
        if(red and blue) printf("Both\n");
        else if(red) printf("Red\n");
        else if(blue) printf("Blue\n");
        else printf("Neither\n");
    }
}
