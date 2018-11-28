#include <stdio.h>
#include <iostream>
using namespace std;

int t,c,d,n;
char com[40][5];
char opp[30][3];
char str[110];
int h,i,j,k,p;
char res[110];

void solve(){
    p=0;
    for(i=0;str[i];++i){
        res[p]=str[i];
        if(p){
            for(j=0;j<c;++j) if(com[j][0]==res[p]&&com[j][1]==res[p-1]||
                                com[j][1]==res[p]&&com[j][0]==res[p-1]){
                --p;
                res[p]=com[j][2];
                if(p)
                    j=0;
                else
                    break;
            }
        }
        if(p){
            for(j=0;j<d;++j)
                for(k=0;k<p;++k) if(opp[j][0]==res[p]&&opp[j][1]==res[k]||
                                    opp[j][1]==res[p]&&opp[j][0]==res[k]){
                    p=-1;
                    goto lp;
                }
        }
        lp:++p;
    }
}

int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.txt","w",stdout);
    scanf("%d",&t);
    for(h=1;h<=t;++h){
        scanf("%d",&c);
        for(i=0;i<c;++i)
            scanf("%s",com[i]);
        scanf("%d",&d);
        for(i=0;i<d;++i)
            scanf("%s",opp[i]);
        scanf("%d",&n);
        scanf("%s",str);
        solve();
        printf("Case #%d: [",h);
        for(i=0;i<p-1;++i)
            printf("%c, ",res[i]);
        if(p) printf("%c",res[p-1]);
        printf("]\n");
    }
}
