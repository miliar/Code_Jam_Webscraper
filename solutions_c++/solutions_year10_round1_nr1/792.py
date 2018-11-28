#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<vector>
#include<algorithm>
#include<set>
#include<string>
#include<stack>
#include<queue>
#include<iostream>
#include<sstream>

using namespace std;

char board[55][55];

void rotate(int n)
{
    for(int row = 0; row < n; ++row)
    {
        for(int col = n-1; col >= 0; --col)
        {
            if(board[row][col] != '.')
            {
                // move to the right
                int c = col+1;
                
                while(c < n && board[row][c] == '.')
                {
                    board[row][c] = board[row][c-1];
                    board[row][c-1] = '.';
                    ++c;    
                }   
            }   
        }   
        
        //puts(board[row]);
    }   
}

bool outside(int r, int c, int n)
{
    if(r < 0 || r >= n || c < 0 || c >= n)
    return true;
       
    return false;
}

int check(int r, int c, int n, int dr, int dc)
{
    if(!outside(r+dr,c+dc,n) && board[r+dr][c+dc] == board[r][c])
        return 1 + check(r+dr,c+dc,n,dr,dc);
    else
        return 1;
}

int main()
{
    freopen("ALarge.in","r",stdin);
    freopen("ALarge.out","w",stdout);
    
    int T; scanf("%d",&T);
    
    for(int t = 1; t <= T; ++t)
    {
        int n, k;
        scanf("%d%d",&n,&k);
        
        for(int i = 0; i < n; ++i)
        scanf("%s",board[i]);
        
        rotate(n);    
        
        int dr[] = {0,  -1, -1, -1};
        int dc[] = {-1, -1,  0, 1};
        
        bool red_wins = false, blue_wins = false;
        
        // check for same colored row
        for(int r = 0; r < n; ++r)
        {
            for(int c = 0; c < n; ++c)
            {
                if(board[r][c] == '.') continue;
                
                for(int i = 0; i < 4; ++i)
                {
                    int max_same = check(r,c,n,dr[i],dc[i]);
                    
                    if(max_same >= k)
                    {
                        if(board[r][c] == 'B')
                        blue_wins = true;
                        else
                        red_wins = true;       
                    }
                }                  
            }   
        }
        
        printf("Case #%d: ",t);
        
        if(red_wins && blue_wins)
        {
            puts("Both");   
        }
        else if(!red_wins && !blue_wins)
        {
            puts("Neither");   
        }
        else if(red_wins)
            puts("Red");
        else
            puts("Blue");
    }
    
    return 0;
}
