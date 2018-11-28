#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

#define SQR(_x) ((_x)*(_x))
#define DIST(_x1,_y1,_x2,_y2) (sqrt(SQR((double)((_x1)-(_x2)))+SQR((double)((_y1)-(_y2)))))

int main(void)
{
    int caso,C,N,X[64],Y[64],R[64];

    scanf("%d",&C);
    for(caso = 1; caso <= C; caso++)
    {
        scanf("%d",&N);
        for(int i = 0; i < N; i++)
            scanf("%d %d %d",X+i,Y+i,R+i);

        double r,x;
        if (N == 1) r = (double)(R[0]);
        else if (N == 2) r = max((double)R[0],(double)R[1]);
        else
        {
            r = max((double)R[2],(DIST(X[0],Y[0],X[1],Y[1])+(double)R[0]+(double)R[1])/2.0);
            x = max((double)R[1],(DIST(X[0],Y[0],X[2],Y[2])+(double)R[0]+(double)R[2])/2.0);
            r = min(r,x);
            x = max((double)R[0],(DIST(X[1],Y[1],X[2],Y[2])+(double)R[1]+(double)R[2])/2.0);
            r = min(r,x);
        }
        printf("Case #%d: %.6lf\n",caso,r);
    }
    

    return(0);
}

