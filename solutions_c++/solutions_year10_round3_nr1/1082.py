#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<vector>
#include<string>
#include<map>
#include<list>
#include<stack>
#include<queue>
#include<algorithm>

using namespace std;

typedef struct point{
    int start,end,diff;
};
point arr[1001];

bool comp(point a, point b)
{
    return a.diff>b.diff;
}
int main(void)
{
    //freopen("A-small-attempt0.in","r",stdin);
    //freopen("A-small-attempt0.out","w",stdout);
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int t = 1; t<=T; t++)
    {
        int n;
        scanf("%d",&n);
        for(int i=0;i<n;i++)
        {
            scanf("%d%d",&arr[i].start,&arr[i].end);
            arr[i].diff = abs(arr[i].start - arr[i].end);
        }
        sort(arr, arr+n,comp);
        int cont=0;
        for(int i = 0; i<n;i++)
        {
            if(arr[i].diff > 0)
            {
                for(int j = i+1; j<n;j++)
                {
                    if(arr[i].start<arr[j].start && arr[i].end > arr[j].end)
                        cont++;
                    else if(arr[i].start > arr[j].start && arr[i].end < arr[j].end)
                        cont++; 
                }
            }
        }
        
        printf("Case #%d: %d\n",t,cont);
    }
    return 0;
}
