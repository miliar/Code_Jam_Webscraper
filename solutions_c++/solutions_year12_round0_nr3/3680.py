#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <iterator>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <utility>

using namespace std;

int main(int argc, char **argv) {

    int cases;

    string hdr;
    getline(cin,hdr);
    stringstream ss(hdr);
    ss >> cases;

    for ( int i = 0; i < cases; ++i)
    {
        int A,B;
        string tmp;
        getline(cin,tmp);
        stringstream line(tmp);
        line >> A;
        line >> B;
        // print case hdr
        cout << "Case #" << i+1 << ": ";
        if ( B < 10 )
        {
            cout << "0" << endl;
            continue;
        }

        // generate all recyled mutations for the given range
        stringstream ctmp;
        vector< pair < int,int > > hits;
        for (int n = A; n <= B; ++n)
        {
            stringstream k_ss;
            k_ss << n;
            for ( int j = 1; j < k_ss.str().size(); ++j )
            {
                int ml,mr,m;
                mr = n / (int)pow(10,j);
                ml = n - ( mr * (int)pow(10,j) );
                m = mr + (int)( ml * (int)pow(10, k_ss.str().size()-j) );
                //cerr << "n: " << n << "\tm: " << m << "\tmr: " << mr << "\tml: " << ml << endl;
                if (n < m && m <= B)
                    hits.push_back(pair<int,int>(m,n));
            }
        }
        // sort the hit vector
        sort(hits.begin(),hits.end());
        vector< pair < int,int > >::iterator it = unique(hits.begin(),hits.end());
        hits.resize(it - hits.begin() );
        //cerr << endl;
        // return the vector size, our result
        cout << hits.size() << endl;
    }

    return 0;
}
