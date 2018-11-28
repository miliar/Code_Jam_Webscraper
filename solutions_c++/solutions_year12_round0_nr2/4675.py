#include <iostream>
#include <fstream>

using namespace std;



int main()
{
    int T;
    ifstream fin("data.in");
    ofstream fout("data.out");
    fin >> T;
    for(int i=0; i<T; ++i)
    {
        int N, S, p;
        fin >> N >> S >> p;
        int r = 0, score;
        for(int j=0; j<N; ++j)
        {
            fin >> score;
            int mean = score / 3;
            int remain = score % 3;
            if(mean >= p)
                ++r;
            else if(remain != 0 && mean + 1 == p)
                ++r;
            else if(S > 0)
            {
                if(remain == 0 && mean > 0 && mean + 1 == p)
                {
                    --S; ++r;
                }
                else if(remain == 2 && mean + 2 == p)
                {
                    --S; ++r;
                }
            }
        }
        fout << "Case #" << (i+1) << ": " << r << endl;
    }
    return 0;
}
