#include <cstdio>
#include<algorithm>
#include<cstring>
#include<cmath>
using namespace std;
char cc[40][5],dd[30][5],s[120],ans[120];
int tt,c,d,n,cas;
int main() {
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    scanf("%d",&tt);
    for(cas=1;cas<=tt;++cas){
        scanf("%d",&c);
        for(int i=0;i<c;++i) scanf("%s",cc[i]);
        scanf("%d",&d);
        for(int i=0;i<d;++i) scanf("%s",dd[i]);
        scanf("%d%s",&n,s);
        int head=-1;
        ans[++head]=s[0];
        for(int i=1;s[i];++i){
            ans[++head]=s[i];
            for(int k=0;(head>0)&&k<c;++k)
                if((ans[head]==cc[k][0]&&ans[head-1]==cc[k][1])||(ans[head]==cc[k][1]&&ans[head-1]==cc[k][0])){
                    ans[--head]=cc[k][2];
                    break;
                }
            for(int j=head-1;(head>0)&&j>=0;--j){
                for(int k=0;k<d;++k)
                    if((ans[head]==dd[k][0]&&ans[j]==dd[k][1])||(ans[head]==dd[k][1]&&ans[j]==dd[k][0])){
                        head=-1;
                        break;
                    }
            }
        }
        printf("Case #%d: ",cas);
        printf("[");
        if(head>=0) printf("%c",ans[0]);
        for(int k=1;k<=head;++k)
            printf(", %c",ans[k]);
        printf("]\n");
    }
    return 0;
}