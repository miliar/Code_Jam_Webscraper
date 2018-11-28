#include <algorithm>
#include <string>
#include <cstdio>
#include <map>
#include <vector>
#define X first
#define Y second
#define FOREACH(c, it) for(typeof(c.begin()) it = c.begin(); it != c.end(); ++it)

using namespace std;

int main() {
    int ncase;
    scanf("%d", &ncase);
    map<long long, long long> sols;
    map<long long, long long> sols_;    
    for (int icase = 0; icase < ncase; ++icase) {
        long long n, m, x, y, z;
        scanf("%lld %lld %lld %lld %lld", &n, &m, &x, &y, &z);
        vector<long long> a(m);
        
        for (int i = 0; i < m; ++i)
            scanf("%lld", &a[i]);
            
        sols.clear();
            
        for (long long i = 0; i < n; ++i) {
            sols_.clear();
            long long act = a[i % m];
            //printf(" %lld\n", act);
            FOREACH(sols, it) {
                sols_[it->X] = (sols_[it->X] + it->Y) % 1000000007;
                if (act > it->X) {
                    sols_[act] = (sols_[act] + it->Y) % 1000000007;
                }
            
            }
            sols_[act] = (sols_[act] + 1) % 1000000007;
            sols.clear();
            FOREACH(sols_, it)
                sols[it->X] = it->Y;
            
            a[i % m] = (x * a[i % m] + y * (i + 1)) % z;
            
            /*FOREACH(sols, it)
                printf("x %lld %lld %lld\n", i, it->first, it->second);*/
        }

        long long sol = 0;
        FOREACH(sols, it) {
            sol = (sol + it->Y) % 1000000007;
        }
        
        printf("Case #%d: %lld\n", icase+1, sol);
    }
    return 0;
}
