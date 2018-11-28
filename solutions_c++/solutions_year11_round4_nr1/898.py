#include <stdio.h>
#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>

#define pb push_back
#define mp make_pair

using namespace std;

const double eps = 1e-9;

typedef pair<int, int> PII;

int x, s, r, t, n;
double was, rs, runt;
int sum;
vector< PII > v;

bool cmp(PII a, PII b)
{
    int v1, v2;
    if(a.second < 0) v1 = r;
    else v1 = a.second + r;
    
    if(b.second < 0) v2 = r;
    else v2 = b.second + r;
    
    return v1 < v2;
}

void init()
{
    v.clear();
    
    scanf("%d %d %d %d %d", &x, &s, &r, &t, &n);
    
    rs = (double)r;
    runt = (double)t;
    was = (double)s;
    
    sum = 0;
    for(int i = 0; i < n; i ++)
    {
        int b, e, w;
        scanf("%d %d %d", &b, &e, &w);
        v.pb(mp(e - b, w));
        sum += (e - b);
    }
    if(x - sum > 0) v.pb(mp(x - sum, -s));
    
    sort(v.begin(), v.end(), cmp);
}

void solve()
{
//    cout << endl;
    double ans = 0;
    
    for(int i = 0; i < v.size(); i ++)
    {
        double len = (double)v[i].first;
        double speed = (double)v[i].second;
        
//        cout << len << " " << speed << endl;
        
        if(speed >= -eps)
        {
//            cout << "1)\n";
            if(runt - len / (speed + rs) >= -eps)
            {
                ans += len / (speed + rs);
                runt -= len / (speed + rs);
            }
            else
            {
                ans += runt;
                
                len -= runt * (speed + rs);
                ans += len / (speed + was);
                
                runt = 0;
            }
        }
        else
        {
//            cout << "2)\n";
            if(runt - len / rs >= -eps)
            {
                ans += len / rs;
                runt -= len / rs;
            }
            else
            {
                ans += runt;
                
                len -= runt * rs;
                runt = 0;
                
                speed *= -1;
                ans += len / speed;
            }
        }
    }
    printf("%.7lf\n",ans);
}

void doit()
{
    init();
    solve();
}

int main()
{
    int T;
    scanf("%d", &T);
    for(int i = 1; i <= T; i ++)
    {
        printf("Case #%d: ", i);
        doit();
    }
    
    return 0;
}
