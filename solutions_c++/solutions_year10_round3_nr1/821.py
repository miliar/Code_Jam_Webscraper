#include <iostream>
#include <vector>

using namespace std;

#define f first
#define s second

int n, t;
vector<pair<int,int> > v;
    
int main()
{
    
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    
    cin >> t;

    for (int tt = 1; tt <= t; ++tt)
    {
        cin >> n;
        v.clear();
        for (int i = 1; i <= n; ++i)
        {
            int ai, bi;
            cin >> ai >> bi;
            v.push_back(make_pair(ai, bi));
        }
        
        int cnt = 0;
        
        for (int i = 0; i + 1 < n; ++i)
        {
            for (int j = i + 1; j < n; ++j)
                if ( ( v[i].f < v[j].f && v[i].s > v[j].s ) || (v[i].f > v[j].f && v[i].s < v[j].s) )
                   ++cnt;
        }
        
        cout << "Case #" << tt << ": " << cnt << "\n";
    }
    
    return 0;   
}
