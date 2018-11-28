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
//#define SIZE "small"
#define SIZE "large"
#define ATT "0"

long long stoi(string q) {
	SS A;
	A << q;
	long long s;
	A >> s;
	return s;
}
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
        char nc[22];
        fscanf(in,"%s\n",&nc);
        string ns = string(nc);
        long long n = stoi(ns);
        //process
        //try yet another approach
        //if they are not, take next permutation
        string ms = ns;
        sort(ms.begin(),ms.end());
        reverse(ms.begin(),ms.end());
        if (ms==ns)
        {   //if digits are sorted, sort them vice versa and add 0 after first digit (first must be non-zero)
            ms = "00";
            int i=ns.size()-1;
            while (ns[i]=='0')
                i--;
            ms[0] = ns[i];
            ns = ns.substr(0,i)+ns.substr(i+1);
            for (i=ns.size()-1; i>=0; i--)
                ms = ms+ns[i];
        }
        else
        {   ms=ns;
            next_permutation(ms.begin(),ms.end());
        }

        //write output
        fprintf(out,"Case #%d: %s\n",it,ms.c_str());
    }
    fclose(in);
    fclose(out);
    return 0;
}
//---------------------------------------------------------------------------
