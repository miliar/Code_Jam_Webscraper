#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <climits>

using namespace std;


int main( int argc, char** argv )
{
    if ( argc != 2 )
    {
        cout << "Please input file name!" << endl;
        return 1;
    }

    ifstream input(argv[1], ios_base::in );

    if ( !input.is_open() )
    {
        cout << "Cannot open input file!" << endl;
        return 1;
    }

    int T, R, k, N; 
    vector<int> g;
    int tmp_g;

    int ii, jj;
    int begin, end, next;
    int cycle_R;
    int residue_R;
    int num_cycle;

    long long int cycle_money;
    long long int total_money;
    long long int residue_money;

    int tmp_money;
    int tmp_cap;

    input >> T;

    for ( ii = 0; ii < T; ++ii )
    {
        g.clear();

        input >> R >> k >> N;

        for ( jj = 0; jj < N; ++jj )
        {
            input >> tmp_g;
            g.push_back(tmp_g);
        }

        cycle_R = 0;
        begin = 0;
        end = 0;
        
        cycle_money = 0;

        for ( jj = 0; jj < R; ++jj )
        {
            cycle_R += 1;

            tmp_cap = 0;
            while ( true )
            {
                tmp_cap += g[end];
                cycle_money += g[end];

                next = (end+1) % N;
                if ( next == begin || (tmp_cap+g[next]) > k )
                    break;
                else
                    end = next;
            }

            begin = next;
            end = begin;

            if ( begin == 0 )
                break;
        }
        
        num_cycle = R/cycle_R;
        total_money = num_cycle*cycle_money;

        residue_R = R % cycle_R;

        begin = 0;
        end = 0;
        residue_money = 0;

        for ( jj = 0; jj < residue_R; ++jj )
        {
            tmp_cap = 0;
            while ( true )
            {
                tmp_cap += g[end];
                residue_money += g[end];

                next = (end+1) % N;
                if ( next == begin || (tmp_cap+g[next]) > k )
                    break;
                else
                    end = next;
            }

            begin = next;
            end = begin;
        }

        total_money += residue_money;
        
        cout << "Case #" << ii+1 << ": " << total_money << endl;
    }   

    input.close();
    return 0;
}
