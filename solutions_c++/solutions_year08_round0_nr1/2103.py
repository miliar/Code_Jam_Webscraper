#include <iostream>
#include <map>
#include <string>
using namespace std;

int n, m, t, index;
char eg[100][101];
char words[1000][101];

int r[1000];
int memo[1001][100];
map<string, int> ms;

void input()
{
    ms.clear();
    scanf("%d\n", &n);
    for (int i = 0; i < n; i++)
    {
        gets(eg[i]);
        ms.insert(make_pair(eg[i], i));
    } 
    scanf("%d\n", &m);
    for (int i = 0; i < m; i++)
    {
        gets(words[i]);
    } 
}    

void getR()
{
    memset(r, -1, sizeof(r));
    for (int i = 0; i < m; i++)
    {
        map<string, int>::iterator it = ms.find(words[i]);
        if (it != ms.end()) r[i] = it->second;
    }    
}    

void solve()
{
    getR();
    memset(memo, 0, sizeof(memo));
    for (int i = 1; i <= m; i++)
    {
        int x = r[i - 1];
        if (x >= 0) memo[i][x] = -1;
        for (int j = 0; j < n; j++)
        {
            if (j == x) continue;
            int __min = 10000;
            for (int k = 0; k < n; k++)
            {
                if (memo[i - 1][k] < 0) continue;
                if (k == j) 
                {
                    if (memo[i - 1][k] < __min) __min = memo[i - 1][k];
                }    
                else 
                {
                    if (i != 1)
                    {
                        if (memo[i - 1][k] + 1 < __min)
                        {
                            __min = memo[i - 1][k] + 1;
                        } 
                    } else if (memo[i - 1][k] < __min) __min = memo[i - 1][k];  
                }         
            }  
            memo[i][j] = __min;  
        }      
    } 
    int ans = 10000;
    for (int i = 0; i < n; i++)
    {
        if (memo[m][i] < ans && memo[m][i] >= 0) ans = memo[m][i];
    }      
    printf("Case #%d: %d\n", ++index, ans);
}    

int main()
{
    //freopen("in.txt", "r", stdin);
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &t);
    while (t--)
    {
        input();
        solve();
    }  
}    
