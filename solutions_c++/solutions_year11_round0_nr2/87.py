#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int cas,n,cc,dd,top;
char inp[110],com[130][130],des[130][130],sta[110];
int main(){
    scanf("%d",&cas);
    for(int iii=0;iii<cas;iii++){
        memset(com,0,sizeof(com));
        memset(des,0,sizeof(des));
        scanf("%d",&cc);
        for(int i=0;i<cc;i++){
            scanf("%s",inp);
            com[inp[0]][inp[1]]=inp[2];
            com[inp[1]][inp[0]]=inp[2];
        }
        scanf("%d",&dd);
        for(int i=0;i<dd;i++){
            scanf("%s",inp);
            des[inp[0]][inp[1]]=1;
            des[inp[1]][inp[0]]=1;
        }        
        scanf("%d%s",&n,inp);
        top=0;
        for(int i=0;i<n;i++){
            sta[top++]=inp[i];
            while(top>1){
                if(!com[sta[top-1]][sta[top-2]])break;
                sta[top-2]=com[sta[top-1]][sta[top-2]];
                top--;
            }
            for(int i=0;i<top;i++){
                if(des[sta[i]][sta[top-1]]){
                    top=0;
                    break;
                }
            }
        }
        printf("Case #%d: [",iii+1);
        if(!top)printf("]\n");
        else{
            printf("%c",sta[0]);
            for(int i=1;i<top;i++)printf(", %c",sta[i]);
            printf("]\n");
        }
    }
    scanf(" ");
    return 0;
}
