#include <cstdio>
#include <iostream>
#include <iomanip>
#include <fstream>
using namespace std;

#define ll long long
int main()
{
    int casos;
    ifstream ifs("C-large.in", ifstream::in );
    ofstream ofs("C-large.out");
    ifs >> casos;
    ll R , K, N, res;
    int mark[1111];
    int sig[1111];
    ll last[1111];
    ll paso[1111];
    ll values[1111];
    for( int i = 0 ; i < casos; i ++ )
    {
        ifs >> R >> K >> N; res = 0 ;
        for( int j = 0 ; j < N ; j ++ ) ifs >> values[j];
         for( int j = 0 ; j < N ; j ++ )
         {
            sig[j] = (j+1)%N;
            mark[j] =  last[j] = paso[j] = 0;
         }

        int index = 0;
        int first = 1;
        cout << " NEW GAME: \n\n\n";
        for( int vuelta = 0 ; vuelta < R ; vuelta ++  )
        {
            if( mark[index] == 3 && first)
            {
                first = 0 ;
                res = res + ( res - last[index] ) * ( ( R-vuelta ) / (vuelta-paso[index]) ) ;
                vuelta = vuelta + ( ( R-vuelta ) / (vuelta-paso[index]) ) * (vuelta-paso[index]);
                //cout << "HOLANDA\n";
            }
            paso[index] = vuelta;
            mark[index]++;
            last[index] = res;
            if( vuelta >= R ) break;
            // And now we look for the next one.

            int beg = index;
            ll tot = values[index];
            //cout << " new race : \n";
            //cout << tot << endl;
            while(sig[beg] != index && tot + values[sig[beg]] <= K )
            {
                beg = sig[beg];
                tot += values[beg];
              //  cout << values[beg] << endl;
            }
            res += tot;
            index = sig[beg];
        }
        ofs << "Case #" << (i+1) << ": " << res << endl;

    }
    return 0;
}

