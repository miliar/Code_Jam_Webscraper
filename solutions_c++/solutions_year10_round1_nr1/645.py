#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
using namespace std;

const int MAXN = 100;
char ori[MAXN][MAXN], res[MAXN][MAXN];
int N, K;

bool chk(int row, int col)
{
    //vertical
    if(row+K-1 < N)
    {
        bool flag = true;
        for(int i = 1; i < K && flag; i++)
            if(res[row][col] != res[row+i][col])
                flag = false;
        if(flag) return true; 
    }
    //horizontal
    if(col+K-1 < N)
    {
        bool flag = true;
        for(int i = 1; i < K && flag; i++)
            if(res[row][col] != res[row][col+i])
                flag = false;
        if(flag) return true; 
    }
    
    //diagonally
    if(col+K-1 < N && row+K-1 < N)
    {
        bool flag = true;
        for(int i = 1; i < K && flag; i++)
            if(res[row][col] != res[row+i][col+i])
                flag = false;
        if(flag) return true; 
    }
    
    if(row+K-1 < N && col-K+1 >= 0)
    {
        bool flag = true;
        for(int i = 1; i < K && flag; i++)
            if(res[row][col] != res[row+i][col-i])
                flag = false;
        if(flag) return true; 
    }
    
    return false;
}

void gravity()
{
    for(int i = N-1; i >= 0; i--)
        for(int j = N-1; j >= 0; j--)
            if(res[i][j] == 'R' || res[i][j] == 'B')
            {
                int k = i;
                while(k < N-1)
                    if(res[k+1][j] == '.')
                        k++;
                    else
                        break;
                res[k][j] = res[i][j];
                if(k != i) res[i][j] = '.';
            }
}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    cin>>T;
    
    for(int t = 0; t < T; t++)
    {
        cin>>N>>K;
        
        for(int i = 0; i < N; i++)
            for(int j = 0; j < N; j++)
                cin>>ori[i][j];
        for(int i = 0; i < N; i++)
            for(int j = 0; j < N; j++)
                res[i][j] = ori[N-j-1][i];
        gravity();
        
        bool rflag = false, bflag = false;
        
        for(int i = 0; i < N; i++)
            for(int j = 0; j < N; j++)
            {
                if(res[i][j] == 'R')
                {
                    if(chk(i,j)) rflag = true;
                }
                else if(res[i][j] == 'B')
                {
                    if(chk(i, j)) bflag = true;
                }
            }
        
        if(rflag && bflag) printf("Case #%d: Both\n", t+1);
        else if(rflag)     printf("Case #%d: Red\n", t+1);
        else if(bflag)     printf("Case #%d: Blue\n", t+1);
        else               printf("Case #%d: Neither\n", t+1);
    }
    return 0;
}
