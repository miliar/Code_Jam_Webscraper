#include <fstream>
#include <iostream>
#include <utility>
#include <string>
#include <map>

using namespace std;

int prices[10][1024];
int matchs[10];
bool buy[10][1024];

int main( int argc, char** argv )
{
    ifstream input(argv[1], ios_base::in);

    int T, P;
    int ii, jj, kk;
    int n_team;
    int tmp;
    int pos;
    long long total;

    multimap<int, int> constraint;
    
    input >> T;

    for ( ii = 0; ii < T; ++ii )
    {
        input >> P;

        for ( jj = 0; jj < P; jj++ )
            matchs[jj] = 1 << (P-1-jj);

        for ( jj = 0; jj < 10; ++jj )
            for ( kk = 0; kk < 1024; ++kk )
            {
                buy[jj][kk] = false;
            }

        n_team = 1 << P; 
        
        constraint.clear();
        for ( jj = 0; jj < n_team; ++jj )
        {
            input >> tmp;
            constraint.insert(make_pair(tmp, jj));
        }

        for ( jj = 0; jj < P; ++jj )
        {
            for ( kk = 0; kk < matchs[jj]; ++kk )
                input >> prices[jj][kk];
        }
        
        for ( multimap<int,int>::iterator it = constraint.begin(), e = constraint.end(); it != e; ++it )
        {
            tmp = it->first;
            jj = it->second;

            // pos = jj/2;
            // for ( kk = 0; kk < P; ++kk )
            // {
            //     if ( buy[kk][pos] )
            //         --tmp;
            //     pos /= 2;                
            // }
            
            // pos = jj/2;
            // for ( kk = 0; kk < P && tmp > 0; ++kk )
            // {
            //     if ( buy[kk][pos] == false )
            //     {
            //         buy[kk][pos] = true;
            //         --tmp;
            //     }
            //     pos /= 2;                
            // }

            pos = jj/2;
            for ( kk = 0; kk < P; ++kk )
            {
                if ( kk >= tmp )
                    buy[kk][pos] = true;
                pos /= 2;
            }

            
        }

        // for ( jj = 1; jj < P; ++jj )
        // {
        //     for ( kk = 0; kk < matchs[jj]; ++kk )
        //     {
        //         if ( !buy[jj][kk] )
        //         {
        //             if ( buy[jj-1][2*kk] && buy[jj-1][2*kk+1] )
        //             {
        //                 if ( prices[jj][kk] < prices[jj-1][2*kk] + prices[jj-1][2*kk+1] )
        //                 {
        //                     buy[jj][kk] = true;
        //                     buy[jj-1][2*kk] = false;
        //                     buy[jj-1][2*kk+1] = false;
        //                 }
        //             }
        //         }
        //     }
        // }

        total = 0;

        for ( jj = 0; jj < P; ++jj )
            for ( kk = 0; kk < matchs[jj]; ++kk )
                if ( buy[jj][kk] )
                    total += prices[jj][kk];

        cout << "Case #" << ii+1 << ": " << total << endl;

    }
    

    input.close();
    return 0;
}
