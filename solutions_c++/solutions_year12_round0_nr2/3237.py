#include<cstdio>

using namespace std;

int main()
{
    //freopen("bsmall.txt","r",stdin);
    freopen("B-large.in","r",stdin);
    //freopen("bsmall_out.txt","w",stdout);
    freopen("blarge_out.txt","w",stdout);

    int tests,t,n,s,p,i,j;
    int score,mand_surp,ans; //mandatory surprising for being greater than p
    float avg;
    
    scanf("%d",&tests);
    for(t=1;t<=tests;t++){
        ans=mand_surp=0;
        scanf("%d%d%d",&n,&s,&p);
        for(i=0;i<n;i++){
            scanf("%d",&score);
            
            if(score%3==0){
                if(score==0){
                    if(p==0){
                        ans++;   
                    }
                    continue; 
                }   
                avg=score/3.0;
                if(avg>=p) ans++;
                else if(avg+1>=p){
                    ans++;
                    mand_surp++;    
                }        
            }    
            
            else if(score%3==1){
                avg=score/3.0;
                if((int)(1+avg)>=p) ans++;        
            }    
            
            else if(score%3==2){
                avg=score/3.0;
                if((int)(1+avg)>=p) ans++;
                else if((int)(avg+2)>=p){
                    ans++;
                    mand_surp++;    
                }        
            }                
        }    
        if(mand_surp>s)
            ans-=mand_surp-s;
        printf("Case #%d: %d\n",t,ans);
    }
    
    //getchar();getchar();
    return 0;
}
