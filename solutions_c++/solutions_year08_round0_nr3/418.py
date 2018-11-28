//---------------------------------------------------------------------------

#include <clx.h>
#pragma hdrstop

//---------------------------------------------------------------------------
#include <map>
#include <string>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <math.h>

using namespace std;

#define VS vector<string>
#define VI vector<int>
#define PB push_back
#define FOR(i,m) for(i=0;i<m;++i)
#define SFOR(i,s,m) for(i=s;i<m;++i)
#define SZ(a) (int)a.size()
#define P2(a) (a)*(a)

#pragma argsused
double area(double x1, double y1, double gap, double R) {
    long long i,j,n=400000,nin=0,nt;
    double x,y,p;
    FOR(i,n)
    {   x=x1+(i+0.5)*gap/n;
        if (P2(R)<P2(x)) continue;
        //найти к нему y, который на границе
        y=sqrt(P2(R)-P2(x));
        p=floor((y-y1-gap*0.5/n)*n/gap);
        nt=(long long)(p);
        //nt штук входит, остальные нет
        if (nt>n) nt=n;
        if (nt>0)
            nin+=nt;
    }
    return nin*P2(gap)*(1.0/n)/n;
}

double prob(double Rfly, double Rout, double Rcontour, double Rstr, double gap) {
    //учтем радиус мухи в конструкции ракетки (чтобы потом считать его 0)
    Rcontour+=Rfly;
    Rstr+=Rfly;
    gap-=2*Rfly;
    if (gap<=0) return 1.0; 
    //основная часть
    double Rin=Rout-Rcontour,period=2*Rstr+gap;
    double Sall=M_PI*Rout*Rout,Sgap=0;
    int i,j;
    for (i=0; Rstr+i*period<Rin; i++)
    {   double x1=Rstr+i*period;
        for (j=0; j<1; j++)
        {   //сначала диагональ (i==j)
            if (2*P2(x1+gap)<P2(Rin))
            {   //ура, целиком
                Sgap+=P2(gap);
                break;
            }
            if (2*P2(x1)>P2(Rin))
            {   //ура, не поместилось
                break;
            }
            Sgap+=area(x1,x1,gap,Rin);
        }
        //потом то, что под диагональю (и умножить на 2)
        for (j=0; j<i && P2(x1)+P2(Rstr+j*period)<P2(Rin); j++)
        {   double y1=Rstr+j*period;
            if (P2(x1+gap)+P2(y1+gap)<P2(Rin))
            {   //поместилось целиком
                Sgap+=2*P2(gap);
                continue;
            }
            Sgap+=2*area(x1,y1,gap,Rin);
        }
    }
    Sgap*=4;
    return 1-Sgap/Sall;
}


int main(int argc, char* argv[])
{
    FILE *in, *out;
    int N,i;

//    in = fopen("C-test.in","rt");
//    out= fopen("C-test.out","wt");
    in = fopen("C-small-attempt1.in","rt");
    out= fopen("C-small-attempt1.out","wt");
    fscanf(in,"%d\n",&N);
    SFOR(i,1,N+1)
    {   double f,R,t,r,g;
        fscanf(in,"%lf %lf %lf %lf %lf\n", &f, &R, &t, &r, &g);
        double ret=prob(f,R,t,r,g);
        fprintf(out,"Case #%d: %.6lf\n",i,floor(ret*1000000)/1000000);
        fflush(out);
    }
    fclose(in);
    fclose(out);
    return 0;
}
//---------------------------------------------------------------------------
 