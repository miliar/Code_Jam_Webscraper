#include<iostream>
#include<stdio.h>
#include<map>
#include<stdlib.h>
#include<algorithm>
#include<vector>
#include<string>
#include<math.h>
using namespace std;

int main()
{
   // freopen("A-large.in","r",stdin);
    //freopen("out.txt","w",stdout);
    int t,i,k,n,ct,cta[110],ctb[110],j;
    double sum,wp[110],owp[110],oowp[110];
    char s[110][110];
    scanf("%d",&t);
    for(k=1;k<=t;k++) {
        scanf("%d",&n);
        for(i=0;i<n;i++) scanf("%s",s[i]);
        for(i=0;i<n;i++) {
            cta[i]=ctb[i]=0;
            for(j=0;j<n;j++) {
                if(s[i][j]=='1') cta[i]++;
                if(s[i][j]!='.') ctb[i]++;
            }
            wp[i]=(double)cta[i]/ctb[i];
        }
        //for(i=0;i<n;i++) cout<<wp[i]<<endl;
        for(i=0;i<n;i++) {
            ct=0;
            sum=0.0;
            for(j=0;j<n;j++) {
                if(s[i][j]!='.') {
                    ct++;
                    if(s[i][j]=='1') sum+=(double)cta[j]/(ctb[j]-1);
                    else sum+=(double)(cta[j]-1)/(ctb[j]-1);
                }
            }
            owp[i]=sum/ct;
        }
        //for(i=0;i<n;i++) cout<<owp[i]<<endl;
        for(i=0;i<n;i++) {
            ct=0;
            sum=0.0;
            for(j=0;j<n;j++) {
                if(s[i][j]!='.') {
                    ct++;
                    sum+=owp[j];
                }
            }
            oowp[i]=sum/ct;
        }
        //for(i=0;i<n;i++) cout<<oowp[i]<<endl;
        printf("Case #%d:\n",k);
        for(i=0;i<n;i++) cout<<0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]<<endl;
    }
    return 0;
}
