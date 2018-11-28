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
#define SIZE "small"
//#define SIZE "large"
#define ATT "0"

string itos(long long q) {
	SS A;
	A << q;
	string s;
	A >> s;
	return s;
}

//---------------------------------------------------------------------------

bool isPrime(int n) {
	int i;
	for(i=2; i<=sqrt(n); i++)
		if (n%i==0)	return false;
	return true;
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
    {   //read input
        int A,B,P;
        fscanf(in,"%d %d %d\n",&A,&B,&P);
        //process
        int i,j,k;
        VI primes;
        SFOR(i,P,B+1)
            if (isPrime(i)) primes.PB(i);
        long long nm=0;
        set<set<int> > sets;
        set<int> divisors;
        set<set<int> >::iterator it1;
        set<int>::iterator it2;
        SFOR(i,A,B+1)
        {   //i = cur.num
            divisors=set<int>();
            FOR(j,SZ(primes))
                if (i%primes[j]==0)
                    divisors.insert(j);
            if (SZ(divisors)==0)   //a set of itself
            {   nm++;
                continue;
            }
            //at least one divisor
            if (sets.count(divisors)>0) //this set already seen
                continue;
            for (it1=sets.begin(); it1!=sets.end(); )
            {   //if there are common elements in devisors and it1
                bool merge=false;
                for (it2=(*it1).begin(); it2!=(*it1).end(); it2++)
                    if (divisors.count(*it2)>0)
                    {   merge=true;
                        break;
                    }
                if (!merge)
                {   it1++;
                    continue;
                }
                //merge (*it1) into divisors
                for (it2=(*it1).begin(); it2!=(*it1).end(); it2++)
                    divisors.insert(*it2);
                //and delete (*it1) from sets
                sets.erase(it1);
            }
            sets.insert(divisors);
        }
        nm+=SZ(sets);
        //write output
        fprintf(out,"Case #%d: %s\n",it,itos(nm).c_str());
    }
    fclose(in);
    fclose(out);
    return 0;
}
//---------------------------------------------------------------------------
