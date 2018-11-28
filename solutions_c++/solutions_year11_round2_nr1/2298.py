#include <iostream>
#include <cstdio>
using namespace std;
struct data
{
    int a,b;
} data[10001];
int NUM;
int main()
{
    freopen("C:\\Users\\¼Ó·ÆÃ¨\\Downloads\\A-large.in", "r", stdin);
    freopen("D:OUTPUT.txt", "w", stdout);
    int n;
    char map[101][101];
    int win[101];
    int sum[101];
    int ok[101];
    double WP[101],OWP[101],OOWP[101];
    double RPI;
    int i,j;
    int pp,test;
    scanf("%d",&test);
    for (pp=1; pp<=test; pp++)
    {
        scanf("%d",&n);
        NUM=0;
        for(i=0; i<n; i++)
        {
            scanf("%s",map[i]);
            sum[i]=0;
            win[i]=0;
            ok[i]=-1;
        }
        for(i=0; i<n; i++)
        {
            for(j=i+1; j<n; j++)
            {
                if(map[i][j]=='.') continue;
                data[NUM].a=j;data[NUM].b=ok[i];ok[i]=NUM++;
                data[NUM].a=i;data[NUM].b=ok[j];ok[j]=NUM++;
                sum[i]++;sum[j]++;
                if(map[i][j]=='1') win[i]++;
                else win[j]++;
            }
            WP[i]=1.0*win[i]/sum[i];
        }
        for(i=0; i<n; i++)
        {
            OWP[i]=0;
            int num=0;
            for(j=ok[i]; j!=-1; j=data[j].b)
            {
                num++;

                if(map[i][data[j].a]=='0')
                    OWP[i]=OWP[i]+1.0*(win[data[j].a]-1)/(sum[data[j].a]-1);
                else
                    OWP[i]=OWP[i]+1.0*(win[data[j].a])/(sum[data[j].a]-1);
            }
            OWP[i]/=num;
        }
        for(i=0; i<n; i++)
        {
            OOWP[i]=0;

            int num=0;
            for(j=ok[i]; j!=-1; j=data[j].b)
            {
                num++;

                OOWP[i]+=OWP[data[j].a];
            }
            OOWP[i]/=num;
        }
        printf("Case #%d:\n",pp);
        for(i=0; i<n; i++)
        {
            RPI=0.25*WP[i]+0.5*OWP[i]+0.25*OOWP[i];
            printf("%.12f\n",RPI);
        }

    }
}
