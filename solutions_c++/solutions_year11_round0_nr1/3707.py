#include<cstdio>
#include<cstdlib>

#define MAX(x,y) (x) > (y) ? (x) : (y)

struct action
{
    char col;
    int but;
};

action acts[110];
int N;

void solve(int T)
{
    int i,j,k;
    scanf("%d ", &N);
    for(i=0; i<N; i++)
        scanf("%c %d ", &acts[i].col, &acts[i].but);

    int actt=0;
    int lastacto=0;
    int lastactb=0;
    int poso=1;
    int posb=1;

    for(i=0; i<N; i++)
    {
        if(acts[i].col == 'B')
        {
            int work = abs(acts[i].but - posb) + 1;
            actt = MAX(lastactb + work, actt+1);
            posb = acts[i].but;
            lastactb = actt;
        }
        else
        {
            int work = abs(acts[i].but - poso) + 1;
            actt = MAX(lastacto + work, actt+1);
            poso = acts[i].but;
            lastacto = actt;
        }
    }

    printf("Case #%d: %d\n", T, actt);
}

int main()
{
    int i,T;
    scanf("%d", &T);

    for(i=0; i<T; i++)
    {
        solve(i+1);
    }

    return 0;
}
