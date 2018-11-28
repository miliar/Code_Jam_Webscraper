#include<cstdio>
#include<cstring>
#include<cmath>
using namespace std;
int T;
int N, PD, PG;

void getin()
{
    scanf("%d%d%d",&N,&PD,&PG);
}

void work()
{
    for (int i=1;i<=N;i++)
    {
        int D=i;
        int d=D*PD/100;
        if (d*100!=D*PD) continue;
        if (d!=0)
        {
            if (D==d)
            {
                if (PG!=0) { printf("Possible\n"); return; }
                else { printf("Broken\n"); return; }
            }
            else if (D>d)
            {
                if (PG==0 || PG==100) { printf("Broken\n"); return; }
                else { printf("Possible\n"); return; }
            }
        }
        else 
        {
            if (PG==100) { printf("Broken\n"); return; }
            else { printf("Possible\n"); return; }
        }
    }
    printf("Broken\n");
}

int main()
{
//    freopen("yy.in","r",stdin);
//    freopen("yy.out","w",stdout);
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
//    freopen("-large.in","r",stdin);
//    freopen("-large.out","w",stdout);    
    scanf("%d",&T);
    for (int ii=1;ii<=T;ii++)
    {
        printf("Case #%d: ",ii);
        getin();
        work();
    }
    return 0;
}
