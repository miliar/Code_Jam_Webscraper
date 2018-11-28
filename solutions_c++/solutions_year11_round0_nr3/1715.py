#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#define MAXN 1234
using namespace std;
int can[MAXN];
int main(){
   // freopen("C-small-attempt0.in","r",stdin);
    freopen("C-large.in","r",stdin);

  //  freopen("C_out.txt","w",stdout);
    freopen("Clarge_out.txt","w",stdout);
    int T,N;
    scanf("%d",&T);
    for(int _case=1;_case<=T;_case++){
        scanf("%d",&N);
        __int64 t=0;
        for(int i=0;i<N;i++){
            scanf("%d",&can[i]);
            t ^= can[i];
        }
        if(t!=0)printf("Case #%d: NO\n",_case);
        else{
            sort(can,can+N);
            __int64 sum=0;
            for(int i=1;i<N;i++)sum+=can[i];
            printf("Case #%d: %I64d\n",_case,sum);
        }
    }

    return 0;
}

