#include <fstream>
#include <iomanip>
#include <iostream>
#include <vector>
using namespace std;

#define IDX(i, j, N) ((i)*(N) + (j))

int main(int argc, char **argv)
{
    const int MAX_N = 101;
    const char ifname[] = "input.txt";
    const char ofname[] = "output.txt";

    ifstream inf(ifname);
    ofstream ouf(ofname);

    long T,N,i,t,j,k;
    inf >> T;
    unsigned char *a = new unsigned char[MAX_N * MAX_N];
    vector<double> wp, owp, oowp;
    char tmp;
    int count;

    for (t = 0; t < T; t++)
    {
        inf >> N;

        wp.clear();
        wp.resize(N);
        owp.clear();
        owp.resize(N);
        oowp.clear();
        oowp.resize(N);

        for (i = 0; i < N; i++)
        {
            count = 0;
            for (j = 0; j < N; j++)
            {
                inf >> tmp;
                a[IDX(i, j, N)] = tmp;
                if (tmp == '0')
                {
                    count++;
                }
                else if (tmp == '1')
                {
                    wp[i] += 1.0f;
                    count++;
                }
            }
            wp[i] /= count;
            inf.getline(&tmp, 1);
        }

        long ccount;
        double colsum;
        for (i = 0; i < N; i++)
        {
            ccount = 0;
            for (k = 0; k < N; k++)
            {
                if (i == k || a[IDX(k, i, N)] == '.') continue;
                colsum = 0.0;
                count = 0;
                for (j = 0; j < N; j++)
                {
                    tmp = a[IDX(k, j, N)];
                    if (j == i || tmp == '.') continue;
                    if (tmp == '0')
                    {
                        count++;
                    }
                    else if (tmp == '1')
                    {
                        colsum += 1.0f;
                        count++;
                    }
                }
                
                if (count > 0) {
                    colsum /= count;
                    ccount++;
                    owp[i] += colsum;
                }
            }
            if (ccount > 0) owp[i] /= ccount;
        }


        for (i = 0; i < N; i++)
        {
            count = 0;
            for (j = 0; j < N; j++)
            {
                tmp = a[IDX(j, i, N)];
                if (i == j || tmp == '.') continue;
                oowp[i] += owp[j];
                count++;
            }
            oowp[i] /= count;
        }

        ouf << "Case #" << t + 1 << ":" << endl;
        for (i = 0; i < N; i++)
        {
            ouf << setprecision( 12 ) << 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i] << endl;
        }

    }
    delete[] a;
    
    inf.close();
    ouf.close();
    return 0;
}