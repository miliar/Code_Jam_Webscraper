#include<iostream>
#include<cstdio>
#include<map>

using namespace std;

#define x first
#define y second

int x, s, r, n;
double to;
map<int,int> mp;
double sol;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int Ti = 1; Ti <= T; ++Ti)
    {
        scanf("%d %d %d %lf %d", &x, &s, &r, &to, &n);
        r -= s;
        mp.clear();
        mp[s] = x;
        while(n--)
        {
            int a, b, v;
            scanf("%d %d %d", &a, &b, &v);
            mp[s+v] += b - a;
            mp[s] -= b - a;
        }
        sol = 0;
        map<int,int>::iterator it;
        for(it = mp.begin(); it != mp.end(); ++it)
        {
            double tr = (double)it->y / ((double)it->x + r);
            if(tr > to)
            {
                sol += (double)to + ((double)it->y - (double)to * (it->x + r)) / (double)it->x;
                to = 0;
            }
            else
            {
                sol += tr;
                to -= tr;
            }
        }
        printf("Case #%d: %.9lf\n", Ti, sol);
    }
    return 0;
}
