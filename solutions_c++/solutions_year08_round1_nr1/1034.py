#include <stdio.h>
#include <string>
using namespace std;

#define MAX 12
#define INF 10000000001LL

long long cap[2*MAX+1][2*MAX+1], cost[2*MAX+1][2*MAX+1], d[2*MAX+1], tata[2*MAX+1],sursa,dest, rez;
int n,z;

void init()
{
        for (int i=0; i<=dest; i++)
                for(int j=0; j<=dest; j++)
                        {
                        cap[i][j] = -1;
                        cost[i][j] = INF;
                        }
        for (int i = 1; i<=n; i++)
                {
                cap[sursa][i] = 1;
                cost[sursa][i] = 0;
                cost[i][sursa]=0;
                }
        for (int i=n+1; i<=2*n; i++)
                {
                cap[i][dest]=1;
                cost[i][dest]=0;
                cost[dest][i]=0;
                }
}

void drum_minim()
{
        for (int i = sursa; i<=dest; d[i] = INF, tata[i]=0, i++);
        d[sursa]=0;
        int ok;
        do {
            ok = 0;
            for (int i=sursa; i<=dest; i++)
                if (d[i] != INF)
                        for (int j=sursa; j<=dest; j++)
                                if (cap[i][j] == 1 && d[i] +cost[i][j] < d[j])
                                {
                                        d[j] = d[i] + cost[i][j];
                                        tata[j] = i;
                                        ok =1;
                                };
            }
        while (ok == 1);
}

void drum()
{
        for (int j,i = dest; i!=0; i=j )
        {
                j= tata[i];
                cap[j][i]=0;
                cap[i][j]=1;
        }
}


int gata()
{
        int flux =0;
        for (int i=n+1; i<=2*n; i++)
                if (cap[i][dest] == 0)
                        flux++;
        return flux==n;
}


void afisare()
{
    rez= 0;
        for (int i=1; i<=n; i++)
                for (int j=n+1; j<=2*n; j++)
                        if (cap[i][j] == 0 && cost[i][j] != INF)
                                rez+=cost[i][j];


        //printf("%lld\n", rez);
        printf("Case #%d: %lld \n", z,rez);

}

void citire()
{
        freopen("cc.in", "r", stdin);
        int T;
        scanf("%d\n", &T);
        for ( z = 1; z<=T; z++)
        {

            scanf("%d\n", &n);
            sursa=0; dest = 2*n+1;
            memset(cap,0, sizeof(cap));
            memset(cost,0,sizeof(cost));
            init();
            for (int x,i = 1; i<=n; i++)
            {
                for (int j = 1; j<=n; j++)
                {
                        scanf("%d", &x);
                        cap[i][n+j] = 1;
                        cost[i][n+j] = x;
                        cost[n+j][i] = -x;
                };
            scanf("\n");
            }

             do {
                drum_minim();
                drum();
            }
            while (!gata() );
            afisare();


        }
            fclose(stdin);
}

int main()
{
        freopen("cc.out", "w", stdout);
        citire();
        fclose(stdout);


        return 0;
}



