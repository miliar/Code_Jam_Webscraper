#include <iostream>
#include <fstream>
#include <queue>

using namespace std;

int main()
{
    long long T, R, k, N, temp, filling, euros;
    bool filled;
    queue< long long > Q, Q2;


    ifstream fin("C-small-attempt0.in");
    ofstream fout("C-small-attempt0.out");

    fin >> T;

    for ( int i = 0; i < T; i++ )
    {
        fin >> R >> k >> N;

        while (!Q.empty())
            Q.pop();

        euros = 0;

        for ( int j = 0; j < N; j++ )
        {
            fin >> temp;
            Q.push( temp );
            //cout << "temp: " << temp << endl;
        }

        for ( int j = 0; j < R; j++ )
        {
            filled = false;
            filling = 0;

            while (!filled)
            {
                if (Q.empty())
                    break;

                if ( Q.front() <= k - filling )
                {
                    temp = Q.front();
                    Q.pop();
                    filling += temp;
                    Q2.push(temp);
                }
                else
                    filled = true;
            }
            while(!Q2.empty())
            {
                Q.push(Q2.front());
                Q2.pop();
            }

            euros += filling;
        }

        fout << "Case #" << i+1 << ": " << euros << endl;
    }




    return 0;
}
