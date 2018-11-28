#include <iostream>
#include <map>
#include <sstream>
using namespace std;
const int MAXN = 101;
map<string,int> mp[MAXN];
int main()
{
    //freopen("A-small-attempt0.in","r",stdin);
    //freopen("A-small-attempt0.out","w",stdout);
    
    int cas,n,m;
    string s;
    scanf("%d",&cas);
    for (int T = 1;T <= cas;T++)
    {
        scanf("%d%d",&n,&m);
        for (int i = 0;i < MAXN;i++)
            mp[i].clear();
        for (int i = 0;i < n;i++)
        {
            cin >> s;
            int l = s.size();
            for (int j = 0;j < l;j++)
                if (s[j] == '/')
                    s[j] = ' ';
            istringstream sin(s);
            int t = 0;
            string tmp;
            while (sin >> tmp)
                mp[t++][tmp] = 1;
        }
        int ans = 0;
        for (int i = 0;i < m;i++)
        {
            cin >> s;
            int l = s.size();
            for (int j = 0;j < l;j++)
                if (s[j] == '/')
                    s[j] = ' ';
            istringstream sin(s);
            int t = 0,cnt = 0;
            string tmp;
            bool flag = 0;
            while (sin >> tmp)
            {
                if (mp[t][tmp] != 1)
                    flag = 1;
                if (flag)
                {
                    mp[t][tmp] = 1;
                    cnt++;
                }
                t++;
            }
            ans += cnt;
        }
        printf("Case #%d: %d\n",T,ans);
    }
}
