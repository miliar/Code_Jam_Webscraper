#include <cstdio>
#include <iostream>
#include <iomanip>
#include <fstream>
using namespace std;

#define ll long long
int main()
{
    int casos;
    ifstream ifs("A-large.in", ifstream::in );
    ofstream ofs("A-large.out");
    ifs >> casos;
    for( int i = 0 ; i < casos; i ++ )
    {
        ll N, K;
        ifs >> N >> K;
        cout << K % (1LL<<N) << " " << (1LL<<N) << endl;
        if( K % (1LL<<(N)) == ((1LL<<(N))-1) )
        {
            ofs << "Case #" << (i+1) << ": ON\n";
        }else ofs << "Case #" << (i+1) << ": OFF\n";
    }
    return 0;
}

