#include <iostream.h>
int main(){
    int T,R,N,K,i,j,sum,tong,ketqua,run;
    int r,result;
    int g[1000];
    FILE *f, *fout;
    f = fopen("input.txt","r");
    fout = fopen("output2.txt","w");
    fscanf(f,"%d", &T);
    for(i=0;i<T;i++){
                ketqua=0;
                tong =0;
                fscanf(f,"%d %d %d", &R, &K, &N);
                for(j=0;j<N;j++){
                                 fscanf(f,"%d", &g[j]);
                                 tong += g[j];
                                 }
                run =0;
                for(j=0;j<R;j++){
                                 sum=0;
                                 while(sum<=K && sum<=tong){
                                               sum += g[run];
                                               //cout<<sum<<"-"<<run<<" ";
                                               run = (run+1)%N;
                                 }
                                 //cout<<endl;
                                 if(run>0) run--;
                                 else run = N-1;
                                 ketqua+=sum-g[run];
                                 
                }
                fprintf(fout,"Case #%d: %d\n", i+1, ketqua);
    }
    //cin>>i;
    fclose(f);
    fclose(fout);
    return 0;
}
