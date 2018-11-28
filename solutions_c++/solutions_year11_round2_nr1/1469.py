#include<stdio.h>
int main(){

    int t,n,nplay[101]={0},nwin[101]={0};
    double wp[101]={0},owp[101]={0},oowp[101]={0};
    char tmp[102],tb[102][102]={0};
    scanf("%d",&t);
    for(int casenum=1;casenum<=t;++casenum)
    {
        scanf("%d",&n);

        for(int i=0;i<n;i++){
            nplay[i]=0;
            nwin[i]=0;
            wp[i]=0;
            owp[i]=0;
            oowp[i]=0;
            for(int j=0;j<n;j++)
                tb[i][j]=0;
        }
        for(int i=0;i<n;++i){
            scanf("%s",tmp);
            for(int j=0;j<n;j++)
                switch(tmp[j]){
                case '1': nwin[i]++;
                case '0': nplay[i]++;
                case '.': tb[i][j]=tmp[j];
                }
            wp[i]=1.0*nwin[i]/nplay[i];
        }


        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(tb[i][j]=='0')
                    owp[i]+=1.0*(nwin[j]-1)/(nplay[j]-1);
                else
                    if(tb[i][j]=='1')
                        owp[i]+=1.0*nwin[j]/(nplay[j]-1);
            }
            owp[i]/=nplay[i];
        }


        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++)
                if(tb[i][j]!='.')
                    oowp[i]+=owp[j];
            oowp[i]/=nplay[i];
        }


        printf("Case #%d:\n",casenum);
        for(int i=0;i<n;i++)
            printf("%.12lf\n",0.25*(wp[i]+oowp[i])+0.5*owp[i]);
//printf("%lf\n",owp[i]);
    }

    return 0;
}
