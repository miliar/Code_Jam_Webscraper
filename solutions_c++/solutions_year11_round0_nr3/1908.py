#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;

int main()
{
    int T;
    scanf("%d",&T);
    for(int tc=1;tc<=T;tc++)
    {
        int N;
        scanf("%d",&N);
        long long A[N];
        for(int i=0;i<N;i++)
        {
            scanf("%lld",&A[i]);
        }
        sort(A,A+N);
        long long ans=0;
        long long t=0;
        for(int i=1;i<N;i++)
        {
            ans=ans^A[i];
            t=t+A[i];
        }
        printf("Case #%d: ",tc);
        if(ans==A[0])
        {
            printf("%lld", t);
        }
        else
        {
            printf("NO");
        }
        printf("\n");
    }

}
