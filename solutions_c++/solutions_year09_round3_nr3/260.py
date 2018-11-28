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

#define PROB "c"
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
        int P,Q,i,j,k,sum,minsum;
        fscanf(in,"%d %d\n",&P,&Q);
        VI inds(Q);
        FOR(i,Q)
            fscanf(in,"%d",&(inds[i]));
        //process
        //bruteforce - try all orders of release and choose the cheapest
        minsum=2*P*Q;
        FOR(i,Q)
            inds[i]--;
        do
        {   vector<bool> cells(P,true);
            sum=0;
            FOR(i,Q)
            {   //release prisoner inds[i]
                cells[inds[i]]=false;
                for (j=inds[i]-1; j>=0; j--)
                    if (!cells[j])
                        break;
                    else sum++;
                for (j=inds[i]+1; j<P; j++)
                    if (!cells[j])
                        break;
                    else sum++;
            }
            if (minsum>sum)
                minsum=sum;
        }
        while (next_permutation(inds.begin(),inds.end()));
        //write output
        fprintf(out,"Case #%d: %d\n",it,minsum);
    }
    fclose(in);
    fclose(out);
    return 0;
}
//---------------------------------------------------------------------------
 