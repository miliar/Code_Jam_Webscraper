#include<stdio.h>
#include<string.h>
char C[300][300],D[300][300];
char str[1000],ans[1000];
int main(){
    freopen("B-large.in.txt","r",stdin);
    freopen("B-large.out.txt","w",stdout);
    int kase,kases=1;
    scanf("%d",&kase);
    while(kase--){
        int c,d,n;
        memset(C,0,sizeof(C));
        memset(D,0,sizeof(D));
        memset(ans,0,sizeof(ans));
        scanf("%d",&c);
        for(int i=0;i<c;i++){
            char t[10];
            scanf("%s",t);
            C[t[0]][t[1]]=t[2];
            C[t[1]][t[0]]=t[2];
        }
        scanf("%d",&d);
        for(int i=0;i<d;i++){
            char t[10];
            scanf("%s",t);
            D[t[0]][t[1]]=1;
            D[t[1]][t[0]]=1;
        }
        scanf("%d",&n);
        scanf("%s",str);
        int l=0;
        for(int i=0;i<n;i++){
            if(l){
                if(C[ans[l-1]][str[i]]!=0){
                    ans[l-1]=C[ans[l-1]][str[i]];
                    continue;
                }else{
                    for(int j=0;j<l;j++)
                        if(D[ans[j]][str[i]]){
                            l=0;
                            break;
                        }
                    if(l==0)continue;
                }
            }
           // printf("%d %c\n",i,str[i]);
            ans[l++]=str[i];
        }
        printf("Case #%d: [",kases++);
        for(int i=0;i<l;i++)printf("%s%c",i==0?"":", ",ans[i]);
        printf("]\n");
    }
    return 0;
}