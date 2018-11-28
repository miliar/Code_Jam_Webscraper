

#include <iostream>
#include <vector>
#include <cstdlib>
using namespace std;


double WP(const vector<vector<int> >& schedule, int team)
{
    int wins = 0;
    int games = 0;
    for(int i = 0, size = schedule.size(); i < size; i++)
    {
        wins = wins + (schedule[team][i] == 1 ? 1 : 0);
        games = games + abs(schedule[team][i]);
    }
    if(games == 0) return 0;
    return ((double)wins)/((double)games);
}


double OWP(vector<vector<int> > schedule, int team)
{
    double owp = 0.0;
    double opponents = 0.0;
    for(int i = 0, size = schedule.size(); i < size; i++)
    {
        if(schedule[team][i] != 0)
        {
            opponents += 1.0;
            int result = schedule[team][i];
            schedule[team][i] = 0;
            schedule[i][team] = 0;
            owp = owp + WP(schedule, i);
            schedule[team][i] = result;
            schedule[i][team] = -result;
        }
    }
    return owp/opponents;
}


double OOWP(vector<vector<int> > schedule, int team)
{
    double oowp = 0.0;
    double opponents = 0.0;
    for(int i = 0, size = schedule.size(); i < size; i++)
    {
        if(schedule[team][i] != 0)
        {
            opponents += 1.0;
            oowp = oowp + OWP(schedule, i);
        }
    }
    return oowp/opponents;;
}


double RPI(const vector<vector<int> >& schedule, int team)
{
    double wp = WP(schedule, team);
    double owp = OWP(schedule, team);
    double oowp = OOWP(schedule, team);
    return 0.25*wp + 0.5*owp + 0.25*oowp;
}



int main()
{
    int cases;
    cin >> cases;
    cout.precision(10);
    for(int k = 0; k < cases; k++)
    {
        int teams;
        cin >> teams;
        vector<vector<int> > schedule(teams, vector<int>(teams, 0));
        for(int i = 0; i < teams; i++)
        {
            for(int j = 0; j < teams; j++)
            {
                char score;
                cin >> score;
                if(score == '.')
                {
                    schedule[i][j] = 0;
                }
                else if(score == '0')
                {
                    schedule[i][j] = -1;
                }
                else
                {
                    schedule[i][j] = 1;
                }
            }
        }
        
        cout << "Case #" << (k + 1) << ":\n";
        for(int i = 0; i < teams; i++)
        {
            cout << RPI(schedule, i) << "\n";
        }
    }


    return 0;
}


