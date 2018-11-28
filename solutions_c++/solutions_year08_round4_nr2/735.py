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

#define PROB "B"
//#define SIZE "test"
#define SIZE "small"
//#define SIZE "large"
#define ATT "2"

//---------------------------------------------------------------------------

#pragma argsused
int main(int argc, char* argv[])
{
    FILE *in, *out;
    int C,it;
    string name=PROB+string("-")+SIZE;
    if (string(SIZE)==string("small"))
        name+=string("-attempt")+ATT;
    in = fopen((name+".in").c_str(),"rt");
    out = fopen((name+".out").c_str(),"wt");
    fscanf(in,"%d\n",&C);
    SFOR(it,1,C+1)
    {   //read input
        int N,M,A;
        fscanf(in,"%d %d %d\n",&N,&M,&A);
        //process
        int x1,x2,y1,y2;
        bool found=false;
        FOR(x1,N+1)
        FOR(y1,M+1)
        FOR(x2,N+1)
        FOR(y2,M+1)
            if (abs(x1*y2-x2*y1)==A)
            {   found=true;
                goto L1;
            }
        //write output
L1:     if (found)
            fprintf(out,"Case #%d: 0 0 %d %d %d %d\n",it,x1,y1,x2,y2);
        else
            fprintf(out,"Case #%d: IMPOSSIBLE\n",it);
    }
    fclose(in);
    fclose(out);
    return 0;
}
//---------------------------------------------------------------------------
 