#include <iostream>

using namespace std;

        double WP[100];
        int num[100];
        int win[100];
        double OWP[100][100];
        double OWP1[100];
        double OOWP[100];
        double RPI[100];

int main()
{
    int n = 0;
    cin >> n;
    for(int i = 0; i < n; i++)
    {
        int m = 0;
        cin >> m;
        string A[m];
        for(int j = 0; j < m; j++)
        {
            cin >> A[j];
        }
        for(int k = 0; k < m; k++)
        {
            WP[k] = 0;
            OWP1[k] = 0;
            num[k] = 0;
            win[k] = 0;
            OOWP[k] = 0;
            for(int l = 0; l < m; l++)
            {
                if(A[k][l] == '1')
                {
                    win[k]++;
                    num[k]++;
                }
                else if(A[k][l] == '0')
                {
                    num[k]++;
                }
            }
            WP[k] = ((double)(win[k]))/num[k];
            //cout << WP[k] << endl;
        }
        for(int k = 0; k < m; k++)
        {
            for(int l = 0; l < m; l++)
            {
                OWP[k][l] = 0;
            }
            for(int l = 0; l < m; l++)
            {
                if(A[k][l] == '1')
                {
                    OWP[k][l] = ((double)(win[l]))/(num[l]-1);
                }
                else if(A[k][l] == '0')
                {
                    OWP[k][l] = ((double)(win[l])-1)/(num[l]-1);
                }
                else if(A[k][l] == '.')
                {
                    OWP[k][l] = 0;
                }
                //cout << k << " " << l << " " << win[l] << " " << num[l] << " " << OWP[k][l] << endl;
            }
            for(int l = 0; l < m; l++)
            {
                OWP1[k] += OWP[k][l];

            }
            OWP1[k] /= num[k];
        }
        for(int k = 0; k < m; k++)
        {
            OOWP[k] = 0;
            for(int l = 0; l < m; l++)
            {
                if(A[k][l] != '.')
                {
                    OOWP[k] += OWP1[l];
                }

            }
             OOWP[k] /= num[k];
        }
        for(int k = 0; k < m; k++)
        {
            RPI[k] = 0.25*WP[k] + 0.5*OWP1[k] + 0.25*OOWP[k];
            cout << RPI[k] << endl;
        }


    }
    return 0;
}
