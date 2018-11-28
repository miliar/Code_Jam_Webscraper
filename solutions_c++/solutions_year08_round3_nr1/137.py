#include <iostream>
#include <cmath>
#include <functional>
using namespace std;

#define int long long

int arr[1024];

main()
{
    int T,kcase(0);
    scanf("%I64d",&T);
    while(T--){
        int P,K,L;
        scanf("%I64d%I64d%I64d",&P,&K,&L);
        for(int i=0;i<L;i++){
            scanf("%I64d",&arr[i]);
        }
        if(P*K>=L){
            sort(arr,arr+L,greater<int>());
            int j=0,res=0,pp=1;
            while(j<L){
                int sum=0;
                for(int i=0;i<K && j<L;i++,j++){
                    sum+=arr[j];
                }
                res+=sum*pp;
                pp++;
            }
            printf("Case #%I64d: %I64d\n",++kcase,res);
        }
        else {
            printf("Case #%I64d: Impossible\n",++kcase);
        }
    }
}

