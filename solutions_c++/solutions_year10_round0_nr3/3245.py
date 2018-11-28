#include <cstdio>
#include <queue>

using namespace std;

queue<int> Q;

int main()
{
    int tests;
	freopen("C-small-attempt0.in","r",stdin);
	freopen("tp.out","w",stdout);
	scanf("%d",&tests);
	for (int knt=1; knt<=tests; knt++)
    {
        int r,k,n,rez=0;
        scanf("%d%d%d",&r,&k,&n);
        for (int i=1; i<=n; i++)
        {
            int nr;
            scanf("%d",&nr);
            Q.push(nr);
        }
        while (r--)
        {
            int s=0;
            for (int kont=0; s+Q.front()<=k && kont+1<=n; kont++)
            {
                s+=Q.front();
                Q.push(Q.front());
                Q.pop();
            }
            rez+=s;
        }
        printf("Case #%d: %d\n",knt,rez);

        for (; !Q.empty(); Q.pop());
    }

    return 0;
}
