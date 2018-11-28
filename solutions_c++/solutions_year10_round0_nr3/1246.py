#include<stdio.h>

int DP[1005];
int to[1005];
int in[2005];

int R,K,N;

long long ans[1005];
int seen[1005];
long long sss;
int main(){
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int C;
    scanf("%d",&C);
    for(int c=1;c<=C;c++){
        scanf("%d %d %d",&R,&K,&N);
        for(int i=0;i<N;i++) scanf("%d",&in[i]);
        for(int i=0;i<N;i++) in[i+N]=in[i];
        
        for(int i=0;i<N;i++){
            int sum=0;
            for(int j=0;j<N;j++){
                sum+=in[i+j];
                if(sum>K) break;
                else {
                    DP[i]=sum;
                    to[i]=(j+i+1)%N;    
                }    
            }    
        }
        
        int r,at=0,round,a;
        long long ccc;
        sss=0;
        for(int i=0;i<1005;i++) seen[i]=-1;
        for(r=0;r<R;r++){
            if(seen[at]==-1){
                seen[at]=r;
                sss+=DP[at];
                ans[r]=sss;
                at=to[at];    
            } else { 
                a=seen[at]; 
                break; 
            }
        }
        R-=r;
        
        if(R){
        
        if(a-1<0){
            round=r;
            sss+=(ans[r-1])*(R/round);
            if(R%round) sss+=(ans[R%round-1]);
        } else {
            ccc=ans[a-1];
            round=r-a;
            sss+=(ans[r-1]-ccc)*(R/round);
            sss+=ans[R%round+a-1]-ccc;
        }
        
        }
        printf("Case #%d: %I64d\n",c,sss);
    }
return 0;
}
