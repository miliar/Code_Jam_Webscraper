#include<iostream>
#include<sstream>
#include<string>
#include<queue>

#define FOR(i,a,n) for(int i=a;i<n;i++)
#define FORN(i,n) FOR(i,0,n)

using namespace std;

int N,T,NA,NB,cap[1010][1010],top,resa,resb;
string arr,dep;
int ha,ma,hd,md;
char basura;
int A[1010],D[1010];

int pred[1010];
int vis[1010];

int mf()
{
    queue<int> Q;

    Q.push(0);

    FORN(i,top+3)
        vis[i]=0;

    FORN(i,top+1)
        pred[i]=-1;

    while (!Q.empty())
    {
        int curr = Q.front(); Q.pop();

        if (vis[curr])
            continue;

        if (curr==top)
            break;

        vis[curr]=true;

        FORN(i,top+1)
        {
            if (!vis[i]&&cap[curr][i]>0)
            {
                if (pred[i]==-1&&i!=0)
                    pred[i]=curr;

                Q.push(i);
            }
        }
    }

    int x = top;

    if (pred[x]==-1)
        return 0;

    int mcap=20000000;

    while (pred[x]!=-1)
    {
        mcap=min(mcap,cap[pred[x]][x]);
        x=pred[x];
    }

    x = top;

    while (pred[x]!=-1)
    {
        cap[pred[x]][x]-=mcap;
        cap[x][pred[x]]+=mcap;
        x=pred[x];
    }

    return mcap;
}

int main()
{
    cin>>N;

    FOR(caso,1,N+1)
    {
        memset(cap,0,sizeof(cap));

        cin>>T>>NA>>NB;

        top = 2*(NA+NB)+1;

        FORN(i,NA+NB)
        {
            cin>>dep>>arr;

            stringstream ssa(arr),ssd(dep);

            ssa>>ha>>basura>>ma;
            ssd>>hd>>basura>>md;

            A[i]=ha*60+ma;
            D[i]=hd*60+md;
        }

        FORN(i,NA)
            FORN(j,NB)
                if(A[i]+T<=D[NA+j])
                    cap[i+1][2*NA+NB+j+1]=1;

        FORN(i,NB)
            FORN(j,NA)
                if(A[NA+i]+T<=D[j])
                    cap[NA+i+1][NA+NB+j+1]=1;

        FORN(i,NA+NB)
            cap[0][i+1]=1;

        FORN(i,NA+NB)
            cap[NA+NB+i+1][top]=1;

        while (mf());

        resa=resb=0;

        FORN(i,NA)
            if(!cap[top][NA+NB+1+i])
                resa++;

        FORN(i,NB)
            if(!cap[top][2*NA+NB+1+i])
                resb++;

        printf("Case #%d: %d %d\n",caso,resa,resb);
    }

    return 0;
}
