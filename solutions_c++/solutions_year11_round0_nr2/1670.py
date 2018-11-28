#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
    ifstream infile("B-large.in");
    ofstream outfile("b_large.txt");

    // 1 QRI 0 4 RRQR
    int t, c, d, n;

    string sc[36], sd[28], sn, ans;
    infile >> t;

    int i, j, k, l, len;

    bool is_cled;

    for (i = 0; i < t; ++i)
    {
        ans = "";
        for (j = 0; j < 1000; ++j)
            ans += ' ';
        infile >> c;
        for (j = 0; j < c; ++j)
        {
            infile >> sc[j];
        }
        infile >> d;
        for (j = 0; j < d; ++j)
        {
            infile >> sd[j];
        }
        infile >> n;
        infile >> sn;
        ans[0] = sn[0];
        len = 1;
        for (j = 1; j < n; ++j)
        {
            is_cled = false;
            if (len > 0)
            {
                for (k = 0; k < c; ++k)
                {
                    if ((sc[k][0] == sn[j] && sc[k][1] == ans[len - 1]) || (sc[k][1] == sn[j] && sc[k][0] == ans[len - 1]))
                    {
                        ans[len - 1] = sc[k][2];
                        break;
                    }
                }
                if (k != c)
                    continue;

                for (k = 0; k < d; ++k)
                {
                    if (sd[k][0] == sn[j])
                    {
                        for (l = 0; l < len; ++l)
                        {
                            if (ans[l] == sd[k][1])
                            {
                                len = 0;
                                is_cled = true;
                                break;
                            }
                        }
                    }
                    else if (sd[k][1] == sn[j])
                    {
                        for (l = 0; l < len; ++l)
                        {
                            if (ans[l] == sd[k][0])
                            {
                                len = 0;
                                is_cled = true;
                                break;
                            }
                        }
                    }

                    if (is_cled == true)
                        break;
                }

                if (k != d)
                    continue;
            }

            ans[len] = sn[j];
            len++;           
        }

        outfile << "Case #" << i + 1<< ": [";
        for (j = 0; j < len - 1; ++j)
            outfile << ans[j] << ", ";
        if (len > 0)
            outfile << ans[len - 1];
        outfile << "]" << endl;
    }
    return 0;
}
