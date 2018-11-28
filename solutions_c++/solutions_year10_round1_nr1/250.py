#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
#define tiao system("pause")

char s[55][55];
int n;
int k;
char tmp[55][55];


bool can(char color)
{
    int i,j,ci,cici,cicici;
    
    for (i=0; i<n; i++)
    {
        j = 0;
        while(j < n)
        {
            for (; j<n; j++) if (s[i][j] == color) break;
            int cnt = 0;
            for (; j<n; j++) 
            {
                if (s[i][j] == color) cnt++;
                else break;
            }
            
            if (cnt >= k) return true;
        }
    }    
    
    for (j=0; j<n; j++)
    {
        i = 0;
        while(i < n)
        {
            for (; i<n; i++) if (s[i][j] == color) break;
            int cnt = 0;
            for (; i<n; i++)
            {
                if (s[i][j] == color) cnt++;
                else break;
            }
            
            if (cnt >= k) return true;
        }
    }
    
    for (j=0; j<n; j++)
    {
        int x = 0, y = j;
        while(x < n && y < n)
        {
            for (; x<n && y<n; x++, y++) if (s[x][y] == color) break;
            int cnt = 0;
            for (; x<n && y<n; x++, y++)
            {
                if (s[x][y] == color) cnt++;
                else break;
            }
            
            if (cnt >= k) return true;
        }
    }
    for (i=0; i<n; i++)
    {
        int x = i, y = 0;
        while(x < n && y < n)
        {
            for (; x<n && y<n; x++, y++) if (s[x][y] == color) break;
            int cnt = 0;
            for (; x<n && y<n; x++, y++)
            {
                if (s[x][y] == color) cnt++;
                else break;
            }
            
            if (cnt >= k) return true;
        }
    }
    
    for (j=0; j<n; j++)
    {
        int x = 0, y = j;
        while(x < n && y >= 0)
        {
            for (; x<n && y>=0; x++, y--) if (s[x][y] == color) break;
            int cnt = 0;
            for (; x<n && y>=0; x++, y--)
            {
                if (s[x][y] == color) cnt++;
                else break;
            }
            
            if (cnt >= k) return true;
        }
    }
    for (i=0; i<n; i++)
    {
        int x = i, y = n-1; // ÎÒÊÇdb!!! 
        while(x < n && y >= 0)
        {
            for (; x<n && y>=0; x++, y--) if (s[x][y] == color) break;
            int cnt = 0;
            for (; x<n && y>=0; x++, y--)
            {
                if (s[x][y] == color) cnt++;
                else break;
            }
            
            if (cnt >= k) return true;
        }
    }
    
    return false;
}

void print(char s[55][55])
{
    for (int i=0; i<n; i++)
    {
        for (int j=0; j<n; j++)
            cout << s[i][j] ;
        cout << endl;
    }
    cout << endl;
}
int main(void)
{
    int i,j,ci,cici,cicici;
    int t;
        
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);    

    scanf("%d", &t);
    for (cicici=1; cicici<=t; cicici++)
    {
        scanf("%d%d", &n, &k);
        for (i=0; i<n; i++) scanf("%s", s[i]);
        
        
        for (i=0; i<n; i++) 
            for (j=0; j<n; j++)
                tmp[j][n-1-i] = s[i][j];
        memcpy(s, tmp, sizeof(s));

        for (cici=0; cici<n; cici++)
        {
            for (j=0; j<n; j++)
            {
                for (i=n-1; i>0; i--)
                {
                    if (s[i][j] == '.')
                    {
                        swap(s[i][j], s[i-1][j]);
                    }
                }
            }
        }
        
        bool red = can('R');
        bool blue = can('B');
        
        if (red && blue) printf("Case #%d: Both\n", cicici);
        else if (red && !blue) printf("Case #%d: Red\n", cicici);
        else if (!red && blue) printf("Case #%d: Blue\n", cicici);
        else printf("Case #%d: Neither\n", cicici);        
    }
//    tiao;
    return 0;
}
