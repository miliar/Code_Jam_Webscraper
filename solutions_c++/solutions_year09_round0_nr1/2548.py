#include <iostream>
#include <string>
using namespace std;

const int N = 5010;

int l, d, n;
string s[N];

void init()
{
    for(int i = 1; i <= d; i++)
        cin>>s[i];
}

bool f[23][27];

bool check(string ss)
{
    for(int i = 0; i < l; i++)
    {
        int c = ss[i] - 'a';

        //for(int k = 0; k < 26; k++) printf("%d ",f[i][k]); printf("\n");

        if(!f[i][c])
            return 0;
    }
    return 1;
}

void solve()
{
    for(int i = 1; i <= n; i++)
    {
        string ss;
        cin>>ss;
        //cout<<ss<<endl;
        memset(f, 0, sizeof(f));
        int pla = 0;
        for(int j = 0; j < l; j++)
        {
            if(ss[pla] != '(')
            {
                //cout<<ss[pla]<<endl;
                f[j][ss[pla] - 'a'] = 1;
            }
            else
            {
                while(1)
                {
                    pla++;
                    if(ss[pla] == ')') break;
                    //cout<<ss[pla]<<endl;
                    f[j][ss[pla] - 'a'] = 1;
                }
            }
            pla++;
            //for(int k = 0; k < 26; k++) printf("%d ",f[j][k]); printf("\n");
        }
        int res = 0;\
        for(int j = 1; j <= d; j++)
        {
            if(check(s[j])) res++;
        }
        printf("Case #%d: %d\n", i, res);
    }
}

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    while(cin>>l>>d>>n)
    {
        init();
        solve();
    }
}
