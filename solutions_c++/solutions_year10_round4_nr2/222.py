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

int P;
VI M;
vector<VI > prices;

//---------------------------------------------------------------------------

#pragma argsused
int main(int argc, char* argv[])
{
    FILE *in, *out;
    int N,it;
    VI pw(20);
    pw[0]=1;
    SFOR(it,1,19)
        pw[it]=pw[it-1]*2;

    string name=PROB+string("-")+SIZE;
    if (string(SIZE)==string("small"))
        name+=string("-attempt")+ATT;
    in = fopen((name+".in").c_str(),"rt");
    out = fopen((name+".out").c_str(),"wt");
    fscanf(in,"%d\n",&N);
    SFOR(it,1,N+1)
    {   //read input
//    cout << endl << "----------------------" << it << endl;
        int i,j,k,t;
        fscanf(in,"%d\n",&P);
        M=VI(pw[P]);
        FOR(i,pw[P])
            fscanf(in,"%d ",&(M[i]));
        FOR(i,pw[P])
            M[i]=P-M[i];
//        prices = vector<VI >(P);
        FOR(i,P)
        FOR(j,pw[P-i-1])
        {   fscanf(in,"%d",&t);
//            prices[j].PB(t);
        }
        //process
        //greedy: if all teams between k and l have one more match to be unmissed, buy this ticket
        bool need;
        int total=0;
        for(i=P-1;i>=0;i--)
        {   //i is index of level
            for (j=0; j<pw[P-i-1]; j++)
            {   //j is index of the ticket to be decided
//                cout << "i = " << i << " j = " << j << endl;
                //check all teams which are within this group
                need=false;
/*                for (k=j*pw[i+1]; k<(j+1)*pw[i+1]; k++)
                    cout << k << " ";
                cout << endl;*/
                for (k=j*pw[i+1]; k<(j+1)*pw[i+1]; k++)
                    if (M[k]>0)
                    {   need=true;
                        break;
                    }
                if (need)
                {   total++;
                    cout << "need at " << i << " " << j << endl;
                    for (k=j*pw[i+1]; k<(j+1)*pw[i+1]; k++)
                        if (M[k]>0)
                            M[k]--;
                }
            }
        }

        //write output
        fprintf(out,"Case #%d: %d\n",it,total);
    }
    fclose(in);
    fclose(out);
    return 0;
}
//---------------------------------------------------------------------------
 