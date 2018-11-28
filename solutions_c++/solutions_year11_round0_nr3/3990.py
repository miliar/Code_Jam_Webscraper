#include<stdio.h>
int T,N;
int data[100];
int sum;
int Xor;
int min;
int def[25];
int main()
{   int q,w,e,r;
    freopen("C-small-attempt0.in","r",stdin);
    freopen("out.out","w",stdout);
    scanf("%d",&T);
    for(q=1,def[0]=1;q<25;++q) def[q]=def[q-1]<<1;
    for(q=0;q<T;++q)
    {   scanf("%d",&N);
        for(w=0,sum=0;w<N;++w){
            scanf("%d",&data[w]);
            sum+=data[w];
            if(data[w]<min||w==0) min=data[w];
            if(w==0) Xor=data[w];
            else{
                for(e=0;def[e]<=data[w]||def[e]<=Xor;++e){
                    if(((def[e]&Xor)&&(!(def[e]&data[w])))||((!(def[e]&Xor))&&(def[e]&data[w]))){
                        Xor=Xor|def[e];
                    }
                    else if(Xor&def[e]) Xor-=def[e];
                }
                //printf("%d\n",Xor);
            }
        }
        if(Xor) printf("Case #%d: NO\n",q+1);
        else printf("Case #%d: %d\n",q+1,sum-min);
    }
    return 0;
}
