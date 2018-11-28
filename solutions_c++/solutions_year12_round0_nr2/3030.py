#include <iostream>
#include <fstream>

using namespace std;

main()
{
    ifstream fin("B-large.in");
    ofstream fout("bl.txt");
    int k, n, s, m, a, b;
    fin >> k;
    for (int cnt = 1; cnt <= k; ++cnt)
    {
        int c = 0;
        fin >> n >> s >> m;
        for (int i = 0; i < n; ++i)
        {
            fin >> a;
            b = (a + 2) / 3;
            if (b >= m)
                ++c;
            else if (s > 0 && b == m - 1 && a % 3 != 1 && a <= 28 && a >= 2)
            {
                ++c;
                --s;
            }
        }
        fout << "Case #" << cnt << ": " << c << endl;
    }
    //while (1);
}
