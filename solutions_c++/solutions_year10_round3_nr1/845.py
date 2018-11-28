#include <cstdio>
#include <iostream>
#include <string>
#include <map>
#include <fstream>
#include <vector>

using namespace std;


int main()
{
    ifstream ifile;
    ofstream ofile;
    string tString, newDir;
    int T, N, M;

    ifile.open("in.txt");
    ofile.open("out.txt");

    ifile >> T;

    for(int t=1; t<=T; t++)
    {
        long long int ans = 0;
        map<string, bool> used;
        ifile >> N >> M;


        for(int i=0; i<N; i++)
        {
            ifile >> tString;
            newDir = tString[0];
            int k=1;
            while(k<tString.size())
            {
                if(tString[k] == '/' || k == tString.size()-1)
                {
                    if(!used[newDir])
                    {
                        used[newDir] = true;
                    }
                }
                newDir += tString[k];
                k++;
            }

        }

        for(int i=0; i<M; i++)
        {
            ifile >> tString;
            newDir = tString[0];
            int k=1;
            while(k<tString.size())
            {
                if(tString[k] == '/' || k == tString.size()-1)
                {
                    if(!used[newDir])
                    {
                        used[newDir] = true;
                        ans++;
                    }
                }
                newDir += tString[k];
                k++;
            }
        }

        ofile << "Case #" << t << ": " << ans << endl;
    }




    ifile.close();
    ofile.close();

    return 0;
}
