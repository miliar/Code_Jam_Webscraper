#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <fstream>

using namespace std;


int main()
{
    long long int N, T, R, k, t, Rev, run;
    ifstream ifile;
    ofstream ofile;
    queue<long long int> line1, line2;


    ifile.open("in.txt");
    ofile.open("out.txt");

    ifile >> T;

    for(int i=1; i<=T; i++)
    {
        Rev = 0;

        ifile >> R >> k >> N;

        for(int j=0; j<N; j++)
        {
            ifile >> t;
            line1.push(t);
        }

        for(int j=0; j<R; j++)
        {
            run = 0;

            //finds the current load from groups
            while(run + line1.front() <= k)
            {
                line2.push(line1.front());
                run += line1.front();
                line1.pop();

                if(line1.empty())
                    break;
            }


            Rev += run;

            while(!line2.empty())
            {
                line1.push(line2.front());
                line2.pop();
            }
        }

        while(!line1.empty())
            line1.pop();

        ofile << "Case #" << i << ": " << Rev << endl;
    }




    ifile.close();
    ofile.close();


    return 0;
}
