#include<iostream>
#include<math.h>
#include<cstring>
#include<cstdio>
using namespace std;
double wp[1001],owp[1001],oowp[1001];
int a[1001][1001];
int t,n;

int main(){
    //freopen("A.out","w",stdout);
    scanf("%d",&t);
    for (int z=1;z<=t;z++){
        scanf("%d",&n);
        getchar();
        for (int i=1;i<=n;i++){
            for (int j=1;j<=n;j++){
                 char x=getchar();
                 if (x=='1') a[i][j]=1;
                 if (x=='0') a[i][j]=0;
                 if (x=='.') a[i][j]=-1;
            }
            getchar();
        }
        
        memset(wp,0,sizeof wp);
        memset(owp,0,sizeof owp);
        memset(oowp,0,sizeof oowp);
        
        for (int p=1;p<=n;p++){
            //WP
            int cnt=0,cnt1=0;
            for (int i=1;i<=n;i++){
                if (a[p][i]!=-1){cnt++;cnt1+=a[p][i];}
            }
            wp[p]=double(cnt1)/cnt;
            
            //OWP
            cnt=0;cnt1=0;int cnt2=0;
            double cnt3=0;
            for (int i=1;i<=n;i++){
                if (i!=p && a[p][i]!=-1){
                   cnt++;
                   cnt1=cnt2=0;
                   for (int j=1;j<=n;j++){
                        if (j!=p && a[i][j]!=-1){cnt1++;cnt2+=a[i][j];}
                   }
                   
                   cnt3+=double(cnt2)/cnt1;
                }
            }
            owp[p]=cnt3/cnt;
        }
        
        for (int i=1;i<=n;i++){
            int cnt=0;
            double cnt1=0;
            for (int j=1;j<=n;j++){
                if (a[i][j]!=-1){
                   cnt1+=owp[j];cnt++;
                }
            }
            oowp[i]=cnt1/cnt;
        }
        printf("Case #%d:\n",z);
        for (int i=1;i<=n;i++){
            double ans1=wp[i]*0.25+owp[i]*0.5+oowp[i]*0.25;
            printf("%7lf\n",ans1);
        }
   }
   //while (1);
}
            
