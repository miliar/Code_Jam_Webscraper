
#include <fstream>

using namespace std;

int main()
{
    ifstream in("A.in");
    ofstream out("A.out");

    int T, N, PD, PG;
    in >> T;

    for (int Case = 1; Case <= T; Case++)
    {
        in >> N >> PD >> PG;
        if (N > 100) N = 100;
        out << "Case #" << Case << ": ";

        if ((PG == 100 && PD < 100) || (PG == 0 && PD > 0))
        {
            out << "Broken" << endl;
            continue;
        }

        for (int i = 0;i < N;i++)
        {
            if ((i*PD) % 100 == 0)
            {
                out << "Possible" << endl;
                break;
            }
            if (i == N-1) out << "Broken" << endl;
        }
    }

    return 0;
}