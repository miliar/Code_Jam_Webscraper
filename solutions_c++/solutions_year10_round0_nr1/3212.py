#include <iostream>
#include <vector>
#include <map>
#include <list>
#include <fstream>
#include <algorithm>
#include <math.h>

using namespace std;
typedef unsigned long long ull;
typedef long long ll;

int main(int argc, char* argv[])
{
    int TCount = 0; //Test case count
    int caseCount = 0;
    if(argc == 3)
    {
        ifstream fin;
        ofstream fout;

        fin.open(argv[1]);
        fout.open(argv[2]);
        
        char *state[] = {"OFF", "ON"};
        fin >> TCount;
    
        for(caseCount = 0 ; caseCount < TCount; caseCount++)
        {
            int N = 0;
            ull k = 0;
            ull ans = 1;
            ull mask = 0;
            fin >> N >> k;

            mask = pow(2, N);
            ans = !((k+1) %(mask));
            fout << "Case #" << caseCount+1 << ": " << state[ans] << endl;
        }
        fin.close();
        fout.close();

    }
    return 0;
}
