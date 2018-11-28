//---------------------------------------------------------------------------

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
        int N,i,j,t1,t2,ans=0;
	VI l,r;
        fscanf(in,"%d\n",&N);
	FOR(i,N)
	{   fscanf(in,"%d %d\n",&t1,&t2);
	    l.PB(t1);
	    r.PB(t2);
	}
	FOR(i,N)
	SFOR(j,i+1,N)
	    if ((l[i]>l[j] && r[i]<r[j]) || (l[i]<l[j] && r[i]>r[j]))
	        ans++;
	fprintf(out,"Case #%d: %d\n",it,ans);
    }
    fclose(in);
    fclose(out);
    return 0;
}
//---------------------------------------------------------------------------
 