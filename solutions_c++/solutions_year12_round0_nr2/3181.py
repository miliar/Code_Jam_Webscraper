#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream in("googlers.in");
    int T;
    in >> T;
    ofstream out("googlers.out");
    for(int i = 0; i < T; ++i)
    {
        int N, S, p;
        in >> N >> S >> p;
        int count = 0;

        int min = (p + 2*(p-1) > 0 ? p + 2*(p-1) : 0);
        int min_s = (p + 2*(p - 2) > 0 ? p + 2*(p - 2) : min);
        for(int j = 0, score; j < N; ++j)
        {
            in >> score;
            if(score >= min)
                ++count;
            else if(score >= min_s && S)
            {
                ++count;
                --S;
            }
        }
        out << "Case #" << i + 1 << ": " << count << "\n";
    }
    in.close();

    return 0;
}
