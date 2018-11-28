#include <cstdio>
#include <queue>

using namespace std;

queue<int> q;
queue<int> outQ;

int main()
{
    int t, r, k, n, g;

    scanf("%d", &t);
    
    for(int kase = 1; kase <= t; kase++)
    {
        long long int ret = 0;

        q = queue<int>();
        outQ = queue<int>();

        scanf("%d%d%d", &r, &k, &n);

        while(n--)
        {
            scanf("%d", &g);
            q.push(g);
        }

        while(r--)
        {
            int cap = k;
            bool increse = true;

            while(increse)
            {
                increse = false;
                if(!q.empty() && q.front() <= cap)
                {
                    int first = q.front();
                    cap -= first;
                    q.pop();
                    outQ.push(first);
                    increse = true;
                }
            }

            while(!outQ.empty())
            {
                q.push(outQ.front());
                outQ.pop();
            }

            ret += k-cap;
        }

        printf("Case #%d: %d\n", kase, ret);
    }


    return 0;
}
