#include<iostream>
#include<string>
#include<cmath>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
using namespace std;

int s[1000010];
int c, d;
int p[300], v[300];

bool check(double t)
{
    double sp, ep, dis;
    int i;
    for(i = 0; i < c; i++)
    {
        if(i == 0)
        {
            sp = p[0] - t;
            ep = p[0] - t + (v[0] - 1.0) * d;
            if(ep - p[0] > t) return false;
            sp = ep + d;
        }
        else
        {
            if(p[i] < sp)
            {
                dis = sp - p[i];
                if(dis > t) return false;
                ep = sp + (v[i] - 1.0) * d;
                if(ep - p[i] > t) return false;
            }
            else
            {
                sp = max(sp, p[i] - t);
                ep = sp + (v[i] - 1.0) * d;
                if(p[i] < ep && ep - p[i] > t) return false;
            }
            sp = ep + d;
        }   
    }
    return true;
}

int main()
{
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);
    
    int T, tt, i;
    double left, right, mid;
    scanf("%d", &T);
    for(tt = 1; tt <= T; tt++)
    {
        scanf("%d%d", &c, &d);
        for(i = 0; i < c; i++) scanf("%d%d", &p[i], &v[i]);
        left = 0; right = 1e20;
        while(right - left > 1e-7)
        {
            mid = (left + right) / 2;
            if(check(mid)) right = mid;
            else left = mid;
        }
        
        printf("Case #%d: %.6lf\n",tt, right);
    }
    
    return 0;
}
