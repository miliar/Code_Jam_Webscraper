#include <iostream>
#include <string>
using namespace std;

int ans;
string s;
int len;
string target = "welcome to code jam";

int record[500][19];

int solve(int x, int y)
{
    if (x >= len) {
        if (y == 19) return 1;
        else return 0;
    }    
    
    if (y == 19) return record[x][y] = 1;
    
    if (record[x][y] >= 0) return record[x][y];
    
    int ans = 0;
    
    for (int i = x; i < len; i++)
    {
        if (s[i] == target[y]) ans += solve(i + 1, y + 1) % 10000;
    }    
    return record[x][y] = ans % 10000;
}    

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    scanf("%d\n", &t);
    char ss[10000];
    for (int i = 0; i < t; i++)
    {
        gets(ss);
        s = ss;
        len = s.size();
        memset(record, -1, sizeof(record));
        ans = solve(0, 0);           
        printf("Case #%d: %04d\n", i + 1, ans);
    }
        
}    
