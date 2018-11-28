//---------------------------------------------------------------------------

#include <clx.h>
#pragma hdrstop

#include <string>
#include <vector>
#include <queue>
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

#define PROB "C"
//#define SIZE "test"
#define SIZE "small"
//#define SIZE "large"
#define ATT "0"

//---------------------------------------------------------------------------
int euros(int R, int k, int N, queue<int> g)
{
int i,j,fill,ans=0;
VI went;
FOR(i,R)
{   went = VI(0);
    fill=0;
    while (g.size()>0 && fill+g.front()<=k)
    {   went.PB(g.front());
        fill+=g.front();
        g.pop();
    }
    ans+=fill;
    FOR(j,SZ(went))
        g.push(went[j]);
}
return ans;
}
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
    SFOR(it,1,T+1)
    {   //read input
        int i,R,k,N,t;
        fscanf(in, "%d %d %d\n", &R, &k, &N);
        queue<int> g;
        FOR(i,N)
        {   fscanf(in, "%d", &t);
            g.push(t);
        }
        //write output
        fprintf(out,"Case #%d: %d\n",it,euros(R,k,N,g));
    }
    fclose(in);
    fclose(out);
    return 0;
}
//---------------------------------------------------------------------------
 