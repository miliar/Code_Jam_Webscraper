#include<iostream>
#include<string>

#define FOR(i,a,n) for(int i=a;i<n;i++)
#define FORN(i,n) FOR(i,0,n)

using namespace std;

int N,S,Q,pos,res,mimax,M[110][1010];
string engines[110],queries[1010],basura;

int main()
{
    cin>>N;

    FOR(caso,1,N+1)
    {
        cin>>S;
        getline(cin,basura);

        FORN(i,S)
            getline(cin,engines[i]);

        cin>>Q;
        getline(cin,basura);

        FORN(i,Q)
            getline(cin,queries[i]);

        FORN(i,S)
        {
            pos=-1;

            FORN(j,Q)
            {
                if(queries[j]==engines[i])
                {
                    FOR(x,pos+1,j)
                        M[i][x]=j-x;

                    M[i][j]=0;
                    pos=j;
                }
            }

            FOR(x,pos+1,Q)
                M[i][x]=Q-x;
        }

        res=-1;
        pos=0;

        while(pos!=Q)
        {
            res++;
            mimax=0;

            FORN(i,S)
                mimax=max(mimax,M[i][pos]);

            pos+=mimax;
        }

        if(Q==0)
            res=0;

        printf("Case #%d: %d\n",caso,res);
    }

    return 0;
}
