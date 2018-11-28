#include <cstdio>
#include <cstring>

char s[3];
int n,m,len,T;
char comb[200][200];
int oppo[200][200];
char el[1000],ans[1000];

int main()
{
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    scanf("%d",&T);
    for (int Case=1;Case<=T;Case++){
        memset(comb,0,sizeof(comb));
        memset(oppo,0,sizeof(oppo));
        scanf("%d",&n);for (int i=1;i<=n;i++){scanf("%s",s);comb[s[0]][s[1]]=s[2];comb[s[1]][s[0]]=s[2];}
        scanf("%d",&m);for (int i=1;i<=m;i++){scanf("%s",s);oppo[s[0]][s[1]]=1;oppo[s[1]][s[0]]=1;}
        scanf("%d",&len);scanf("%s",el);
        ans[0]=el[0];
        int now=0;
        for (int i=1;i<len;i++){
            if (now==-1) ans[++now]=el[i];else
            if (comb[el[i]][ans[now]]) 
               ans[now]=comb[el[i]][ans[now]];
            else{
               for (int j=0;j<=now;j++) if (oppo[el[i]][ans[j]]) {now=-1;break;}
               if (now!=-1) ans[++now]=el[i]; 
            }
        }
        printf("Case #%d: [",Case);
        if (now!=-1) printf("%c",ans[0]);
        for (int i=1;i<=now;i++) printf(", %c",ans[i]);printf("]\n");
    }
}
