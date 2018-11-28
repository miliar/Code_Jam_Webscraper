#include <iostream>
#include <string>
using namespace std;

const int N = 5010;

int l, d, n;
string s[N];
bool Hash[23][27];

bool judge(string needtojudge)
{
    for(int i = 0; i < l; i++)
    {
        int now = needtojudge[i] - 'a';

        if(!Hash[i][now])
            return 0;
    }
    return 1;
}

void solve()
{
    for(int i = 1; i <= n; i++)
    {
        string now;
        cin>>now;
        memset(Hash, 0, sizeof(Hash));

        int pla = 0;
        for(int j = 0; j < l; j++)
        {
            if(now[pla] != '(')
            {
                Hash[j][now[pla] - 'a'] = 1;
            }
            else
            {
                while(1)
                {
                    pla++;
                    if(now[pla] == ')') break;
                    Hash[j][now[pla] - 'a'] = 1;
                }
            }
            pla++;
        }
        int res = 0;
        for(int j = 1; j <= d; j++)
        {
            if(judge(s[j])) res++;
        }
        printf("Case #%d: %d\n", i, res);
    }
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    while(cin>>l>>d>>n)
    {
        for(int i = 1; i <= d; i++)
            cin>>s[i];
        solve();
    }
}
