#include <stdio.h>
#include <string.h>
int main(){
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    
    int T,t,C,i,j,k,D,N,Head,Tail;
    char c,s[4];
    int com[27][27],opp[27][27],Queue[105];
    
    scanf("%d",&T);
    for (t=1;t<=T;t++){
        memset(com,0,sizeof(com));
        memset(opp,0,sizeof(opp));
        scanf("%d",&C);
        while (C--){
              scanf("%s",s);
              i=s[0]-'A'+1;
              j=s[1]-'A'+1;
              k=s[2]-'A'+1;
              com[i][j]=k;
              com[j][i]=k;
        }
        scanf("%d",&D);
        while (D--){
              scanf("%s",s);
              i=s[0]-'A'+1;
              j=s[1]-'A'+1;
              opp[i][j]=1;
              opp[j][i]=1;
        }
        Head=Tail=1;
        scanf("%d%c",&N,&c);
        for (i=1;i<=N;i++){
            scanf("%c",&c);
            j=c-'A'+1;
            if (Head==Tail){
               Queue[Tail]=j;
               Tail++;
               continue;
            }
            if (com[Queue[Tail-1]][j]!=0){
               Queue[Tail-1]=com[Queue[Tail-1]][j];
               continue;
            }
            for (k=Head;k<Tail;k++)
                if (opp[Queue[k]][j]==1)
                   break;
            if (k<Tail)
               Head=Tail=1;
            else{
               Queue[Tail]=j;
               Tail++;
            }
        }
        printf("Case #%d: [",t);
        for (i=Head;i<Tail;i++)
            if (i!=Head) printf(", %c",Queue[i]-1+'A');
            else printf("%c",Queue[i]-1+'A');
        printf("]\n");
    }
    
    fclose(stdin);
    fclose(stdout);
    return 0;
}
