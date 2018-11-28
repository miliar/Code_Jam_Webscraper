#include <iostream>
#include <vector>
#include <map>
#include <list>
#include <fstream>
#include <algorithm>

using namespace std;

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

        fin >> TCount;
    
        for(caseCount = 0 ; caseCount < TCount; caseCount++)
        {
            unsigned long long group[1000];

            long long R = 0, k = 0, N = 0;
            long long gSize = 0;
            long long i = 0;
            unsigned long long earning = 0;

            fin >> R >> k >> N;

            for(;i < N; i++)
            {
                fin >> group[i];
            }

            long long tripCount = 0;
            long long currentGrp = 0;
            unsigned long long tripEarning = 0;
            long long tripGrpCount = 0;
            long long tmp = 0;
            for(;tripCount < R; tripCount++)
            {
                tripEarning = 0;
                tripGrpCount = 0;
                tmp = 0 ;
                while(((tmp = tripEarning + group[currentGrp]) <= k) && 
                       (tripGrpCount < N) )
                {
                    tripEarning = tmp;
                    currentGrp = currentGrp == (N - 1) ? 0 : currentGrp + 1;
                    tripGrpCount++;
                }

                earning += tripEarning;
            }
            
            fout << "Case #" << caseCount+1 << ": " << earning << endl;
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
