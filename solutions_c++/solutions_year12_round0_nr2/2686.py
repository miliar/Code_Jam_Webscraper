#include<stdio.h>
#include<algorithm>
using namespace std;
int T,N,S,P;
int data[200],out;
int main()
{   freopen("B-small-attempt1.in","r",stdin);
    freopen("out.out","w",stdout);
    int q,w,e,r;
    scanf("%d",&T);
    for(q=0;q<T;++q){
        out=0;
        scanf("%d%d%d",&N,&S,&P);
        //printf("%d %d %d ",N,S,P);
        for(w=0;w<N;++w){
            scanf("%d",&data[w]);
        }
        sort(data,data+N);

        //for(w=0;w<N;++w) printf("%d ",data[w]); printf("\n");

        for(w=N-1;w>=0&&data[w]>(P-1)*3;--w){
            out++;
        }
        for(;data[w]>(P-2)*3+1&&data[w]>=P&&w>=0&&S>0;--w,S--) out++;
        printf("Case #%d: %d\n",q+1,out);
    }
    //return 0;
}
