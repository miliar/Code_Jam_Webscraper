/*
TASK: Problem C. Candy Splitting
LANG: C++
*/
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<algorithm>
using namespace std;
int N,M,T;
int num[1005];
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int i,j,k;
    scanf("%d",&T);
    for(int tt=1;tt<=T;tt++)
    {
        scanf("%d",&N);
        k=0;
        int sum=0;
        for(i=0;i<N;i++)
        {
            scanf("%d",&num[i]);
            k^=num[i];
            sum+=num[i];
        }
        sort(&num[0],&num[N]);
        if(k!=0)
            printf("Case #%d: NO\n",tt);
        else
            printf("Case #%d: %d\n",tt,sum-num[0]);
    }
}
