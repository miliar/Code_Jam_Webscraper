//---------------------------------------------------------------------------

#include <clx.h>
#pragma hdrstop

//---------------------------------------------------------------------------
#include <map>
#include <string>
#include <vector>
#include <stdio.h>

using namespace std;

#define VS vector<string>
#define VI vector<int>
#define PB push_back
#define FOR(i,m) for(i=0;i<m;++i)
#define SFOR(i,s,m) for(i=s;i<m;++i)
#define SZ(a) (int)a.size()

int nsw(int S, VI r)
{   //количество поисковых машин и индексы запросов
    int i,j,k,kbest,n,nmin=SZ(r);
    FOR(i,S)
    {   n=0;
        FOR(j,SZ(r))
            if (r[j]==i) n++;
        if (n<nmin) nmin=n;
    }
    if (nmin==0) return nmin;
    int start[100][1001];
    //количество запросов, которые сможет обработать i-ый поисковик,
    //включившись перед j-ым запросом
    FOR(i,S)
    {   start[i][SZ(r)]=0;
        for(j=SZ(r)-1; j>=0; j--)
            if (r[j]==i) start[i][j]=0; //ни одного
                    else start[i][j]=start[i][j+1]+1;   //этот и следующие
    }
    //на каждом шагу жадно выбираем тот, который дает больше всего
    i=0;    //индекс текущего запроса
    j=-1;    //индекс текущей машины
    n=-1;    //количество переключений
    while (i<SZ(r))
    {   kbest=-1;
        FOR(k,S)
            if (k!=j && (kbest==-1 || start[k][i]>start[kbest][i]))
                kbest=k;
        n++;
        j=kbest;
        i+=start[kbest][i];
    }
    return n;
}

#pragma argsused
int main(int argc, char* argv[])
{
    FILE *in, *out;
    int N,i,j,S,Q,ind;
    char tmp[100];
    string req;
    VS eng;
    VI r;
    in = fopen("A-large.in","rt");
    out= fopen("A-large.out","wt");
/*    in = fopen("A-test.in","rt");
    out= fopen("A-test.out","wt");*/
    fscanf(in,"%d\n",&N);
    SFOR(i,1,N+1)
    {   eng=VS(0);
        fscanf(in,"%d\n",&S);
        FOR(j,S)
        {   fscanf(in,"%s\n",tmp);
            eng.PB(string(tmp));
        }
        r=VI(0);
        fscanf(in,"%d\n",&Q);
        FOR(j,Q)
        {   fscanf(in,"%s\n",tmp);
            req=string(tmp);
            ind=find(eng.begin(),eng.end(),req)-eng.begin();
            if (SZ(r)==0 || ind!=r[SZ(r)-1])
                r.PB(ind);
        }
        fprintf(out,"Case #%d: %d\n",i,nsw(S, r));
    }
    fclose(in);
    fclose(out);
    return 0;
}
//---------------------------------------------------------------------------
