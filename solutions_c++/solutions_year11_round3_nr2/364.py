#include <stdio.h>
#include <stdlib.h>
long long int N,L,t,C;
struct e_element{
    long long int pos;
    long long int incr;
};
e_element elem[1000005];
long long int  inc[1000005];
int compa(const void *a,const void *b){
    e_element *aa = (e_element *)a;
    e_element *bb = (e_element *)b;
    if( aa->incr > bb->incr)
        return -1;
    if( aa->incr == bb->incr)
        return 0;
    return 1;
}
void resuelve(){
    scanf("%lld",&L);
    scanf("%lld",&t);
    scanf("%lld",&N);
    scanf("%lld",&C);
    for(int i=0;i<C;i++){
        scanf("%lld",&inc[i]);
    }
    long long int ini=-1;
    long long int total=0;;
    elem[0].pos = 0;
    for(int i=0;i<N;i++){
          elem[i].incr = inc[i%C];
          elem[i+1].pos = elem[i].pos+elem[i].incr;
          total+=elem[i].incr*2;
          if( ini == -1 && total >=t){
            ini  = i;
            elem[i].incr = ((total-t))/2;
          }
    }
    if( ini != -1){
        qsort( &elem[ini], N-ini, sizeof(elem[0]), compa);
        for(int i=ini,util=0; i <N && util < L; i++,util++){
            total-= elem[i].incr;
        }
    }
    printf("%lld",total);
}
int main(){
    int T;
    scanf("%d",&T);
    for(int i=1;i<=T;i++){
        printf("Case #%d: ",i);
        resuelve();
        printf("\n");
    }
    return 0;
}
