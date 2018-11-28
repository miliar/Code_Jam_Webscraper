#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;
string a[105];
int n;
double wp[105],owp[105],oowp[105];
int main(){
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    cin>>T;
    for (int t=1;t<=T;t++){
        printf("Case #%d:\n",t);
        cin>>n;
        for (int i=0;i<n;i++){
            cin>>a[i];
            double sum=0,cnt=0;
            for (int j=0;j<n;j++){
                if (a[i][j]!='.'){
                    sum++;
                    if (a[i][j]=='1')
                        cnt++;
                }
            }
            wp[i]=cnt/sum;
        }

        for (int i=0;i<n;i++){
            owp[i]=0;
            double b=0;
            for (int j=0;j<n;j++) if (a[i][j]!='.'){
                b++;
                double sum=0,cnt=0;
                for (int k=0;k<n;k++) if (k!=i && a[j][k]!='.'){
                    sum++;
                    if (a[j][k]=='1')
                        cnt++;
                }
                owp[i]+=cnt/sum;
            }
            owp[i]/=b;
        }

        for (int i=0;i<n;i++){
            int cnt=0;
            oowp[i]=0;
            for (int j=0;j<n;j++)if (a[i][j]!='.'){
                cnt++;
                oowp[i]+=owp[j];
            }
            oowp[i]/=cnt;
        }
        for (int i=0;i<n;i++){
            double res= 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
            printf("%.12f\n",res);
        }
    }
    return 0;
}