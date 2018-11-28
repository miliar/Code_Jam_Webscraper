
#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int T;
    scanf("%d",&T);
    for(int kCase=1;kCase<=T;kCase++)
    {
        int N;
        scanf("%d",&N);
        vector<int> arr(N);
        for(int i=0;i<N;i++)
        {
            scanf("%d",&arr[i]);
        }

        int sum = arr[0];
        int bsum = arr[0];
        int minv = arr[0];
        for(int i=1;i<N;i++)
        {
            sum += arr[i];
            bsum ^= arr[i];
            minv = min(minv, arr[i]);
        }
        
        if(bsum == 0)
        {
            printf("Case #%d: %d\n", kCase, sum - minv);
        }
        else
        {
            printf("Case #%d: NO\n", kCase);
        }
    }
}



namespace{
struct Test
{
    Test()
    {
        freopen("../Resource/C-large.in","r",stdin);
        freopen("../Resource/C-large.out","w",stdout);
    }

    ~Test()
    {
        //scanf("%*s");
    }
}g_Test;
}

