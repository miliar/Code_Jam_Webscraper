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
            map<string, int> existingDirectory;
            
            int mkDirCount = 0;
            int N = 0, M = 0;

            fin >> N >> M;


            for(int i = 0; i < N; i++)
            {
                string dir;

                fin >> dir;
                existingDirectory[dir] = 1;
            }

            for(int j =0; j < M; j++)
            {
                string dir;
                fin >> dir;

                size_t pos = dir.find("/", 1);
            
                while(pos != string::npos)
                {
                    string subString = dir.substr(0, pos);

                    if(existingDirectory[subString] != 1)
                    {
                        mkDirCount++;
                        existingDirectory[subString] = 1;
                    }

                    pos = dir.find("/", pos+1);
                    
                }

                if(existingDirectory[dir] != 1)
                {
                    mkDirCount++;
                    existingDirectory[dir] = 1;
                }
            }
            
            fout << "Case #" << caseCount+1 << ": " << mkDirCount << endl;
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
