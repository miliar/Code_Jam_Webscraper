#include <cstdio>
#include <queue>
using namespace std;
typedef long long int ll;
typedef pair<ll, int> P;
ll as[1024];

ll norm(ll n, ll c)
{
    n %= c;
    if(n < 0)
        n += c;

    return n;
}

int main()
{
    int T;
    scanf("%d", &T);

    for(int testnum = 1; testnum  <= T; testnum++)
    {
        priority_queue<P, vector<P>, greater<P> > que;

        int L, N, C;
        long long int t;
        scanf("%d%lld%d%d", &L, &t, &N, &C);
        for(int i = 1; i <= C; i++)
        {
            scanf("%lld", as + i);
            as[i] *= 2;
            as[i] += as[i - 1];
        }

        long long int total = (as[C] * (N / C) + as[N % C]);
        ll finish = t / as[C] * C;
        for(ll i = as[1], j = 1; i <= t % as[C]; i = as[++j], finish++);


        //ll mid = t / as[C];
        for(int i = 0; i < C; i++)
        {
            int s = i, e = (N - 1) / C * C + i;

            if(e >= N)
                e -= C;
               while(s > e);
          
            if(finish > e)
                que.push(P(0, (e - s) / C + 1));
            else if(finish < s)
                que.push(P(as[i + 1] - as[i], (e - s) / C + 1));
            else
            {
                ll m = finish - norm(finish % C - i, C);

                while(!(m <= finish && m + C >= finish && m % C == i % C));
                if(m == finish)
                    m -= C;

                if(m >= s)
                    que.push(P(0, (m - s) / C + 1));//, printf("11 %lld %d\n", m, s);
                
                m = finish + norm(i - finish % C, C);
                while(!(m >= finish && m - C <= finish && m % C == i % C));

                if(m == finish)
                {
                    ll tt = as[C] * (m / C) + as[i + 1]; 
                    que.push(P(tt - t, 1));//, printf("22 %lld\n", tt - t);
                    m += C;
                }

                if(m <= e)
                    que.push(P(as[i + 1] - as[i], (e - m) / C + 1));//, printf("33 %lld %d\n", m, e);
            }
        }


        while(N > L)
        {
            P p = que.top();
            que.pop();

            if(p.second <= N - L)
                N -= p.second;
            else
            {
                p.second -= N - L;
                N = L;
                que.push(p);
            }
        }
        
        int dd  = 0;
        while(que.size())
            total -= que.top().first * que.top().second / 2, dd += que.top().second, que.pop();

        printf("Case #%d: %lld\n", testnum, total);
    }
    return 0;
}
