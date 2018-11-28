#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

int main ()
{

    int N;

    // input output streams
    freopen ("B-large.in", "r", stdin);
    //freopen ("input2.txt", "r", stdin);
    freopen ("output.txt", "w", stdout);

    // number of cases
    scanf ("%d", &N);
    if (N < 1)
        printf ("Error: input file not found\n");

    // for each case
    for (int caseId=1; caseId<=N; caseId++)
    {
        int n;
        scanf ("%d", &n);
        double sumx=0, sumy=0, sumz=0, sumvx=0, sumvy=0, sumvz=0;
        for (int i=0; i<n; i++)
        {
            int x,y,z,vx,vy,vz;
            //scanf ("%lf%lf%lf%lf%lf%lf", &x, &y, &z, &vx, &vy, &vz);
            scanf ("%d%d%d%d%d%d", &x, &y, &z, &vx, &vy, &vz);
            //printf ("%f", x);
            sumx +=x;
            sumy +=y;
            sumz +=z;
            sumvx +=vx;
            sumvy +=vy;
            sumvz +=vz;
        }
        //printf ("%f%f%f%f%f%f\n", sumx, sumy, sumz, sumvx, sumvy, sumvz);
        sumx /= n;
        sumz /= n;
        sumy /= n;

        sumvx /= n;
        sumvz /= n;
        sumvy /= n;

        double startd = sqrt (abs(sumx*sumx+ sumy*sumy+ sumz*sumz));
        double startv = sqrt (abs(sumvx*sumvx+ sumvy*sumvy+ sumvz*sumvz));

        double dot=0; // distance from start to closest ppoint
        double x=0, u=0;
        if (abs(startv) > 0.000001)
        {
        dot += sumx*sumvx;
        dot += sumy*sumvy;
        dot += sumz*sumvz;
        dot = 0-dot;
        dot /= startv;
        x = dot/startv;
        u=sqrt(abs(startd*startd - dot*dot));
        }
        else {
            //printf ("this  ");
            x = 0;
            u=startd;
        }

        if (x<0)
        {
            u=startd;
            x=0;
        }
        printf ("Case #%d: %f %f\n", caseId, u, x);
    }
    return 0;
}
