#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int K = 1; K <= T; ++K)
    {
        int r, c, d;
        cin >> r >> c >> d;
        vector<vector<long long> > m(r + 1, vector<long long>(c + 1));
        // d = 1;

        for (int i = 1; i <= r; ++i)
        {
            string s;
            cin >> s;
            for (int j = 1; j <= c; ++j)
            {
                m[i][j] = d + s[j - 1] - '0';
            }
        }

        vector<vector<long long> > sm(r + 1, vector<long long>(c + 1));
        vector<vector<long long> > smi(r + 1, vector<long long>(c + 1));
        vector<vector<long long> > smj(r + 1, vector<long long>(c + 1));

        for (int i = 1; i <= r; ++i)
        {
            long long sm1 = 0;
            long long smi1 = 0;
            long long smj1 = 0;
            for (int j = 1; j <= c; ++j)
            {
                sm1 += m[i][j];
                smi1 += m[i][j] * i;
                smj1 += m[i][j] * j;

                sm[i][j] = sm[i-1][j] + sm1;
                smi[i][j] = smi[i-1][j] + smi1;
                smj[i][j] = smj[i-1][j] + smj1;
                // cerr << sm[i][j] << " ";
            }
            // cerr << "\n";
        }


        int ansk = -1;

        for (int i = 0; i < r; ++i)
        {
            for (int j = 0; j < c; ++j)
            {
                int maxk = min(r - i, c - j);

                for (int k = maxk; k >= 3; --k)
                {
                    long long si1 = 2 * (smi[i + k][j + k] + smi[i][j] - smi[i][j + k] - smi[i + k][j]
                            - m[i + 1][j + 1] * (i + 1) - m[i + k][j + 1] * (i + k)
                            - m[i + 1][j + k] * (i + 1) - m[i + k][j + k] * (i + k));

                    long long sj1 = 2 * (smj[i + k][j + k] + smj[i][j] - smj[i][j + k] - smj[i + k][j]
                            - m[i + 1][j + 1] * (j + 1) - m[i + k][j + 1] * (j + 1) 
                            - m[i + 1][j + k] * (j + k) - m[i + k][j + k] * (j + k));

                    long long sm1 = sm[i + k][j + k] + sm[i][j] - sm[i][j + k] - sm[i + k][j]
                            - m[i + 1][j + 1] - m[i + k][j + 1]
                            - m[i + 1][j + k] - m[i + k][j + k];

                    /*
                    if ((i == 2) && (j == 3) && (k == 5))
                    {
                        cerr << "here:\n";
                        cerr << si1 << " " << sj1 << " " << sm1 << "\n";
                        cerr << (static_cast<double>(si1)/sm1) << "\n";
                        cerr << (static_cast<double>(sj1)/sm1) << "\n";
                    }
                    */

                    if ((si1 % sm1 == 0) &&
                        (si1 / sm1 == 2 * i + k + 1) &&
                        (sj1 % sm1 == 0) &&
                        (sj1 / sm1 == 2 * j + k + 1))
                    {
                        if (k > ansk)
                        {
                            ansk = k;

                            /*
                            cerr << i << " " << j << " " << k << ":\n";
                            cerr << si1 << " " << sj1 << " " << sm1 << "\n";
                            cerr << (static_cast<double>(si1)/sm1) << "\n";
                            cerr << (static_cast<double>(sj1)/sm1) << "\n";
                            */
                            break;
                        }
                    }

                }
            }
        }

        cout << "Case #" << K << ": ";
        if (ansk > 0) 
        {
            cout << ansk;
        }
        else 
        {
            cout << "IMPOSSIBLE";
        }
        cout << "\n";

    }
}
