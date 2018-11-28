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

#define PROB "B"
//#define SIZE "test"
//#define SIZE "small"
#define SIZE "large"
#define ATT "1"

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
	int L,P,C;	//L < P
        fscanf(in,"%d %d %d\n",&L,&P,&C);
	double low1 = log(L)/log(C), high1 = log(P)/log(C);
	high1-=low1;
	int lim;
	if (high1-floor(high1)<1e-12)
	    lim=(int)floor(high1);
	else lim=(int)ceil(high1);
        //find lowest power of 2 which is greater than high1
	int h=1,p=0;
	while (h<lim)
	{   h*=2;
	    p++;
	}
	fprintf(out,"Case #%d: %d\n",it,p);
//	fprintf(out,"%f %f %f\n",low1,high1,high1-low1); 
    
    }
    fclose(in);
    fclose(out);
    return 0;
}
//---------------------------------------------------------------------------
 