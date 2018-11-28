#include <assert.h>
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

struct Team
{
    double OWPM;
    double WPLossM;
    double WPWinM;
    double WPM;
    double RPIM;
};

class RPI
{
public:
    void Solve()
    {
        // First pass. calc WPM, and WPmodM
        int w = scheduleM[0].length();
        for (unsigned int i = 0; i < scheduleM.size(); i++)
        {
            int nGames = 0;
            int nWon = 0;
            for (int j = 0; j < w; j++)
            {
                if (scheduleM[i][j] != '.')
                {
                    nGames++;
                    if (scheduleM[i][j] == '1') {
                        nWon++;
                    }
                }
            }
            teamsM[i].WPM = (double) nWon / nGames;
            teamsM[i].WPWinM = (double) (nWon - 1) / (nGames - 1);
            teamsM[i].WPLossM = (double) (nWon) / (nGames - 1);
        }
        
        // Second pass. calc owp
        for (unsigned int i = 0; i < scheduleM.size(); i++)
        {
            double owpSum = 0;
            int nOpps = 0;
            for (int j = 0; j < w; j++)
            {
                if (scheduleM[i][j] != '.') {
                    if (scheduleM[i][j] == '1') {
                        owpSum += teamsM[j].WPLossM;
                    }
                    else {
                        owpSum += teamsM[j].WPWinM;
                    }
                    nOpps++;
                }
            }
            teamsM[i].OWPM = owpSum / nOpps;
        }
        
        // Third pass. calc RPI
        for (unsigned int i = 0; i < scheduleM.size(); i++)
        {
            double oowpSum = 0;
            int nOpps = 0;
            for (int j = 0; j < w; j++)
            {
                if (scheduleM[i][j] != '.') {
                    oowpSum += teamsM[j].OWPM;
                    nOpps++;
                }
            }
            double oowp = oowpSum / nOpps;
            teamsM[i].RPIM = 0.25 * teamsM[i].WPM + 0.50 * teamsM[i].OWPM + .25 * oowp;
        }
    }

    void Start()
    {
        int T = 0;
        cin >> T;
        
        for (int t = 0; t < T; t++) {
            this->Reset();
            int N = 0;
            cin >> N;
            teamsM.resize(N);
            scheduleM.resize(N);
            
            for (int n = 0; n < N; n++)
            {
                cin >> scheduleM[n];
            }

            cout << "Case #" << (t + 1) << ":\n";
            this->Solve();
            for (unsigned int i = 0; i < teamsM.size(); i++)
            {
                printf("%1.12f\n", teamsM[i].RPIM);
            }
        }
    }
    
    void Reset()
    {
        scheduleM.clear();
        teamsM.clear();
    }
    
private:
    vector<string> scheduleM;
    vector<Team> teamsM;
};

int main(int argc, const char *argv[])
{
    RPI g;
    g.Start();
    return 0;
}
