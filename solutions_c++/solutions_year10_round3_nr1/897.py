#include <iostream>
#include <vector>
#include <map>
#include <list>
#include <fstream>
#include <algorithm>
typedef long long ll;
using namespace std;

struct wire
{
    ll A;
    ll B;
};

bool compare(struct wire first, struct wire second)
{
    return first.A < second.A;
}

int main(int argc, char* argv[])
{
    int TCount = 0; //Test case count
    int caseCount = 0;
    if(argc == 3)
    {
        ll N = 0;
        ifstream fin;
        ofstream fout;

        fin.open(argv[1]);
        fout.open(argv[2]);

        fin >> TCount;
    
        for(caseCount = 0 ; caseCount < TCount; caseCount++)
        {
            struct wire conn[1000];
            ll intersection = 0;
            fin >> N;

            for(ll i = 0; i < N; i++)
            {
                fin >> conn[i].A >> conn[i].B;
            }
            
            sort(conn, conn + N, compare);

            for(ll ii = 0; ii < N -1 ; ii++)
            {
                for(ll jj = ii; jj < N; jj++)
                {
                    if(conn[ii].B > conn[jj].B)
                    {
                        intersection++;
                    }
                }
            }
            fout << "Case #" << caseCount+1 << ": " << intersection << endl;
        }
        fin.close();
        fout.close();

    }
    else
    {
        cout << "Pass the test case file and output file" << endl;
    }
    return 0;
}
