#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
using namespace std;

int main()
{
    int T, t;
    vector<string> stats;
    int i, j, k;
    int N;
    vector<double> wp;
    vector<double> owp;
    vector<double> oowp;
    int games_played;
    int games_won;
    double total_wp;
    int no_opponent;

    cin >> T;
    for (t = 1; t <= T; t++)
    {
        cin >> N;
        stats.resize(N);
        for (i = 0; i < N; i++)
        {
            cin >> stats[i];
        }

        // Calculate WP
        wp.clear();
        wp.resize(N);
        for (i = 0; i < N; i++)
        {
            games_played = 0;
            games_won = 0;
            for (j = 0; j < N; j++)
            {
                switch (stats[i][j])
                {
                    case '.':
                        break;
                    case '1':
                        games_played++;
                        games_won++;
                        break;
                    case '0':
                        games_played++;
                        break;
                    default:
                        break;
                }
            }
            wp[i] = (double) games_won / games_played;
        }

        // Calculate OWP
        owp.clear();
        owp.resize(N);
        for (i = 0; i < N; i++)
        {
            total_wp = 0.0;
            no_opponent = 0;
            for (j = 0; j < N; j++)
            {
                if (stats[i][j] != '.')
                {
                    no_opponent++;
                    games_played = 0;
                    games_won = 0;
                    for (k = 0; k < N; k++)
                    {
                        if (k != i)
                        {
                            switch (stats[j][k])
                            {
                                case '.':
                                    break;
                                case '1':
                                    games_played++;
                                    games_won++;
                                    break;
                                case '0':
                                    games_played++;
                                    break;
                                default:
                                    break;
                            }
                        }
                    }
                    total_wp += (double) games_won / games_played;
                }
            }
            owp[i] = total_wp / no_opponent;
        }

        // Calculate OOWP
        oowp.clear();
        oowp.resize(N);
        for (i = 0; i < N; i++)
        {
            total_wp = 0.0;
            no_opponent = 0;
            for (j = 0; j < N; j++)
            {
                if (stats[i][j] != '.')
                {
                    no_opponent++;
                    total_wp += owp[j];
                }
            }
            oowp[i] = total_wp / no_opponent;
        }

        // Output
        cout << "Case #" << t << ":" << endl;
        for (i = 0; i < N; i++)
        {
            printf("%.9lf\n", wp[i]/4 + owp[i]/2 + oowp[i]/4);
        }
    }

    return 0;
}

