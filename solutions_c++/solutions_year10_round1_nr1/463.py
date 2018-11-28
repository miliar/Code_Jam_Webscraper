
#include<stdio.h>
#include<string.h>

char str[55][55], rot[55][55];
int n, k;
void rota() {
    memset(rot, '.', sizeof(rot));
    for(int r = n - 1; r >= 0; r--) 
    {
        int rr = n - 1;
        for(int c = n - 1; c >= 0; c--) if(str[r][c] != '.')
         {
            rot[rr--][n - r - 1] = str[r][c];
        }
    }
   
}
bool judge(char c)
 {
    for(int i = 0; i < n; i++) 
    {
        int tot = 0;
        for(int j = 0; j < n; j++) 
        {
            if(rot[i][j] == c) 
            {
                tot++;
                if(tot == k) return true;
            } 
            else 
            {
                tot = 0;
            }
        }
    }
    for(int j = 0; j < n; j++) {
        int tot = 0;
        for(int i = 0; i < n; i++) {
            if(rot[i][j] == c) {
                tot++;
                if(tot == k) return true;
            } else {
                tot = 0;
            }
        }
    }
    for(int j = 0; j < 2 * n - 1; j++) {
        int row, col;
        if(j < n) 
        {
            row = 0;
            col = j;
        } 
        else 
        {
            row = n - j + 1;
            col = n - 1;
        }
        int tot = 0;
        while(row < n && col >= 0) 
        {
            if(rot[row][col] == c) 
            {
                tot++;
                if(tot == k) return true;
            } 
            else 
            {
                tot = 0;
            } 
            row++;
            col--;
        }
    }
    for(int j = n - 1; j >= -(n - 1); j--) 
    {
        int row, col;
        if(j >= 0) 
        {
            row = 0;
            col = j;
        } 
        else 
        {
            row = -j;
            col = 0;
        }
        int tot = 0;
        while(row < n && col < n) 
        {
            if(rot[row][col] == c) 
            {
                tot++;
                if(tot == k) return true;
            } else {
                tot = 0;
            }
            row++;
            col++;
        }
    }
    return false;
}
int main() {
    int t;
    int Case = 1;
    freopen("A-small-attempt1.in","r",stdin);
    freopen("a1.out","w",stdout);
    scanf("%d",&t);
    while(t--) {
        scanf("%d%d",&n,&k);
        for(int i = 0; i < n; i++) scanf("%s",str[i]);
        rota();
        bool red = judge('R');
        bool blue = judge('B');
        if(!red && !blue) 
        {
            printf("Case #%d: Neither\n", Case++);
        } 
        else if(red && blue) 
        {
            printf("Case #%d: Both\n", Case++);
        } 
        else if(red) 
        {
            printf("Case #%d: Red\n", Case++);
        } 
        else 
        {
            printf("Case #%d: Blue\n", Case++);
        }
    }
    return 0;
}
        
