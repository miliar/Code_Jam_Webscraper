#include<iostream>

using namespace std;

void deal(void)
{
    int n;
    char a[200][200];
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        scanf("%s",a[i]);
    }
    double wp[200],owp[200],oowp[200];
    int num[200]={0},win[200]={0};
    for(int i=0;i<n;i++){
        int w=0,t=0;
        for(int j=0;j<n;j++){
            if(a[i][j]!='.'){
                t++;
                if(a[i][j]=='1')
                    w++;
            }
        }
        wp[i]=(double)w/t;
        num[i]=t;
        win[i]=w;
    }
    for(int i=0;i<n;i++){
        owp[i]=0.0;
        for(int j=0;j<n;j++){
            if(a[i][j]=='.')
                continue;
            if(a[j][i]=='1'){
                owp[i]+=(double)(win[j]-1)/(num[j]-1);
            }
            else{
                owp[i]+=(double)win[j]/(num[j]-1);
            }
        }
        owp[i]/=num[i];
    }
    for(int i=0;i<n;i++){
        oowp[i]=0.0;
        for(int j=0;j<n;j++){
            if(a[i][j]=='.')
                continue;
            oowp[i]+=owp[j];
        }
        oowp[i]/=num[i];
    }
    for(int i=0;i<n;i++){
        printf("%lf\n",wp[i]/4+owp[i]/2+oowp[i]/4);
    }

}

int main(void)
{
    int num=0;
    scanf("%d",&num);
    for(int i=1;i<=num;i++){
        printf("Case #%d:\n",i);
        deal();
    }
    return 0;
}
/* vim: set expandtab ts=4 sw=4 sts=4 tw=100: */
