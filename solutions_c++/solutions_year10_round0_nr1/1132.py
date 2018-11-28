#include <fstream>
#include <iostream>

using namespace std;

int main()
{
    int noGames=0, N=0, K=0;
    ifstream fin("A-large.in");
    ofstream fout("A-large.out");

    fin >> noGames;

    for ( int i = 0; i < noGames; i++ )
    {
        fin >> N >> K;
        fout << "Case #" << i+1 << ": ";

        //cout << K << " " << N << " " <<((1<<N)-1) << " " << (K & ((1<<N)-1)) << endl;
        if ( (K & ((1<<N)-1)) == ((1<<N)-1)  )
        {
            fout << "ON" << endl;
        }
        else
        {
            fout << "OFF" << endl;
        }





    }
    return 0;
}
