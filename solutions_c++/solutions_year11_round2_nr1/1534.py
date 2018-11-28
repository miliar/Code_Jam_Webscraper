#include<iostream>
#include<string>

using namespace std;

int tb[100][100];
double WP[100],OWP[100],OOWP[100];

int main(){
    freopen("A-large.in","r",stdin);
    freopen("x.out","w",stdout);
    int tc;
    cin>>tc;
    for(int t=1;t<=tc;t++){
        int n;
        cin>>n;
        string s;
        for(int i=0;i<n;i++){
            cin>>s;
            for(int j=0;j<n;j++)
                tb[i][j]=(s[j]=='1'?1:s[j]=='0'?0:-1);
        }
        int cnt,cnt2;
        for(int i=0;i<n;i++){
            double wp=0,owp=0;
            cnt2=0;
            for(int j=0;j<n;j++)
                if(i!=j&&tb[i][j]>=0){
                    cnt=wp=0;
                    for(int k=0;k<n;k++)
                        if(k!=i&&tb[j][k]>=0){
                            wp+=tb[j][k];
                            cnt++;
                        }
                    owp+=wp/cnt;
                    cnt2++;
                }
            owp/=cnt2;
            cnt=wp=0;
            for(int j=0;j<n;j++)
                if(tb[i][j]>=0){
                    wp+=tb[i][j];
                    cnt++;
                }
            wp/=cnt;
            WP[i]=wp;
            OWP[i]=owp;
        }
        printf("Case #%d:\n",t);
        for(int i=0;i<n;i++){
            cnt=0;
            OOWP[i]=0;
            for(int j=0;j<n;j++)
                if(tb[i][j]>=0){
                    OOWP[i]+=OWP[j];
                    cnt++;
                }    
            OOWP[i]/=cnt;
            printf("%.12lf\n",0.25*WP[i]+0.5*OWP[i]+0.25*OOWP[i]);
        }
    }    
    return 0;
}
