/*  Google Code Jam Round 1B 2011
    Problem A. RPI
    Varot Premtoon 21 May 2554 */

#include <cstdio>

char tab[200][200];
double wp[200],owp[200],oowp[200];
double res[200];
int wpi[200][2];
int n;

int fwp()
{
    int all,win;
    int i,j;
    for(i=0;i<n;i++) {
        all = win = 0;
        for(j=0;j<n;j++) {
            if(tab[i][j]!='.') all++;
            if(tab[i][j]=='1') win++;
        }
        wp[i] = (double)((double)(win) / (double)(all*4.0));
    }
    return 0;
}

int fowp()
{
    int i,j,k;
    double awp;
    int all,win,opp;
    for(i=0;i<n;i++) {
        awp = 0;
        opp = 0;
        for(j=0;j<n;j++) {
            if(j==i||tab[i][j]=='.') continue;
            all = win = 0;
            opp++;
            for(k=0;k<n;k++) {
                if(k==i) continue;
                if(tab[j][k]!='.') all++;
                if(tab[j][k]=='1') win++;
            }
            awp += (double)((double)(win) / (double)(all));
        }
        owp[i] = (double)(awp / (double)(opp*2.0));
    }
    return 0;
}

int foowp()
{
    int i,j,k;
    double sum = 0;
    int opp;
    /*for(i=0;i<n;i++) sum += owp[i];
    for(i=0;i<n;i++) {
        oowp[i] = (double)((double)(sum - owp[i]) / (double)(n-1));
    }/**/
    for(i=0;i<n;i++) {
        sum = 0;
        opp = 0;
        for(j=0;j<n;j++) {
            if(j==i||tab[i][j]=='.') continue;
            sum += owp[j];
            opp++;
        }
        oowp[i] = (double)(sum / (double)(opp*2.0));
    }
    return 0;
}

int sol(int cse)
{
    printf("Case #%d:\n",cse);
    int i;
    double A,B;
    A = 0.25000000000000;
    B = 0.50000000000000;
    scanf("%d",&n);
    for(i=0;i<n;i++) scanf("%s",tab[i]);
    fwp();
    fowp();
    foowp();
    /*for(i=0;i<n;i++) {
        printf("PLAYER %d : %lf, %lf, %lf\n",i+1,wp[i],owp[i],oowp[i]);
    }/**/
    //for(i=0;i<n;i++) printf("%.20lf\n",(double)(A*wp[i]+B*owp[i]+A*oowp[i]));
    for(i=0;i<n;i++) printf("%lf\n",(double)(wp[i]+owp[i]+oowp[i]));
    return 0;
}

int main()
{
    int t,i;
    //printf("%.20lf\n",0.55555555555555547000+0.55555555555555547000
    scanf("%d",&t);
    for(i=1;i<=t;i++) sol(i);
    return 0;
}
