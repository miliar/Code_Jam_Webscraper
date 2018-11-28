#include <cstdio>
#include <cstring>

int main()
{
    int a[24*60*2],b[24*60*2];
    int ago[24*60*2],bgo[24*60*2];

    int turn,na,nb,resa,resb,re,cas,i,j,h1,h2,min1,min2;
    int a_start[128],a_end[128],b_start[128],b_end[128];
    
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);

    for(scanf("%d",&re),cas=1;re--;++cas){
        scanf("%d",&turn);
        scanf("%d%d",&na,&nb);
        
        for(i=0;i<na;++i){
            scanf("%d:%d",&h1,&min1);
            scanf("%d:%d",&h2,&min2);
            a_start[i]=60*h1+min1;
            a_end[i]=60*h2+min2;
        }

        for(i=0;i<nb;++i){
            scanf("%d:%d",&h1,&min1);
            scanf("%d:%d",&h2,&min2);
            b_start[i]=60*h1+min1;
            b_end[i]=60*h2+min2;
        }
        
        memset(a,0,sizeof a);
        memset(b,0,sizeof b);
        memset(ago,0,sizeof ago);
        memset(bgo,0,sizeof bgo);
        
        for(i=0;i<nb;++i){
            ++a[b_end[i]+turn];
            ++bgo[b_start[i]];
        }
        for(i=0;i<na;++i){
            ++b[a_end[i]+turn];
            ++ago[a_start[i]];
        }
        
        resa=resb=0;
        int acnt=0,bcnt=0;
        
        for(i=0;i<24*60;++i){
            acnt+=a[i];
            bcnt+=b[i];
            
            if(acnt>=ago[i])
                acnt-=ago[i];
            else{
                resa+=ago[i]-acnt;
                acnt=0;
            }
            
            if(bcnt>=bgo[i])
                bcnt-=bgo[i];
            else{
                resb+=bgo[i]-bcnt;
                bcnt=0;
            }
        }
        
        printf("Case #%d: %d %d\n",cas,resa,resb);
    }
}
