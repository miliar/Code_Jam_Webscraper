#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int MAX = 24*60;

struct train
{
    int depart, arrive , flag;
};

train times[ 300 ];
int nt[ MAX + 100 ][ 2 ];
int na,nb,t;

bool compare(const train &a, const train &b)
{
    return a.depart  < b.depart;
}

int main()
{
    freopen("trainin.txt", "r", stdin);
    freopen("trainout.txt", "w" , stdout);
    int i,j,k,n;

    scanf("%d", &n);

    for(k=1; k<=n; k++)
    {
        int res[2];
        res[0] = res[1]= 0;
        memset( nt, 0, sizeof nt );
        scanf("%d %d %d", &t , &na, &nb);
        for(i = 0; i < na; i++)
        {
            char temp1[ 10 ], temp2[ 10 ];
            int h1, m1, h2,m2;
            scanf("%s %s", temp1, temp2 );
            sscanf(temp1, "%d:%d", &h1,&m1);
            sscanf(temp2, "%d:%d", &h2,&m2);
            times[i].arrive = h2*60 + m2 + t;
            times[i].depart = h1*60 + m1 ;
            times[i].flag = 0;
        }
        for(i=0;i<nb; i++)
        {
            char temp1[ 10 ], temp2[ 10 ];
            int h1, m1, h2,m2;
            scanf("%s %s", temp1, temp2 );
            sscanf(temp1, "%d:%d", &h1,&m1);
            sscanf(temp2, "%d:%d", &h2,&m2);
            times[i+na].arrive = h2*60 + m2 + t;
            times[i+na].depart = h1*60 + m1 ;
            times[i+na].flag = 1;
        }
        sort( times, times + na+nb , compare);

        for(i=0;i < na+nb;i++)
        {
            if(nt[times[i].depart][times[i].flag]==0)
            {
                res[ times[i].flag ]++;
                for(j = times[i].arrive ; j < MAX ; j++ )
                 nt[ j ][ !times[i].flag ] ++;
            }
            else
            {
                for(j = times[i].depart ; j < MAX; j++)
                 nt[j][ times[i].flag ] --;
                for(j = times[i].arrive; j < MAX ; j++)
                 nt[j][ !times[i].flag ] ++;
            }
        }
        printf("Case #%d: %d %d\n", k , res[0], res[1]);
    }

    return 0;
}
