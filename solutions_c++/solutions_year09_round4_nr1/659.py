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
#include <conio.h>
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
int calc(int N, VS p)
{
//for each line, calc index of last 1 in it
int i,j,k;
VI ind(N);
FOR(i,N)
    for(j=N-1;j>=0;j--)
        if (p[i][j]=='1')
        {   ind[i]=j;
            break;
        }
//"sort": for each line i, put into it the first element for which ind[i]<=i
int ans=0;
FOR(i,N-1)
{   for(j=i; j<N && ind[j]>i; j++);
    ans+=(j-i);
    for(k=j-1; k>=i; k--)
        swap(ind[k],ind[k+1]);
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
        int i,N;
        VS p;
        char t[50];
        fscanf(in,"%d\n",&N);
        FOR(i,N)
        {   fscanf(in,"%s\n",t);
            p.push_back(string(t));
        }
        //write output
        fprintf(out,"Case #%d: %d\n",it,calc(N,p));
    }
    fclose(in);
    fclose(out);
    return 0;
}
//---------------------------------------------------------------------------
