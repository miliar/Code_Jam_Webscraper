#include <sstream>
#include <queue>
#include<stack>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <string.h>

using namespace std;

int used[140];
vector<int>opp[140];
map<int, int>mp[140];

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B.out", "w", stdout);
    int test, cas=1;
    scanf("%d", &test);
    while(test--)
    {
        int c, d, n, i, j;
        memset(used, 0, sizeof used);
        for(i=0;i<50;i++)
        {
            opp[i].clear();
            mp[i].clear();
        }
        scanf("%d", &c);
        for(i=0;i<c;i++)
        {
            char a, b, c;
            int aa, bb, cc;
            getchar();
            scanf("%c%c%c", &a, &b, &c);
            aa = a-'A', bb = b-'A', cc = c-'A';
            mp[aa][bb] = cc;
            mp[bb][aa] = cc;
        }
//        printf("inv done\n");
        scanf("%d", &d);
        for(i=0;i<d;i++)
        {
            char a, b;
            int aa, bb;
            getchar();
            scanf("%c%c", &a, &b);
            aa = a-'A', bb = b-'A';
            opp[aa].push_back(bb);
            opp[bb].push_back(aa);
        }
//        printf("opp done\n");
        scanf("%d", &n);
        stack<char>stk;
//        printf("ok \n");
        getchar();
        for(i=0;i<n;i++)
        {
            char a, b, c;
            scanf("%c", &a);
            if(!stk.empty())
            {
                b = stk.top();
                if(mp[a-'A'][b-'A']!=0 || mp[b-'A'][a-'A']!=0)
                {
                    c = mp[a-'A'][b-'A'] + 'A';
                    stk.pop();
                    stk.push(c);
                    used[b-'A']--;
                    used[c-'A']++;
                }
                else
                {
                    int lim = opp[a-'A'].size(), ok=0;
                    for(j=0;j<lim;j++)
                    {
//                        printf("a %c, b %c\n", a, opp[a-'A'][j]+'A');
//                        printf("opp %d, col %d\n", opp[a-'A'][j], used[opp[a-'A'][j]]);
                        if(used[opp[a-'A'][j]])
                        {
                            while(!stk.empty())
                                stk.pop();
                            memset(used, 0, sizeof used);
                            ok=1;
                            break;
                        }
                    }
                    if(ok==0)
                    {
                        stk.push(a);
                        used[a-'A']++;
                    }
                }
            }
            else
            {
                stk.push(a);
                used[a-'A']++;
            }
        }
        string ans;
        while(!stk.empty())
        {
            ans.push_back(stk.top());
            stk.pop();
        }
        int sz = ans.size();
        printf("Case #%d: [", cas++);
        for(i=sz-1;i>=0;i--)
        {
            if(i!=sz-1)
                printf(", ");
            printf("%c", ans[i]);
        }
        printf("]");
        printf("\n");
    }
    return 0;
}



