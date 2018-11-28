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
//#define SIZE "small"
#define SIZE "large"
#define ATT "0"

//---------------------------------------------------------------------------
vector<int> pows;

/*string snapper_fast(int N, int K)
{
if ((K+1)%pows[N]==0)
    return "ON";
return "OFF";
}*/
//---------------------------------------------------------------------------

#pragma argsused
int main(int argc, char* argv[])
{
    FILE *in, *out;
    int T,it;
    string name=PROB+string("-")+SIZE;
    if (string(SIZE)==string("small"))
        name+=string("-attempt")+ATT;
    in = fopen((name+".in").c_str(),"rt");
    out = fopen((name+".out").c_str(),"wt");
    fscanf(in,"%d\n",&T);

    pows.push_back(1);
    SFOR(it,1,31)
        pows.push_back(pows[it-1]*2);

    SFOR(it,1,T+1)
    {   //read input
        int N,K;
        fscanf(in, "%d% d\n",&N,&K);
        //write output
        if ((K+1)%pows[N]==0)
            fprintf(out,"Case #%d: ON\n",it);
       else fprintf(out,"Case #%d: OFF\n",it);
    }
    fclose(in);
    fclose(out);
    return 0;
}
//---------------------------------------------------------------------------
 