#include<stdio.h>
int main(void){
    FILE *inp,*oup;
    inp = fopen("C-small-attempt7.in.","r");
    oup = fopen("C-small.oup","w");
    int T,N,R,k,g[10];
    int sum = 0,y = 0,c=0;
    fscanf(inp,"%d",&T);
    for(int i=0;i<T;i++){
        fscanf(inp,"%d%d%d",&R,&k,&N);
        for(int j = 0; j < N; j++)
          fscanf(inp,"%d",&g[j]);
        c = 0;
        for(int p=0;p<R;p++){
        for(int h=0;h<N;h++)
          {
                  sum += g[(c%N)];
                  c++;
                  if(sum>k){
                  sum-=g[(c-1)%N];
                  c--;
                  break;
                  }

          }

            y += sum;
            sum=0;
        }
        fprintf(oup,"Case #%d: %d\n",i+1,y);
        y=0;
    }

}
