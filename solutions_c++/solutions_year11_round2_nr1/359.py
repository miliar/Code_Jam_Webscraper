#include <iostream>
#include <string>
#include <iomanip>

using namespace std;

typedef struct
{
    string schedule;
    int win;
    int total;
    double wp;
    double owp;
    double oowp;
} school;

int main()
{
    int t, n;
    school *team;

    cin >> t;
    for (int i = 0; i < t; i++)
    {
        cin >> n;
        team = new school[n];

        for (int j = 0; j < n; j++)
        {
            cin >> team[j].schedule;
            team[j].win = 0;
            team[j].total = 0;
            team[j].wp = 0.0;
            team[j].owp = 0.0;
            team[j].oowp = 0.0;
        }

        for (int j = 0; j < n; j++)
        {
            for (int k = 0; k < n; k++)
            {
                if (team[j].schedule[k] != '.')
                {
                    team[j].total++;
                    if (team[j].schedule[k] == '1')
                        team[j].win++;
                }
            }
            team[j].wp = (double)team[j].win / (double)team[j].total;
        }

        for (int j = 0; j < n; j++)
        {
            for (int k = 0; k < n; k++)
            {
                if (team[j].schedule[k] == '0')
                    team[j].owp += (double)(team[k].win - 1) / (team[k].total - 1);
                else if (team[j].schedule[k] == '1')
                    team[j].owp += (double)(team[k].win) / (team[k].total - 1);
            }
            team[j].owp /= team[j].total;
        }

        for (int j = 0; j < n; j++)
        {
            for (int k = 0; k < n; k++)\
            {
                if (team[j].schedule[k] != '.')
                    team[j].oowp += team[k].owp;
            }
            team[j].oowp /= team[j].total;
        }

        cout << "Case #" << i + 1 << ":" << endl;
        for (int j = 0; j < n; j++)
            cout << setprecision(12) <<
                0.25 * team[j].wp + 0.5 * team[j].owp + 0.25 * team[j].oowp << endl;

        delete [] team;
    }

    return 0;
}
