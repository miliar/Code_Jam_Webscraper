#include <iostream>
#include <cstring>
#include <string>
using namespace std;

const int N = 510;
const int M = 20;
const int MOD = 10000;
const string need = "welcome to code jam";

char s[N];
int res[M];

void solve(int tcase)
{
    gets(s);
    //puts(s);
    memset(res, 0 , sizeof(res));

    int len = strlen(s);
    for(int i = 0; i < len; i++)
    {
        int ss = need.size();
        for(int j = 0; j < ss; j++)
        {
            if(s[i] != need[j]) continue;
            if(!j) res[j]++;
            else res[j] += res[j-1];
            res[j] %= MOD;
        }
    }
    printf("Case #%d: %04d\n", tcase, res[need.size()-1]);
}

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    cin>>T;
    getchar();
    for(int i = 1; i <= T; i++)
    {
        solve(i);
    }
}
