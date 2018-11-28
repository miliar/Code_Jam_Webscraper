#include<cstdio>
#include<cstdlib>
#include<cstring>
long long addmod(long long x, long long n){
    if(x==n-1)
        return 0;
    return x+1;
}

int main(){
    long long r,k,n,t;
    long long g[1010];
    
    scanf("%lld",&t);
    for(long long c=1;c<=t;c++){
        scanf("%lld %lld %lld",&r,&k,&n);
        //printf("c:%d r:%d k:%d n:%d\n",c,r,k,n);
        for(long long i=0;i<n;i++){
            scanf("%lld",&g[i]);
            //printf("g[%d]=%d\n",i,g[i]);
        }
        long long p=0;
        long long lbl[1010];
        memset(lbl,0,1010*sizeof(long long));
        long long tot=0;
        long long t=0;
        long long gs[1010];
        
        while(1){
            t++;
            if(lbl[p]){
                break;
            }
            gs[t]=tot;
            lbl[p]=t;
            long long i,soma=0;
 //         printf("p:%d\n",p);
            for( i =p;;i=addmod(i,n)){
   //           printf("i:%d g[i]:%d soma:%d\n",i,g[i],soma);
                if(soma+g[i]>k){
               
                    break;
                }
                
                soma+=g[i];
                if(addmod(i,n)==p){
                    i=p;break;
                }
                
            }
            tot+=soma;
     //      printf("tot:%d\n",tot);
            p=i;
            if(t==r){
                t++;
                break;
            }
        }
        
        t--;
        if(t==r){
            printf("Case #%lld: %lld\n",c,tot);
            continue;
        }
       // printf("ciclo de tamanho %d com soma %d\n",t,tot);
       // printf("antes deu tot=%d t=%d\n",tot,t);
       // printf("lbl[p]:%d  gd[lbl[p]]:%d\n",lbl[p],gs[lbl[p]]); 
        tot = tot + (tot-gs[lbl[p]])*( (r-t)/(t-lbl[p]+1));
        t= t + (t-lbl[p]+1)*( (r-t)/(t-lbl[p]+1));
      // printf("depois deu tot=%d t=%d\n",tot,t);
        while(t<r){
            t++;
            long long i,soma=0;
            for( i =p;;i=addmod(i,n)){
                if(soma+g[i]>k)
                    break;
                soma+=g[i];
                if(addmod(i,n)==p){
                    i=p;break;
                }
                
            }
            tot+=soma;
            p=i;
        }
        printf("Case #%lld: %lld\n",c,tot);
    }
    return 0;

}
