#include<cstdio>
#include<vector>
#include<algorithm>
#include<cassert>
#define MP make_pair
#define F first
#define S second
#define MAX 1005

using namespace std;

pair<int, int> arr[MAX];
pair<int, int> ans[MAX];
int main()
{
    int z;
    scanf("%d", &z);

    for(int zi=1; zi<=z; zi++)
    {
        int n, W, L;
        scanf("%d %d %d", &n, &W, &L);

        for(int i=0; i<n; i++)
        {
            int r;
            scanf("%d", &r);

            arr[i] = MP(r, i);
        }

        sort(arr, arr+n);

        bool flag = 0;
        if(W < L)
            swap(W, L), flag = 1;

        int nowW = INT_MIN;
        for(int i=n-1; i>=0;)
        {
            int nowL = INT_MIN;
            int w = max(arr[i].F + nowW, 0);
            nowW = w + arr[i].F;

            while(i>=0)
            {
                int l = max(arr[i].F + nowL, 0);
                nowL = l + arr[i].F;

                if(l > L)
                    break;

                ans[ arr[i].S ] = MP( w, l );
                i--;
            }
            assert(nowW <= W);
        }
        printf("Case #%d:", zi);
        for(int i=0; i<n; i++)
        {
            if(flag)
                printf(" %d %d", ans[i].S, ans[i].F);
            else
                printf(" %d %d", ans[i].F, ans[i].S);
        }
        printf("\n");
    }
}
