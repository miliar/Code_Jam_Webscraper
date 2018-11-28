#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

const int N = 110;

char m[N][N];
int n, k;
bool r, b;

void init()
{
    memset(m, 0, sizeof(m));
    cin>>n>>k;
    for(int i = 0; i < n; i++)
    {
        cin>>m[i];
    }
}

void rotate()
{
    char m2[N][N];
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < n; j++)
        {
            int x = j;
            int y = i;
            x = n-1-x;
            m2[i][j] = m[x][y];
            //printf("%c", m2[i][j]);
        }
        //printf("\n");
    }
    //printf("\n");
    for(int i = 0; i < n; i++)
    {
        int pos = n-1;
        for(int j = n-1; j >= 0; j--)
        {
            if(m2[j][i] == '.') continue;
            m2[pos][i] = m2[j][i];
            if(j != pos) m2[j][i] = '.';
            pos--;
        }
    }

    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < n; j++)
        {
            m[i][j] = m2[i][j];
            //printf("%c", m2[i][j]);
        }
        //printf("\n");
    }
    //printf("\n");
}

void judge()
{
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < n; j++)
        {
            char c = m[i][j];
            if(c == '.') continue;
            bool f = 0;
            int kk;
            for(kk = 1; kk < k; kk++)
            {
                if(j + kk >= n || m[i][j+kk] != c) break;
            }
            if(kk == k) f = 1;
            for(kk = 1; kk < k; kk++)
            {
                if(i + kk >= n || m[i+kk][j] != c) break;
            }
            if(kk == k) f = 1;
            for(kk = 1; kk < k; kk++)
            {
                if(j + kk >= n || i + kk >= n || m[i+kk][j+kk] != c) break;
            }
            if(kk == k) f = 1;
            for(kk = 1; kk < k; kk++)
            {
                if(j + kk >= n || i - kk >= n || m[i-kk][j+kk] != c) break;
            }
            if(kk == k) f = 1;
            if(f)
            {
                if(c == 'R') r = 1;
                else b = 1;
            }
        }
    }
}

void solve(int tcase)
{
    r = b = 0;
    rotate();
    judge();

    printf("Case #%d: ", tcase);
    if(r && b) printf("Both\n");
    if(!r && !b) printf("Neither\n");
    if(r && !b) printf("Red\n");
    if(!r && b) printf("Blue\n");
}

int main()
{
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    int T;
    cin>>T;

    for(int i = 1; i <= T; i++)
    {
        init();
        solve(i);
    }
}
