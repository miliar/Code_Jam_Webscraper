#include <cstdio>
#include <cstring>
double WP[110];
double OWP[110];
double OOWP[110],res[110];
char s[110][110];
int num[110];
int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    int T,n,ca=0;
    scanf("%d",&T);
    while(T--){
        scanf("%d",&n);
        memset(num,0,sizeof(num));
        for(int i=0;i<n;i++)
            scanf("%s",s[i]);
        for(int i=0;i<n;i++){
            int cnt=0;
            for(int j=0;j<n;j++){
                if(s[i][j]=='0') {
                    num[i]++;
                }
                else if(s[i][j]=='1'){
                    num[i]++;
                    cnt++;
                }
            }
            WP[i]=cnt*1.0/num[i];
        }
        for(int i=0;i<n;i++){
            double f=0;
            for(int j=0;j<n;j++){
                if(s[j][i]=='0'){
                    f+=WP[j]*num[j]/(num[j]-1);
                }
                else if(s[j][i]=='1'){
                    f+=(WP[j]*num[j]-1)/(num[j]-1);
                }
            }
            OWP[i]=f/num[i];
        }
        for(int i=0;i<n;i++){
            double f=0;
            for(int j=0;j<n;j++){
                if(s[i][j]!='.'){
                    f+=OWP[j];
                }
            }
            OOWP[i]=f/num[i];
        }
        for(int i=0;i<n;i++)
            res[i]=0.25*WP[i]+0.5*OWP[i]+0.25*OOWP[i];
        printf("Case #%d:\n",++ca);
        for(int i=0;i<n;i++)
            printf("%.12lf\n",res[i]);
    }
}
