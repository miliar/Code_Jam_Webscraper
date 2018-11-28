#include <cstdio>
#include <algorithm>
using namespace std;
char ch[105][105];
int g[105][105];
int cnt[105];
double wp[105];
double owp[105];
double oowp[105];
double rpi[105];
int n;
void calwp(){
    for(int i=0;i<n;i++){
        double a=0,b=0;
        cnt[i]=0;
        for(int j=0;j<n;j++){
            if(g[i][j]==1) a+=1,b+=1,cnt[i]++;
            if(g[i][j]==-1) b+=1,cnt[i]++;
        }
        wp[i]=a/b;
    }
}
void calowp(){
    for(int i=0;i<n;i++){
        double tot=0;
        for(int j=0;j<n;j++){
            if(g[i][j]==0) continue;
            double tmp=wp[j]*cnt[j];
            if(g[i][j]==-1) tmp-=1;
            tmp/=(cnt[j]-1);
            tot+=tmp;
        }
        owp[i]=tot/(cnt[i]);
    }
}
void caloowp(){
    for(int i=0;i<n;i++){
        double tot=0;
        for(int j=0;j<n;j++){
            if(g[i][j]==0) continue;
            double tmp=owp[j];
            tot+=tmp;
        }
        oowp[i]=tot/(cnt[i]);
    }
}
int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int ca=0;
    int m;
    scanf("%d",&m);
    while(m--){
    scanf("%d",&n);
    for(int i=0;i<n;i++)
    {
        scanf("\n%s",ch[i]);
        for(int j=0;j<n;j++){
            if(ch[i][j]=='1') g[i][j]=1;
            if(ch[i][j]=='0') g[i][j]=-1;
            if(ch[i][j]=='.') g[i][j]=0;
        }
        //for(int j=0;j<n;j++) printf("%d ",g[i][j]);
        //puts("");
    }

    calwp();
    calowp();
    caloowp();
    printf("Case #%d:\n",++ca);
    for(int i=0;i<n;i++){
        printf("%.10lf\n",wp[i]/4+owp[i]/2+oowp[i]/4);
    }
    }
    return 0;
}
