//---------------------------------------------------------------------------

#include <clx.h>
#pragma hdrstop

#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <stdio.h>
#include <stdarg.h>
#include <stddef.h>
#include <stdlib.h>
#include <math.h>

using namespace std;

#define VS vector<string>
#define VI vector<int>
#define SS stringstream
#define PB push_back
#define SZ(a) (int)a.size()
#define FOR(i,m) for(i=0;i<m;++i)
#define SFOR(i,s,m) for(i=s;i<m;++i)
#define DEB(x) cout<<#x<<" = "<<(x)<<endl;

#define PROB "A"
//#define SIZE "test"
#define SIZE "small"
//#define SIZE "large"
#define ATT "0"

//---------------------------------------------------------------------------

#pragma argsused
int main(int argc, char* argv[])
{
    FILE *in, *out;
    int N,it;
    string name=PROB+string("-")+SIZE;
    if (string(SIZE)==string("small"))
        name+=string("-attempt")+ATT;
    in = fopen((name+".in").c_str(),"rt");
    out = fopen((name+".out").c_str(),"wt");
    fscanf(in,"%d\n",&N);
    SFOR(it,1,N+1)
    {   //read input
        int M,V,i,t1,t2;
        VI igate,ich,lval;
        fscanf(in,"%d %d\n",&M,&V);
        FOR(i,(M-1)/2)
        {   fscanf(in,"%d %d\n",&t1,&t2);
            igate.PB(t1);
            ich.PB(t2);
        }
        FOR(i,(M+1)/2)
        {   fscanf(in,"%d\n",&t1);
            lval.PB(t1);
        }
        //process
        //try all possible masks of changes
        int ngates=(M-1)/2;   //
        int chmask,nch,minnch=ngates+1;
        bool all;
        VI g;
        FOR(chmask,(1<<ngates))
        {   //number of bits to change
            nch=0;
            FOR(i,ngates)
                if ((chmask & (1<<i))>0)
                    nch++;
            if (nch>minnch) continue;
            //check whether all chosen gates can be changed
            all=true;
            FOR(i,ngates)
                if ((chmask & (1<<i))>0 && ich[i]==0)
                {   all=false;
                    break;
                }
            if (!all) continue;
            //do the changes
            g=igate;
            FOR(i,ngates)
                if ((chmask & (1<<i))>0)
                    g[i]=1-g[i];
            //count the values of the tree nodes
            VI res(M,-1);
            SFOR(i,ngates,M)
                res[i]=lval[i-ngates];
            for (i=ngates-1; i>=0; i--)
            {   //count node (i+1)
                if (g[i]==1)
                {   //AND
                    res[i]=res[2*(i+1)-1] & res[2*(i+1)];
                }
                else
                {   //OR
                    res[i]=res[2*(i+1)-1] | res[2*(i+1)];
                }
            }
            if (res[0]==V)
                minnch=min<int>(minnch,nch);
        }
        //write output
        if (minnch<ngates+1)
            fprintf(out,"Case #%d: %d\n",it,minnch);
        else
            fprintf(out,"Case #%d: IMPOSSIBLE\n",it);
    }
    fclose(in);
    fclose(out);
    return 0;
}
//---------------------------------------------------------------------------
 