#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define MAXN 110
int CAS;
int n;
int map[MAXN][MAXN];
char s[MAXN];
double wp[MAXN],owp[MAXN],oowp[MAXN],rpi[MAXN];
double win[MAXN],lose[MAXN];
int main()
{
    freopen("a.in","r",stdin);
    freopen("out.txt","w",stdout);
    double temp;
    double wintemp,losetemp;
    scanf("%d",&CAS);
    for(int cas = 1;cas <= CAS;cas++)
    {
        scanf("%d",&n);
        for(int i = 0; i < n;i++)
        {
            scanf("%s",s);
            for(int j = 0;j < n;j++)
            {
                if(s[j] == '1')
                    map[i][j] = 1;
                if(s[j] == '0')
                    map[i][j] = 0;
                if(s[j] == '.')
                    map[i][j] = -1;
            }
        }
        for(int i = 0;i < MAXN;i++)
        {
            win[i] = lose[i] = wp[i] = owp[i] = oowp[i] = 0;
        }
        for(int i = 0;i < n;i++)
        {
            for(int j = 0;j < n;j++)
                if(map[i][j] == 1)
                    win[i] += 1;
                else if(map[i][j] == 0)
                    lose[i] += 1;
            wp[i] = win[i]/(win[i]+lose[i]);
        }
        //for(int i = 0;i < n;i++)
         //   printf("wp: %lf ",wp[i]);
        //printf("\n");
        for(int i = 0;i < n;i++)
        {
            temp = 0;
            for(int j = 0;j < n;j++)
            {
                wintemp = win[j];
                losetemp = lose[j];
                if(map[j][i] == 1)
                    wintemp -= 1;
                else if(map[j][i] == 0)
                    losetemp -= 1;
                if(map[j][i] != -1)
                    temp+= wintemp/(wintemp+losetemp);
            }
            owp[i] = 1.0/(win[i]+lose[i])*temp;
        }
        //for(int i = 0;i < n;i++)
        //    printf("owp: %lf ",owp[i]);
        //printf("\n");
        for(int i = 0;i < n;i++)
        {
            for(int j = 0;j < n;j++)
                if(map[i][j] != -1)
                    oowp[i] += owp[j];
            oowp[i] = oowp[i]/(win[i]+lose[i]);
        }
        printf("Case #%d:\n",cas);
        for(int i = 0;i < n;i++)
        {
            rpi[i] = 0.25*wp[i]+0.5*owp[i]+0.25*oowp[i];
            printf("%.8lf\n",rpi[i]);
        }
    }
    fclose(stdin);
    fclose(stdout);
}
