#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

#define REP(i,n) for (__typeof(n) i=0;i!=(n);++i)
#define FOR(i,a,b) for(__typeof(a) i=a;i<=b;++i)

int main()
{
        int T,N,S,P;
        scanf("%d",&T);
        REP(i,T)
        {
                scanf("%d%d%d",&N,&S,&P);
                int ans(0);
                REP(j,N)
                {
                        int sum;
                        scanf("%d",&sum);
                        bool IsSurprise(false),valid(false);
                        FOR(best,P,10) 
                        {
                                int start=max(0,best-2);
                                FOR(first,start,best) 
                                        FOR(second,start,best)
                                                if (first+second+best==sum)
                                                {
                                                        if (second==best-2 || first==best-2) IsSurprise=true;
                                                        else valid=true;
                                                }
                        }
                        if (valid) ans++;
                        else if (IsSurprise && S) ++ans,--S;
                }
                printf("Case #%d: %d\n",i+1,ans);
        }
        return 0;
}
