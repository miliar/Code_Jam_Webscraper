#include<cstdio>
#include<cstring>

int t,c,d,n;
char combine[100][10], opp[100][10];
int have[200];
int pos;
char ans[1000];

int main(){
    scanf("%d",&t);
    for (int ca=1;ca<=t;++ca){
        memset(opp,0,sizeof(opp));
        memset(have,0,sizeof(have));
        pos=0;
        
        scanf("%d",&c);
        for (int i=0;i<c;++i) scanf("%s",combine[i]);
        scanf("%d",&d);
        for (int i=0;i<d;++i) scanf("%s",opp[i]);
        
        char tmp[1000];
        scanf("%d%s",&n,tmp);
        for (int i=0;i<n;++i){
            ++have[tmp[i]];
            ans[pos++] = tmp[i];
            if (pos!=1){
                for (int j=0;j<c;++j){
                    if (((combine[j][0]==ans[pos-1]) && (combine[j][1]==ans[pos-2]))
                        ||((combine[j][1]==ans[pos-1]) && (combine[j][0]==ans[pos-2]))){
                        --have[ans[pos-1]]; --have[ans[pos-2]];
                        pos-=2;
                        ans[pos++]=combine[j][2];
                    }
                }
                for (int j=0;j<d;++j){
                    if ((have[opp[j][0]] && have[opp[j][1]]) || (have[opp[j][1]] && have[opp[j][0]])){
                        memset(have,0,sizeof(have));
                        pos=0;
                    }
                }
            }
        }
        printf("Case #%d: [",ca);
        for (int i=0;i<pos;++i){
            if (i==0) printf("%c",ans[i]);
            else printf(", %c",ans[i]);
        }
        printf("]\n");
    }
    return 0;
}
