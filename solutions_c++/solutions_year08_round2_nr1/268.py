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

string itos(long long q) {
	SS A;
	A << q;
	string s;
	A >> s;
	return s;
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
        int i,j,k,n;
        int A,B,C,D,x0,y0,M;
        vector<long long> x,y;
        fscanf(in,"%d %d %d %d %d %d %d %d\n",&n,&A,&B,&C,&D,&x0,&y0,&M);
        //generate
        x.PB(x0);
        y.PB(y0);
        SFOR(i,1,n)
        {   x.PB((x[i-1]*A+B)%M);
            y.PB((y[i-1]*C+D)%M);
        }
        long long np[9];
        FOR(i,9)
            np[i]=0;
        FOR(i,n)
            np[(int)((x[i]%3)*3+y[i]%3)]++;
        long long ans=0;
        FOR(i,9)
            ans+=(np[i]*(np[i]-1)*(np[i]-2))/6;
        FOR(i,9)
        SFOR(j,i+1,9)
        SFOR(k,j+1,9)
            if (((i/3)+(j/3)+(k/3))%3==0 && ((i%3)+(j%3)+(k%3))%3==0)
                ans+=np[i]*np[j]*np[k];
        //write output
        fprintf(out,"Case #%d: %s\n",it,itos(ans).c_str());
    }
    fclose(in);
    fclose(out);
    return 0;
}
//---------------------------------------------------------------------------
 