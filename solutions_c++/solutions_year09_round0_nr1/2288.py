#include <iostream>
#include <vector>
#include <map>
#include <list>
#include <fstream>
#include <algorithm>
#include <iostream>

using namespace std;

int L = 0, D = 0;

char words[5000][15];
char matches[5000];
string inputString;
int main(int argc, char* argv[])
{
    int TCount = 0; //Test case count
    if(argc == 3)
    {
        ifstream fin;
        ofstream fout;
        int i = 0;
        fin.open(argv[1]);
        fout.open(argv[2]);

        fin >> L >> D >> TCount;
    

        for(i = 0; i < D; i++)
        {
            string nw;
            fin >> words[i];
            cout << words[i] << endl;
        }
        
        for(i = 0 ; i < TCount; i++)
        {
            long long count = 0;
            
            fin >> inputString;
            
            int j = 0;
            int alphaPos = 0;

            for(j = 0; j < D; j++)
            {
                matches[j] = 0;
            }
            
            j = 0;
            int insideP = 0;
            for(;alphaPos < L; alphaPos++)
            {
                insideP = 0;
                for(; j < inputString.length(); j++)
                {
                    if(inputString[j] == '(')
                    {
                        insideP = 1;
                        continue;
                    }
                    else if(inputString[j] == ')')
                    {
                        j++;
                        break;
                    }
                    else
                    {
                        for(int k = 0; k < D; k++)
                        {
                            if(inputString[j] == words[k][alphaPos])
                            {
                                 matches[k]++;
                            }
                        }

                        if(insideP == 0)
                        {
                            j++;
                            break;
                        }
                    }
                }
            }
            
            for(j = 0 ;j < D; j++)
            {
                //cout << "matches[" << j << "]: " << matches[j] << endl;
                if(matches[j] == L)
                {
                    count ++;
                }
            }
            
            //cout << endl;
            fout << "Case #" << i+1 << ": " << count << endl;
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
