#include<cstdio>
#include<queue>

#define ll long long

long long t;
long long r, k, n;
std::queue<long long> q;
std::queue<long long> rc;
long long actrc;

void solve(long long t)
{
    long long i,j;
    long long res=0;

    scanf("%lld%lld%lld", &r, &k, &n);
    for(i=0; i<n; i++)
    {
        long long gs;
        scanf("%lld", &gs);
        q.push(gs);
    }

    for(i=0; i<r; i++)
    {
        // fill the rc
        actrc=0;
        while(!q.empty())
        {
            if(actrc+q.front()<=k)
            {
                rc.push(q.front());
                actrc+=q.front();
                q.pop();
            }
            else
            {
                // no more passangers
                break;
            }
        }
        res += actrc;

        // get rc long longo q
        while(!rc.empty())
        {
            q.push(rc.front());
            rc.pop();
        }
    }

    while(!q.empty())
        q.pop();

    printf("Case #%lld: %lld\n", t, res);
}

int main()
{
    long long i;

    scanf("%lld", &t);

    for(i=1; i<=t; i++)
    {
        solve(i);
    }

    return 0;
}
