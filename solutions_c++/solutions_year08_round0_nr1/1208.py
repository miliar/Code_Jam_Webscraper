#include <cstdio>
#include <cstring>

char ans[128][128];
char ask[1024][128];

int main()
{
    char s[1024];
    int re,cas,i,j,ask_cnt,ans_cnt;
    
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    for(scanf("%d",&re),cas=1;re--;++cas){
        scanf("%d",&ans_cnt);
        gets(s);
        for(i=0;i<ans_cnt;++i)
            gets(ans[i]);
        scanf("%d",&ask_cnt);
        gets(s);
        for(i=0;i<ask_cnt;++i)
            gets(ask[i]);
            
        if(ask_cnt==0){
            printf("Case #%d: 0\n",cas);
            continue;
        }

        int best,pos=0,res=0;
        
        while(pos<ask_cnt){
            best=pos;
            for(i=0;i<ans_cnt;++i){
                for(j=pos;j<ask_cnt;++j)
                    if(strcmp(ans[i],ask[j])==0)
                        break;
                if(j>best)
                    best=j;
            }
            pos=best;
            ++res;
        }
        
        printf("Case #%d: %d\n",cas,res-1);
    }
}

        
        

