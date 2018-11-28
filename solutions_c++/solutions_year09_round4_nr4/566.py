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

#define PROB "D"
//#define SIZE "test"
#define SIZE "small"
//#define SIZE "large"
#define ATT "0"

//---------------------------------------------------------------------------
double calc(int n, VI x, VI y, VI r)
{   if (n==1)
        return r[0];
    if (n==2)
        return max<int>(r[0],r[1]);
    if (n>3)
        return -1;
    //try to cover each pair with 1 sprink and the rest with second
    VI ord;
    ord.PB(0);
    ord.PB(1);
    ord.PB(2);
    double rmin=1000000,r1,r2;
    do
    {   r1 = 0.5*(sqrt((x[ord[0]]-x[ord[1]])*(x[ord[0]]-x[ord[1]]) + (y[ord[0]]-y[ord[1]])*(y[ord[0]]-y[ord[1]])) + r[ord[0]] + r[ord[1]]);
        r2 = r[ord[2]];
        rmin=min<double>(rmin,max<double>(r1,r2));
    }
    while(next_permutation(ord.begin(),ord.end()));
    return rmin;
}
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
        int i,n;
        fscanf(in,"%d\n",&n);
        VI x(n),y(n),r(n);
        FOR(i,n)
            fscanf(in,"%d %d %d\n",&(x[i]),&(y[i]),&(r[i]));
        //write output
        fprintf(out,"Case #%d: %.6lf\n",it,calc(n,x,y,r));
    }
    fclose(in);
    fclose(out);
    return 0;
}
//---------------------------------------------------------------------------
 