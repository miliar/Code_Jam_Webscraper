#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;

typedef long long LL;

int C, D;
int V[256], P[256];

double help[1000001];

bool can(double test)
{
    int num = 1;
    help[0] = P[0] - test;
    for (int i = 0; i < C; i++)
    {
        for (int j = 0; j < V[i]; j++)
        {
            if (i == 0 && j == 0) continue;
            double where = help[num - 1];
            
            if (P[i] > where)
            {
                double dist = P[i] - where;
                if (dist > D) { help[num] = P[i] - min(test, (dist - D)); num++; };    
                if (dist < D) { help[num] = P[i] + min(test, (D - dist)); num++; }
            }
            else
            {
                double one = P[i] + test;
                if (one - where > D) one -= (one - where - D);
                help[num] = one; 
                num++;
            }
        }    
    }
    
    for (int i = 0; i < num; i++)
    {
        bool l = true, r = true;
        if (i > 0 && help[i] - help[i - 1] < D) l = false;
        if (i < num - 1 && help[i + 1] - help[i] < D) r = false;
    
        if (!l || !r) return false;
    }
    
    return true;
}

double solve()
{
    double l = 0, r = 1000000000;
    
    for (int i = 0; i < 100; i++)
    {
        double mid = (l + r) / 2.;
        
        //mid = 2.7;
        if (can(mid)) r = mid; else l = mid;
        //cout << mid << " ";
        //break;
    }
    
    return r;
}

int main()
{
    int T; cin >> T;
    
    for (int t = 1; t <= T; t++)
    {        
        cin >> C >> D;
        for (int i = 0; i < C; i++)
            cin >> P[i] >> V[i];
            
        double res = solve();
        printf("Case #%d: %.8lf\n", t, res);
    }      
    
    return 0;
}
