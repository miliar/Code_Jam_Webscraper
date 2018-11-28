#include <cstdio>
#include <cstring>

int T,n;
char tmp;
char map[201][201];
double wp[201],owp[201],oowp[201];
int win[201],cnt[201];

int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&T);
    for (int Case=1;Case<=T;Case++){
        scanf("%d\n",&n);
        for (int i=1;i<=n;i++){
            for (int j=1;j<=n;j++) scanf("%c",&map[i][j]);
            scanf("%c",&tmp);
        }
        memset(win,0,sizeof(win));
        memset(cnt,0,sizeof(cnt));
        for (int i=1;i<=n;i++){
            for (int j=1;j<=n;j++) if (map[i][j]=='0'){cnt[i]++;}else if (map[i][j]=='1'){cnt[i]++;win[i]++;}
            wp[i]=win[i]*1.0/cnt[i];
        }
        for (int i=1;i<=n;i++){
            int cn=0;
            double tot=0;
            for (int j=1;j<=n;j++) if (map[i][j]=='0' || map[i][j]=='1'){
                if (map[j][i]=='1') tot+=(win[j]-1)*1.0/(cnt[j]-1);else
                if (map[j][i]=='0') tot+=win[j]*1.0/(cnt[j]-1);
                cn++;
            }
            owp[i]=tot/cn;
            //printf("owp[%d]=%lf\n",i,owp[i]);
        }
        for (int i=1;i<=n;i++){
            int cnt=0;
            double tot=0;
            for (int j=1;j<=n;j++) if (map[i][j]=='0' || map[i][j]=='1') {tot+=owp[j];cnt++;}
            oowp[i]=tot/cnt;
            //printf("oowp[%d]=%lf\n",i,oowp[i]);
        }
        printf("Case #%d:\n",Case);
        for (int i=1;i<=n;i++) printf("%lf\n",0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
    }
}
