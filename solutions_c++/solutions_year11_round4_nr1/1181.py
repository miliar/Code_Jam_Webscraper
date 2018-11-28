//---------------------------------------------------------------------------

#include <stdio.h>
#include <vector>
#include <algorithm>
#pragma hdrstop

using namespace std;
//---------------------------------------------------------------------------
int abs(int a)
{
    if (a<0)
        return -a;
    return a;
}

long int GCD(long int A,long int B)
{
    if (A==0)
    {
        return B;
    }
    return GCD(B%A,A);
}

struct TPasillo
{
    int longitud;
    int w;
};

bool operator<(const TPasillo &a,const TPasillo &b)
{
    if (a.w!=b.w)
    {
        return a.w<b.w;
    }
    return a.longitud<b.longitud;
}

#pragma argsused
int main(int argc, char* argv[])
{
    int T;
    scanf("%d\n",&T);
    for (int t=1;t<=T;t++)
    {
        //general case
        int X, S,R,N,time_;
        scanf("%d %d %d %d %d",&X,&S,&R,&time_,&N);
        double totaltime=0.0f;
        double remainingtime=double(time_);
        int currentpos=0;
        vector<TPasillo> pasillo;
        pasillo.resize(N);
        for (int n=0;n<N;n++)
        {
            int B,E,W;
            scanf("%d %d %d",&B,&E,&W);
            pasillo[n].longitud=E-B;
            pasillo[n].w=W;
            double walk=double(B-currentpos);
            if ((remainingtime*double(R))>=walk)
            {
                //run all
                double actual=walk/double(R);
                remainingtime-=actual;
                totaltime+=actual;
            }
            else
            {
                //run as much as possible
                double actual=(walk-(remainingtime*double(R)))/double(S);
                actual+=remainingtime;
                remainingtime=0.0f;
                totaltime+=actual;
            }
            currentpos=E;
        }
        //run the last part
        double walk=double(X-currentpos);
        if ((remainingtime*double(R))>=walk)
        {
            //run all
            double actual=walk/double(R);
            remainingtime-=actual;
            totaltime+=actual;
        }
        else
        {
            //run as much as possible
            double actual=(walk-(remainingtime*double(R)))/double(S);
            actual+=remainingtime;
            remainingtime=0.0f;
            totaltime+=actual;
        }
        sort(pasillo.begin(),pasillo.end());
        for (int n=0;n<N;n++)
        {
            walk=double(pasillo[n].longitud);
            if ((remainingtime*double(R+pasillo[n].w))>=walk)
            {
                //run all
                double actual=walk/double(R+pasillo[n].w);
                remainingtime-=actual;
                totaltime+=actual;
            }
            else
            {
                //run as much as possible
                double actual=(walk-(remainingtime*double(R+pasillo[n].w)))/double(S+pasillo[n].w);
                actual+=remainingtime;
                remainingtime=0.0f;
                totaltime+=actual;
            }
        }
        printf("Case #%d: %0.15lf\n",t,totaltime);
    }
    return 0;
}
//---------------------------------------------------------------------------


