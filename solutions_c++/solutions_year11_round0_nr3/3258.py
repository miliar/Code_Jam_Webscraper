#include <cstdio>
using namespace std;
int T,N,sum,min,a;
int S;
int main(){
    scanf("%d",&T);
    for(int t=0;t<T;t++){
        S=0;
        sum=0;min=0xFFFFFF;
        scanf("%d",&N);
        for(int i=0;i<N;i++){
            scanf("%d",&a);
            sum+=a;
            if (a<min) min=a;
            S^=a;
            }
        printf("Case #%d: ",t+1);
        if (S!=0)
          printf("NO\n");
        else{
          printf("%d\n",sum-min);
        }
    }

}
