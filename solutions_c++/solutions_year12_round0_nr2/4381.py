#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <stdlib.h>
#include <math.h>

using namespace std;

int main(int, char**)
{
    fstream in;
    fstream out;

    in.open("B-large.in", ios_base::in);
    out.open("B-large.out", ios_base::out);

    string line;

    getline(in, line);

    int T = atoi(line.c_str());

    for (int i=0; i < T; i++)
    {
        string word;
        int start = 0;
        int stop = 0;
        int N, S, p;
        int total, lavg, rem;
        int match = 0;

        out << "Case #" << i+1 << ": ";

        getline(in, line);

        stop = line.find(' ', start);
        word = line.substr(start, stop);
        N = atoi(word.c_str());

        start = stop+1;
        stop = line.find(' ', start);
        word = line.substr(start, stop);
        S = atoi(word.c_str());

        start = stop+1;
        stop = line.find(' ', start);
        word = line.substr(start, stop);
        p = atoi(word.c_str());

        for (int j=0; j < N; j++)
        {
            start = stop+1;
            stop = line.find(' ', start);
            word = line.substr(start, stop);
            total = atoi(word.c_str());

            if(total == 0 && p == 0) match++;
            else if(total>0)
            {
                rem = (p*3) - total;

                if(rem <= 0)
                {
                    match++;
                }

                else if(rem <= 4 && rem > 2 && S > 0)
                {
                    match++;
                    S--;
                }

                else if(rem <= 2)
                {
                    match++;
                }
            }
        }

        out << match << endl;
    }

    in.close();
    out.close();

    return 0;
}

