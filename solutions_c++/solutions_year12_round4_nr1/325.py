#include<cstdio>
#include<vector>
#include<cassert>
#define MAX 50005
#define MP make_pair
#define F first
#define S second
using namespace std;

pair<int, int> arr[MAX];
int dis[MAX];
int main()
{
    int z;
    scanf("%d", &z);

    for(int zi=1; zi<=z; zi++)
    {
        int n;
        scanf("%d", &n);

        for(int i=0; i<n; i++)
        {
            int a, b;
            scanf("%d %d", &a, &b);

            arr[i] = MP(a, b);
        }
        int D;
        int t = scanf("%d", &D);
        assert(t == 1);
        arr[n++] = MP(D, 0); 

        memset(dis, -1, sizeof(dis));

        dis[0] = arr[0].F;
        for(int i=0; i<n; i++)
        {
            for(int j=i+1; j<n; j++)
            {
                int d = arr[j].F - arr[i].F;

                if(d > dis[i])
                    break;

                //int c = d;
                int c = min(d, arr[j].S);
                if(dis[j] == -1 || dis[j] < c)
                    dis[j] = c;
            }
        }
        printf("Case #%d: ", zi);
        if(dis[n-1] == -1)
            printf("NO\n");
        else
            printf("YES\n");
    }
}
