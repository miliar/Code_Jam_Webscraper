#include<iostream>
#include<cstdio>
#include<vector>

using namespace std;

int c, d, n;
char ct[200][200];
bool dt[200][200];
vector<char> v;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int Ti = 1; Ti <= T; ++Ti)
    {
        memset(ct, 0, sizeof ct);
        memset(dt, 0, sizeof dt);
        v.clear();
        scanf("%d", &c);
        while(c--)
        {
            char s[10];
            scanf(" %s", s);
            ct[s[0]][s[1]] = s[2];
            ct[s[1]][s[0]] = s[2];
        }
        scanf("%d", &d);
        while(d--)
        {
            char s[10];
            scanf(" %s", s);
            dt[s[0]][s[1]] = 1;
            dt[s[1]][s[0]] = 1;
        }
        scanf("%d", &n);
        while(n--)
        {
            char e;
            scanf(" %c", &e);
            if(v.empty())
                v.push_back(e);
            else
            {
                char ch = ct[v.back()][e];
                if(ch)
                {
                    v.pop_back();
                    v.push_back(ch);
                }
                else
                {
                    int ok = 1;
                    for(int i = 0; i < v.size(); ++i)
                        if(dt[v[i]][e])
                        {
                            v.clear();
                            ok = 0;
                            break;
                        }
                    if(ok)
                        v.push_back(e);
                }
            }
        }
        printf("Case #%d: [", Ti);
        for(int i = 0; i < (int)v.size() - 1; ++i)
            printf("%c, ", v[i]);
        if(v.size())
            printf("%c", v[v.size()-1]);
        printf("]\n");
    }
    return 0;
}
