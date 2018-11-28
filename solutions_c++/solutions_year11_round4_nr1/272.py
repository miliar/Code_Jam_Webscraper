#include <cstdio>
#include <algorithm>
using namespace std;

struct way
{
    int L, W;
    
    bool operator<(const way& a) const
    {
        return W < a.W;
    }
};

const int MAXN = 1100;
way ways[MAXN];

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("outa_l.txt", "w", stdout);
    int T, X, S, R, ti, N, sum;
    scanf("%d", &T);
    
    for(int t = 1; T--; ++t)
    {
        sum = 0;
        scanf("%d%d%d%d%d", &X, &S, &R, &ti, &N);
        for(int i = 0; i < N; i++)
        {
            int B, E;
            scanf("%d%d%d", &B, &E, &ways[i].W);
            ways[i].L = E-B;
            sum += E-B;
        }
        
        ways[N].W = 0, ways[N].L = X-sum;
        ++N;
        double tsum = 0, ans = 0;
        sort(ways, ways+N);
        
        for(int i = 0; i < N; i++)
        {
            double ttemp = ways[i].L/(double)(ways[i].W+R), ttemp2, r;
            
            if(ttemp+tsum <= ti)
                tsum += ttemp, ans += ttemp;
            else
            {
                ttemp = ti-tsum;
                r = ways[i].L-ttemp*(ways[i].W+R);
                ttemp2 = r/(ways[i].W+S);
                
                tsum += ttemp;
                ans += ttemp+ttemp2;
            }
        }
        
        printf("Case #%d: %.7f\n", t, ans);
    }
    return 0;
}
