#include <iostream>
#include <fstream>
#include <ctime>

using namespace std;
typedef long long ll;

ifstream fin ("blah.in");
ofstream fout ("blah.txt");

int main()
{
    srand (time (NULL));
    int ntest; fin >> ntest;
    for (int test = 0; test < ntest; test++)
    {
        int n;
        int peak[12];
        fin >> n;
        for (int i = 0; i < n - 1; i++)
        {
            fin >> peak[i];
            peak[i]--;
        }
        bool check = true;
        for (int i = 0; i < n - 1; i++)
            for (int j = i + 1; j < n - 1; j++)
                if (peak[i] > j && peak[j] > peak[i])
                    check = false;
        fout << "Case #" << test + 1 << ": ";
        if (!check)
        {
            fout << "Impossible\n";
            continue;
        }
        while (true)
        {
            ll val[12];
            for (int i = 0; i < n; i++)
                val[i] = (10007 * rand()) % (1000000001LL);
            bool check = true;
            for (int i = 0; i < n - 1; i++)
            {
                int loc = i + 1;
                for (int j = i + 2; j < n; j++)
                {
                    if ((val[j] - val[i]) * (loc - i) > (val[loc] - val[i]) * (j - i))
                        loc = j;
                }
                if (loc != peak[i])
                {
                    check = false;
                    break;
                }
            }
            if (check)
            {
                for (int i = 0; i < n; i++)
                {
                    fout << val[i];
                    if (i < n - 1)
                        fout << " ";
                }
                fout << "\n";
                break;
            }
        }
    }
    //system ("Pause");
    return 0;
}
