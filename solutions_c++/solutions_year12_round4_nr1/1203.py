#include <cstdio>
#include <vector>
#include <utility>
#include <algorithm>
#include <cstdlib>

using namespace std;

int main()
{
    int t;
    scanf("%d", &t);
    for(int lp=1;lp<=t;++lp)
    {
        int n;
        scanf("%d", &n);
        vector<pair<int,int>> vines(n);
        for(auto& p : vines)
        {
            scanf("%d %d", &p.first, &p.second);
        }
        
        int d;
        scanf("%d", &d);
        vines.push_back(make_pair(d,0));
        ++n;
        
        vector<int> maxlen(n, -1);
        maxlen[0] = min(vines[0].second, vines[0].first);
        int cvine = 0;
        
        for(int i=0;i<n;++i)
        {
            for(int j=i+1;j<n;++j)
            {
                if(vines[j].first <= vines[i].first + maxlen[i])
                {
                    maxlen[j] = max(maxlen[j], min(vines[j].second, abs(vines[i].first - vines[j].first)));
                }
            }
        }
        
        printf("Case #%d: %s\n", lp, (maxlen[n-1] >= 0) ? "YES" : "NO");
        
    }
    
    return 0;
}