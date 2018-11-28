#include <iostream>
#include <fstream>

using namespace std;

ifstream fin("a.in");
ofstream fout("a.out");

#define MAX 20010
#define INF 0x3f3f3f3f

int T,M;
int val[MAX], a[MAX][2], op[MAX], ch[MAX];

void calc(int nod)
{
    if ( nod > M ) return;
    if( val[nod] != -1)
    {
        a[nod][val[nod]] = 0;
    }
    else
    {
        calc(2*nod);
        calc(2*nod+1);

        if ( op[nod] == 1 ) // AND
        {
            a[nod][1] = a[2*nod][1] + a[2*nod+1][1];
            a[nod][0] = min( min( a[2*nod][0]+a[2*nod+1][0], a[2*nod][0] + a[2*nod+1][1]), a[2*nod][1] + a[2*nod+1][0] );

            if ( ch[nod] == 1)
            {
                int aux1 = a[2*nod][0] + a[2*nod+1][0] + 1;
                int aux2 = min( min( a[2*nod][1]+a[2*nod+1][1], a[2*nod][0] + a[2*nod+1][1]), a[2*nod][1] + a[2*nod+1][0] ) + 1;
                if ( a[nod][0] > aux1 )
                    a[nod][0] = aux1;
                if ( a[nod][1] > aux2 )
                    a[nod][1] = aux2;
            }
        }
        else
        {
            a[nod][0] = a[2*nod][0] + a[2*nod+1][0];
            a[nod][1] = min( min( a[2*nod][1]+a[2*nod+1][1], a[2*nod][0] + a[2*nod+1][1]), a[2*nod][1] + a[2*nod+1][0] );
            if ( ch[nod] == 1)
            {
                int aux1 = a[2*nod][1] + a[2*nod+1][1] + 1;
                int aux2 = min( min( a[2*nod][0]+a[2*nod+1][0], a[2*nod][0] + a[2*nod+1][1]), a[2*nod][1] + a[2*nod+1][0] ) + 1;
                if ( a[nod][1] > aux1 )
                    a[nod][1] = aux1;
                if ( a[nod][0] > aux2 )
                    a[nod][0] = aux2;
            }

        }
        if ( a[nod][1] > INF )
                a[nod][1] = INF;
        if ( a[nod][0] > INF )
                a[nod][0] = INF;
    }
}

int main()
{
    fin>>T;
    int V;
    for ( int z = 1; z<=T; z++)
    {
        fin>>M>>V;
        for (int i = 0; i < MAX; i++)
        {
            op[i] = -1;
            a[i][0] = a[i][1] = INF;
            val[i] = -1;
        }

        for (int i = 1; i <= (M-1)/2; i++)
                 fin>>op[i]>>ch[i];
        for (int i =  1; i<= (M+1)/2; i++)
        {
            fin>>val[(M-1)/2+i];
        }

        calc(1);
        if ( a[1][V] < INF )
            fout<<"Case #"<<z<<": "<<a[1][V]<<"\n";
        else
            fout<<"Case #"<<z<<": IMPOSSIBLE\n";
    }


    return 0;
}
