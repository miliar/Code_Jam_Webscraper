#include <cstdio>
#include <string>
#include <algorithm>
#include <map>

using namespace std;

map<char,int> mp;

int main()
{
//        freopen("in.in","r",stdin);
        freopen("ou.ou","w",stdout);
        int end;
        scanf("%d\n",&end);
        char str[100];

        for(int rend=0;rend < end;rend++)
        {
                gets(str);        
                mp.clear();
                int n = strlen(str);
                int c = 1;
                int flag = 0;
                int i;
                for(i=0;i<n;i++)
                {
                        if(mp.find(str[i]) == mp.end())
                        {
                                if(c == 2 && !flag)
                                {
                                        mp[str[i]] = 0;
                                        flag = 1;
                                }
                                else
                                {
                                        mp[str[i]] = c++;
                                }
                        }
                }
                long long res = 0;
                for(i=0;i<n;i++)
                {
                        res = res * c + mp[str[i]];        
                }
                printf("Case #%d: %lld\n",rend+1,res);

        }

        return 0;
}