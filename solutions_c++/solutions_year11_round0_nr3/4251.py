#include <fstream>
#include <iostream>

using namespace std;

int main()
{
    ifstream in("C.in");
    ofstream out("C.out");

    int T;
    in >> T;

    int N, C, xsum, sum, min;
    for (int test = 1;test <= T;test++)
    {
        in >> N;
        sum = xsum = min = 0;

        out << "Case #" << test << ": ";

        for (int i = 0;i < N;i++)
        {
            in >> C;
            xsum ^= C;
            sum += C;
            if (min == 0 || C < min) min = C;
        }
        if (xsum != 0) out << "NO" << endl;
        else out << (sum - min) << endl;
    }

    return 0;
}