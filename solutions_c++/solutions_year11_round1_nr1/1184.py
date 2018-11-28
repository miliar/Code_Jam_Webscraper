// Large1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


#include <fstream>
#include<iostream>
#include <string>
#include <vector>

#define dout if(0) cout

using namespace std;

typedef long long LL;
_int64 max_n = 1000000000000000;

string GetAns(long long N, int Pd, int Pg)
{
    if (Pg == 0 && Pd > 0) return "Broken";
    if (Pg == 0 && Pd == 0) return "Possible";
	if (Pg == 100 && Pd < 100) return "Broken";

    for(long long d=1; d <=N; ++d)
    {
        bool d_poss=false;
        bool g_poss=false;

        if(d*Pd %100 == 0)
        {
            d_poss = true;    
        }
       
        if(d_poss)
        {
            long long total_lost = (long long)max_n * (100-Pg);
			dout << "d=" << d << " " << total_lost << endl; 
            long long today_lost = d-((d*Pd)/100);
    
            if(total_lost >= today_lost)
                g_poss =true;
        
        }
        
        if(d_poss && g_poss)
            return "Possible";
    }

    return "Broken";

}




int _tmain(int argc, _TCHAR* argv[])
{
	ifstream infile;
    infile.open ( "large1.in" , std::ofstream::in );
	ofstream outfile;
    outfile.open("large1.out", ofstream::out);

    dout << "sizeof " << sizeof(long long) << " " << max_n << endl;
    int T;
    infile >>T;
    dout << T << endl;
    for(int t=1; t<=T; ++t)
    {
        long long N;
        int Pd, Pg;
        infile >> N >> Pd >> Pg;
        outfile << "Case #" << t << ": " << GetAns(N, Pd, Pg) << endl;

    }

	cout << "ENDED";
	cin >> T;
return 0;
}
