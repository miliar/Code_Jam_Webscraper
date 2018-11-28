#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <memory.h>
using namespace std;
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    long i,j,n;
    long test,order,os,ow;
    long sum[105],win[105];
    char rank[105][105];
    double total[105],owp[105],mop[105];
    scanf("%ld",&test);
    for(order=1;order<=test;order++){
        memset(mop,0,sizeof(mop));
        memset(total,0,sizeof(total));
        memset(owp,0,sizeof(owp));
        memset(sum,0,sizeof(sum));
        memset(win,0,sizeof(win));
        scanf("%ld",&n);
        for(i=1;i<=n;i++)
            scanf("%s",&rank[i][1]);
        for(i=1;i<=n;i++){
            for(j=1;j<=n;j++)
                if(rank[i][j]!='.'){
                    sum[i]++;
                    win[i]+=rank[i][j]-'0';
                }
            total[i]=win[i]*1.0/sum[i];
        }
        for(i=1;i<=n;i++){
            for(j=1;j<=n;j++){
                if(rank[i][j]!='.'){
                    ow=win[j];
                    os=sum[j]-1;
                    if(rank[i][j]=='0')
                        ow--;
                    owp[i]+=ow*1.0/os;//initialize
                }
            }
            owp[i]/=sum[i];
        }
        for(i=1;i<=n;i++){
            for(j=1;j<=n;j++)
                if(rank[i][j]!='.'){
                mop[i]+=owp[j];
            }
            mop[i]/=sum[i];
        }
        printf("Case #%ld:\n",order);
        for(i=1;i<=n;i++){
            printf("%.12lf\n",0.25*total[i]+0.5*owp[i]+0.25*mop[i]);
        }
    }
    return 0;
}
