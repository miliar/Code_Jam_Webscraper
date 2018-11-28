#include <stdio.h>
bool com[30][30];
bool opp[30][30];
int main(){
    int t,cs;
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&t);
    for(cs=1;cs<=t;++cs){
        int i,j,c,d,n;
        for(i=0;i<26;++i) for(j=0;j<26;++j) com[i][j]=opp[i][j]=false;
        char conv[30][30];
        char str[10];
        scanf("%d",&c);
        for(i=1;i<=c&&c;++i){
            scanf(" %s",str);
            com[str[0]-65][str[1]-65]=com[str[1]-65][str[0]-65]=true;
            conv[str[0]-65][str[1]-65]=conv[str[1]-65][str[0]-65]=str[2];
        }
        scanf("%d",&d);
        for(i=1;i<=d&&d;++i){
            scanf(" %s",str);
            opp[str[0]-65][str[1]-65]=opp[str[1]-65][str[0]-65]=true;
        }
        scanf("%d",&n);
        char res[150],ch;
        int ind=0;
        for(i=1;i<=n;++i){
            scanf(" %c",&ch);
            if(ind==0) res[ind++]=ch;
            else{
                if(com[ch-65][res[ind-1]-65]) res[ind-1]=conv[ch-65][res[ind-1]-65];
                else{
                    for(j=0;j<ind;++j) if(opp[ch-65][res[j]-65]) break;
                    if(j==ind) res[ind++]=ch;
                    else ind=0;
                }
            }
        }
        printf("Case #%d: [",cs);
        if(ind) printf("%c",res[0]);
        for(j=1;j<ind;++j) printf(", %c",res[j]);
        printf("]\n");
    }
    return 0;
}
