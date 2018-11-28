#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
    int n, s, q, i, j, k, c, swaps;
    string as[100], qs;
    char tmp[255], ch;
    bool af[100], f;
    ifstream fin;
    ofstream fout;
    fin.open("in.txt");
    if (fin.fail())
        exit(1);
    fout.open("out.txt");

    fin >> n;

    for (int t = 1; t <= n; ++t)
    {
        fin >> s;

        fin.get(ch);
        while (ch != '\n')
            fin.get(ch);

        for (i = 0; i < s; ++i)
        {
            fin.getline(tmp, 256);
            as[i].assign(tmp);
            af[i] = false;
        }

        swaps = 0;
        c = s;
        fin >> q;
        fin.get(ch);
        while (ch != '\n')
            fin.get(ch);

        for (i = 0; i < q; ++i)
        {
            f = false;
            fin.getline(tmp, 256);
            qs.assign(tmp);
            for (j = 0; !f && (j < s); ++j)
            {
                if (!af[j] && (qs == as[j]))
                {
                    if (c == 1)
                    {
                        for (k = 0; k < s; ++k)
                            af[k] = false;
                        c = s;
                        ++swaps;
                    }
                    af[j] = true;
                    --c;
                    f = true;
                }
            }
        }

        fout << "Case #" << t << ": " << swaps << endl;
    }

    return 0;
}
