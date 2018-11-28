#include<iostream>
#include<cstdio>
#include<vector>

using namespace std;

int n;
vector<int> v, o, b;
int sol = 0;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int Ti = 1; Ti <= T; ++Ti)
    {
        v.clear();
        o.clear();
        b.clear();
        scanf("%d", &n);
        for(int i = 0; i < n; ++i)
        {
            char r;
            int k;
            scanf(" %c %d", &r, &k);
            v.push_back(r == 'O');
            if(r == 'O')
                o.push_back(k);
            else
                b.push_back(k);
        }
        sol = 0;
        int op = 1, bp = 1;
        int ok = 0, bk = 0;
        for(int i = 0; i < n; ++i)
            if(v[i])
            {
                int d = abs(op - o[ok]) + 1;
                if(bk < b.size())
                {
                    if(bp < b[bk])
                        bp += min(d, b[bk] - bp);
                    else
                        bp -= min(d, bp - b[bk]);
                }
                op = o[ok++];
                sol += d;
            }
            else
            {
                int d = abs(bp - b[bk]) + 1;
                if(ok < o.size())
                {
                    if(op < o[ok])
                        op += min(d, o[ok] - op);
                    else
                        op -= min(d, op - o[ok]);
                }
                bp = b[bk++];
                sol += d;
            }
        printf("Case #%d: %d\n", Ti, sol);
    }
    return 0;
}
