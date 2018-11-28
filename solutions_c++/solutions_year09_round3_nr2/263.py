#include <stdio.h>
#include <math.h>

inline double sqr(double x){return x*x;}

class TPoint
{
    public:
    double x, y, z;
    void input()
    {
        scanf("%lf%lf%lf", &x, &y, &z);
    }
};

double getD(double A, double B, double t, double n)
{
    return sqr((t*A + B) / n );
}

int main()
{
    int T, test;
    scanf("%d", &T);
    for (test = 1;test<=T;test++)
    {
        int N, i;
        TPoint p[500], v[500];
        double Ax=0.0, Ay=0.0, Az=0.0, Bx=0.0, By=0.0, Bz=0.0;
        scanf("%d", &N);
        for (i=0;i<N;i++)
        {
            p[i].input();
            v[i].input();
            Ax+=v[i].x;
            Ay+=v[i].y;
            Az+=v[i].z;
            Bx+=p[i].x;
            By+=p[i].y;
            Bz+=p[i].z;
        }

        /*double A, B, C, D, n = (double)N, t1, t2;

        A = -1.0*(sqr(Ax) + sqr(Ay) + sqr(Az));
        B = 2.0*(sqr(Ax) + sqr(Ay) + sqr(Az))*sqr(n) - 2.0*(Ax*Bx + Ay*By + Az*Bz);
        C = 2.0*(Ax*Bx + Ay*By + Az*Bz)*sqr(n) - 1.0*(sqr(Bx) + sqr(By) + sqr(Bz) );
        D = sqr(B) - 4.0*A*C;

        if (D>=0.0)
        {
            t1 = (-B + sqrt(D))/(2.0*A);
            t2 = (-B - sqrt(D))/(2.0*A);
            printf("%lf %lf\n", t1, t2);
        }
        else printf("---\n");*/

        double t, A, B, Dmin, Tmin = 0.0, n = (double)N;
        A = sqr(Ax) + sqr(Ay) + sqr(Az);
        B = Ax*Bx + Ay*By + Az*Bz;

        Dmin = getD(Ax, Bx, 0.0, n) + getD(Ay, By, 0.0, n) + getD(Az, Bz, 0.0, n);

        if (A!=0.0)
        {
            t = -B/A;
            if (t>0.0)
            {
                double d = getD(Ax, Bx, t, n) + getD(Ay, By, t, n) + getD(Az, Bz, t, n);
                //if (d<Dmin)
                {
                    Dmin = d;
                    Tmin = t;
                }
            }
            //printf("t = %lf\n", t);
        }
        //else printf("---\n");
        printf("Case #%d: %1.8lf %1.8lf\n", test ,sqrt(Dmin), Tmin);
    }

    return 0;
}
