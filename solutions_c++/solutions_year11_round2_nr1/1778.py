#include <cstring>
#include <cstdio>
using namespace std;
int set[101][128];
double wp[101];
double tmpWP[101];
double owp[101];
double oowp[101];
char line[128];
int N;
void calTmpWP(int r)
{
    for(int i=0;i<N;i++)
    {
        if(i==r) continue;
        int times=0;
        int win=0;
        for(int j=0;j<N;j++)
        {
            if(j==r) continue;
            if(set[i][j]==-1) continue;
            times++;
            if(set[i][j]==1)
            {
                win++;
            }
        }
        tmpWP[i]=(double)win/times;
    }

}
int main()
{
    int T,round=1;
//    double rpi=0;
    scanf("%d",&T);
    while(T--)
    {
        memset(set,-1,sizeof(set));
        memset(wp,0,sizeof(wp));
        memset(owp,0,sizeof(owp));
        memset(oowp,0,sizeof(oowp));
        scanf("%d",&N);
        for(int i=0;i<N;i++)
        {
            scanf("%s",line);
            int win=0,times=0;
            for(int j=0;j<N;j++)
            {
                if(line[j]=='.') continue;
                times++;
                if(line[j]=='1')
                {
                    set[i][j]=1;
                    win++;
                    continue;
                }
                if(line[j]=='0')
                {
                    set[i][j]=0;
                    continue;
                }
            }
            if(win==0) wp[i]=0.0;
            else if(times==0) wp[i]=0;
            else wp[i]=(double)win/times;
//            printf("wp[%d]=%.6lf\n",i,wp[i]);
        }
        //owp
        for(int i=0;i<N;i++)
        {
            memset(tmpWP,0,sizeof(tmpWP));
            calTmpWP(i);
            int count=0;
            double wpSum=0.0;
            for(int j=0;j<N;j++)
            {
                if(set[j][i]!=-1)
                {
                    count++;
                    wpSum+=tmpWP[j];
                }
            }
            owp[i]=wpSum/count;
//                printf("owp[%d]=%.6lf\n",i,owp[i]);
        }
        printf("Case #%d:\n",round++);
        //oowp
        for(int i=0;i<N;i++)
        {
                int count=0;
                double owpSum=0;
                for(int j=0;j<N;j++)
                {
                    if(set[i][j]!=-1)
                    {
                        count++;
                        owpSum+=owp[j];
                    }
                }
                oowp[i]=owpSum/count;
                double rpi=(wp[i]+2*owp[i]+oowp[i])/4.0;
                printf("%.6lf\n",rpi);
        }
    }
    return 0;
}
