#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

string s, u = "welcome to code jam";

int memo[500][20];

int f(int a, int b)
{
    if(b==19) return 1;
    if(a==s.size()) return 0;
    
    if(memo[a][b]!=-1) return memo[a][b];
    
    int x = 0;
    
    for(int p=a; p<s.size(); p++)
    {
        if(s[p]==u[b])
        {
            x = (x + f(p+1, b+1))%10000;
        }
    }
    
    memo[a][b] = x;
    return x;
}

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    int N;
    cin>>N;
    
    getline(cin, s);
    
    for(int nCaso = 1; nCaso <= N; nCaso++)
    {
        memset(memo, -1, sizeof(memo));
        getline(cin, s);
        printf("Case #%d: %0.4d\n", nCaso, f(0, 0)%10000);
    }
    
    return 0;
}
