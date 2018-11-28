#include <stdio.h>
#include <string.h>
#include <iostream>
using namespace std;
int M[100][100];
int tot[100];
int won[100];
double WP [100];
double OWP [100];
double OOWP [100];
int main (void)
{
    int test, part, i, j, k;
    cin >> test;
    char c;
    for (int i = 0; i < test; i++)
    {
        memset (tot, 0, sizeof(tot));
        memset (won, 0, sizeof(tot));
        int teams;
        cin >> teams;
        for (j =0; j < teams; j++)
        {
            for (k = 0; k < teams; k++)
            {
                cin >> c;
                M[j][k] = c == '1';
                if (c == '1')
                    won[j]++;
                if (c != '.')
                    tot[j]++;
            }
            WP[j] = (double)won[j]/(double)tot[j];
//            cout <<"wp " << WP[j] << endl;
        }
        double sum;
        for (j = 0; j < teams; j++)
        {
            OWP[j] = 0.0;
            for(k = 0; k < teams; k++)
            {
                if (M[j][k]|M[k][j])
                {
                    OWP[j]+=(double)(won[k] - M[k][j])/(double)(tot[k]-(M[j][k]|M[k][j]));
//                    cout << won[k] - M[k][j] << " " << tot[k]-(M[j][k]|M[k][j]) << endl;
                }
            }
            OWP[j] /= (tot[j]);
//            cout <<"owp " << OWP[j] << endl;

        }
        for (j = 0; j < teams; j++)
        {

            OOWP[j] = 0.0;
            for (k = 0; k < teams; k++)
            {
                if (M[j][k]|M[k][j])
                    OOWP[j] += OWP[k];
            }
            OOWP[j] /= tot[j];
//            cout <<"oowp " << OWP[j] << endl;
        }
        cout << "Case #" << i+1 << ":" <<endl;
        for (j = 0; j < teams; j++)
            printf ("%.9f\n", 0.25 * WP[j] + 0.50 * OWP[j] + 0.25 * OOWP[j]);
    }

}
