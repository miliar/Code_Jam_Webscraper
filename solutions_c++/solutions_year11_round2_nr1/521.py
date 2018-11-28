#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

char c[128][128];
int wins[128], games[128];

int main()
{
    ifstream f("1l.in");
    ofstream g("1.out");
    int t, T, n, i, j, nr;
    double WP[128], OWP[128], OOWP[128], s;

    f >> T;
    for(t = 1; t <= T; t++){
        f >> n;
        f.get();
        for(i = 0; i < n; i++){
            f.getline(c[i], 128);
            wins[i] = games[i] = 0;
        }

        for(i = 0; i < n; i++)
            for(j = 0; j < n; j++){
                if(c[i][j] == '1')
                    wins[i]++, games[i]++;
                if(c[i][j] == '0')
                    games[i]++;
            }
        g << "Case #" << t << ":\n";
        for(i = 0; i < n; i++)
            WP[i] = (double)wins[i] / games[i];

        for(i = 0; i < n; i++){
            s = 0;
            nr = 0;
            for(j = 0; j < n; j++)
                if(c[i][j] != '.'){
                    nr++;
                    if(c[i][j] == '0')
                        s += (double)(wins[j] - 1) / (games[j] - 1);
                    else s += (double)(wins[j]) / (games[j] - 1);
                }
            OWP[i] = (double)s/nr;
        }

        for(i = 0; i < n; i++){
            s = 0;
            nr = 0;
            for(j = 0; j < n; j++)
                if(c[i][j] != '.'){
                    nr++;
                    s += OWP[j];
                }
            OOWP[i] = (double)s / nr;
        }

        for(i = 0; i < n; i++)
            g << setprecision(9) << 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i] << "\n";



    }

    return 0;
}
