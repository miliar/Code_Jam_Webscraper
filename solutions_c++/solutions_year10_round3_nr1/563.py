#include<iostream>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
#include<string>
#include<map>
#include<stack>
#include<queue>
#define max(a,b)(a>b?a:b)
#define min(a,b)(a<b?a:b)
#define inf 100


using namespace std;

int A[1001],B[1001];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    int test,_case=1,i,j,c,N;

    scanf("%d",&test);

    while(test--)
    {
        scanf("%d",&N);
        for(i=0;i<N;i++)
            scanf("%d %d",&A[i],&B[i]);

        c=0;

        for(i=0;i<N;i++)
            for(j=i+1;j<N;j++)
            {
                if((A[i]>A[j]&&B[i]<B[j])||(A[i]<A[j]&&B[i]>B[j]))
                    c++;
            }
        printf("Case #%d: %d\n",_case++,c);
    }



    return 0;
}
