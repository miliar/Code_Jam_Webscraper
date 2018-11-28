#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <string>
#include <cstring>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <iomanip>
#include <sstream>
#include <algorithm>


using namespace std;


struct Node
{
    int l;
    int speed;

    bool operator <(const Node &a) const
    {
        return this->speed < a.speed;
    }
};

Node node[1001];


int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for(int ti = 1; ti <= t; ++ti)
    {
        int x, s, r, tt, n;
        cin >> x >> s >> r >> tt >> n;
        node[0].speed = s;
        node[0].l = x;
        for(int i = 1; i <= n; ++i)
        {
            int b, e, w;
            cin >> b >> e >> w;
            node[i].l = e - b;
            node[i].speed = w + s;
            node[0].l -= (e - b);
        }
        sort(node, node + n + 1);
        double an = 0.0;
        double leave = tt;
        for(int i = 0; i <= n; ++i)
        {
            if(leave > 1e-8)
            {
                double rr = r + node[i].speed - s;
                double canUse = node[i].l / rr;
                if(canUse < leave)
                {
                    an += canUse;
                    leave -= canUse;
                }
                else
                {
                    an += leave;                    
                    an += (node[i].l - leave * rr) / node[i].speed;
                    leave = 0.0;
                }
            }
            else
                an += node[i].l * 1.0 / node[i].speed;
        }

        printf("Case #%d: ", ti);
        printf("%.9lf\n", an);
    }

    return 0;
}
