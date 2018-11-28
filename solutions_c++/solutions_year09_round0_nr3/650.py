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

#define PROB "C"
//#define SIZE "test"
//#define SIZE "small"
#define SIZE "large"
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
    string et = "welcome to code jam";
    SFOR(it,1,N+1)
    {   //read input
        char c;
        string s;
        while(true)
        {   fscanf(in,"%c",&c);
            if (c=='\n') break;
            s+=c;
        }
        //process
        int dp[501][20];    //the number of times substr(et,j) appears in substr(s,i)
        int i,j;
        FOR(i,SZ(et)+1)
            dp[0][i] = 0;
        FOR(i,SZ(s)+1)
            dp[i][0] = 1;
        SFOR(i,1,SZ(s)+1)
        SFOR(j,1,SZ(et)+1)
        {   dp[i][j] = dp[i-1][j];
            if (et[j-1]==s[i-1])
                dp[i][j] = (dp[i][j]+dp[i-1][j-1])%10000;
        }
        //write output
        fprintf(out,"Case #%d: %04d\n",it,dp[SZ(s)][SZ(et)]);
    }
    fclose(in);
    fclose(out);
    return 0;
}
//---------------------------------------------------------------------------
