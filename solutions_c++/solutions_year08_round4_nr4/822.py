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
#define ATT "1"

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
        int k,i,j,ng,ngmin;
        string S;
        char c[1002];
        fscanf(in,"%d\n",&k);
        fscanf(in,"%s\n",c);
        S = string(c);
        //process
        //try all permutations of 0..k-1
        VI p;
        FOR(i,k)
            p.PB(i);
        ngmin=SZ(S);
        //non-permuted
            //encode
            string res(SZ(S)+1,'.');
            FOR(i,SZ(S))
            {   j=i/k;
                res[i]=S[j*k+p[i%k]];
            }
            //count number of groups in RES
            ng=0;
            i=0;    //start of next group
            while (i!=SZ(S))
            {   j=i;
                while (res[j]==res[i]) j++;
                ng++;
                i=j;
            }
            ngmin=min<int>(ng,ngmin);

        while (next_permutation(p.begin(),p.end()))
        {   //encode
            string res(SZ(S)+1,'.');
            FOR(i,SZ(S))
            {   j=i/k;
                res[i]=S[j*k+p[i%k]];
            }
            //count number of groups in RES
            ng=0;
            i=0;    //start of next group
            while (i!=SZ(S))
            {   j=i;
                while (res[j]==res[i]) j++;
                ng++;
                i=j;
            }
            ngmin=min<int>(ng,ngmin);
        }
        //write output
        fprintf(out,"Case #%d: %d\n",it,ngmin);
    }
    fclose(in);
    fclose(out);
    return 0;
}
//---------------------------------------------------------------------------
 