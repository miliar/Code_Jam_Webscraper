#include<fstream>
#include<iostream>
#include<vector>
#include<iomanip>
#include<math.h>

using namespace std;

ifstream in("C-small-attempt0.in");
ofstream out("output.txt");

int T;

int main()
{
    in >> T;
    for(int test = 0; test < T; test++)
    {
        int N;
        long long L, H;
        in >> N >> L >> H;
        vector<long long> players(N);
        for(int i = 0; i < N; i++)
            in >> players[i];

        long long answer = 0;
        for(long long c = L; c <= H; c++)
        {
            bool good = true;
            for(int i = 0; i < N; i++)
                if(players[i] % c > 0 && c % players[i] > 0)
                {
                    good = false;
                    break;
                }
            if(good)
            {
                answer = c;
                break;
            }
        }
        out << "Case #" << (test + 1) << ": ";
        if(answer > 0)
            out << answer << endl;
        else
            out << "NO" << endl;
    }
    return 0;
}
