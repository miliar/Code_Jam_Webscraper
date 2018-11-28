#include <iostream>
#include <fstream>
#include <algorithm>
#include <climits>
#include <cstdio>
#include <cmath>
#include <cstring>



using namespace std;


int N;

char mat[110][110];

double WP[110];
double OWP[110];

double OOWP[110];
double res[110];

void work()
{
    memset(WP,0,sizeof(WP));
    memset(OWP,0,sizeof(OWP));
    memset(OOWP,0,sizeof(OOWP));
    int a,b;
    for(int i=0;i<N;i++)
    {
        a=b=0;
        for(int j=0;j<N;j++)
        {
            if('.'==mat[i][j])
            continue;
            b++;
            if('1'==mat[i][j])
            a++;
        }
        if(b)
        WP[i]=double(a)/double(b);
    }
    int c,d;
    double tmp;

    for(int i=0;i<N;i++)
    {
        tmp=0;
        b=0;
        for(int j=0;j<N;j++)
        {
            if('.'==mat[i][j])
            continue;
            b++;
            c=0,d=0;
            for(int k=0;k<N;k++)
            {
                if(i==k)
                continue;
                if('.'==mat[j][k])
                continue;
                d++;
                if('1'==mat[j][k])
                c++;
            }
            if(d)
            tmp+=double(c)/double(d);
        }
        if(b)
        OWP[i]=tmp/b;
    }


    for(int i=0;i<N;i++)
    {
        tmp=0;
        b=0;
        for(int j=0;j<N;j++)
        {
            if('.'==mat[i][j])
            continue;
            b++;
            tmp+=OWP[j];

        }
        if(b)
        OOWP[i]=tmp/double(b);

    }

    for(int i=0;i<N;i++)
    {
        res[i]=0.25*WP[i]+0.5*OWP[i]+0.25*OOWP[i];
    }



}





int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.out","w",stdout);

    int T;
    scanf("%d",&T);

    for(int loop=1;loop<=T;loop++)
    {
        scanf("%d",&N);

        for(int i=0;i<N;i++)
        scanf("%s",mat[i]);
        work();
        printf("Case #%d:\n",loop);
        for(int i=0;i<N;i++)
        printf("%0.10lf\n",res[i]);
    }














    return 0;
}
