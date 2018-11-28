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
#define LL __int64

#define PROB "A"
//#define SIZE "test"
//#define SIZE "small"
#define SIZE "large"
#define ATT "0"

//---------------------------------------------------------------------------
string itos(LL q) {
	SS A;
	A << q;
	string s;
	A >> s;
	return s;
}

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
    {   //read input string
        char a[100];
        string s;
        fscanf(in,"%s\n",a);
        s = string(a);
        //process
        //get distinct characters, map them to "digits" (first one is 1, next 0, than 2, 3, ...)
        //and calc the sum
        map<char, int> digits;
        digits[s[0]]=1;
        int i;
        for(i=1; i<s.size(); i++)
        {   if (digits.find(s[i])!=digits.end())    //digit already mapped
                continue;
            if (digits.size()==1)   //next digit = 0
                digits[s[i]]=0;
            else
                digits[s[i]]=digits.size();
        }
        LL n=0,base=(digits.size()==1?2:digits.size()),mult=1;
        for(i=s.size()-1; i>=0; i--)
        {   n+=mult*digits[s[i]];
            mult*=base;
        }
        //write output
        fprintf(out,"Case #%d: %s\n",it,itos(n).c_str());
    }
    fclose(in);
    fclose(out);
    return 0;
}
//---------------------------------------------------------------------------
 