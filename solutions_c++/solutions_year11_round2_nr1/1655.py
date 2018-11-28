#include <iostream>
#include <fstream>

using namespace std;

double calculatePercentage(int won, int played)
{
    return (played == 0) ? 0 : ((double)won / (double)played);
}

double calculateOWP(char** teams, const int n, const int indexToSkip)
{
    int i, j;
    
    double OWP = 0;
    int teamsPlayed = 0;

    for (i = 0; i < n; i++)
    {
        if (teams[i][indexToSkip] == '.')
            continue;

        int gamesPlayed = 0, gamesWon = 0;

        for (j = 0; j < n; j++)
        {
            if (indexToSkip == j)
                continue;

            if (teams[i][j] != '.')
            {
                gamesPlayed++;

                if (teams[i][j] == '1')
                    gamesWon++;
            }
        }
        
        OWP += calculatePercentage(gamesWon, gamesPlayed);
        teamsPlayed++;
    }

    return OWP / (double)teamsPlayed;
}

double getOOWP(char** teams, double* OWP, const int n, const int indexToSkip)
{
    int i;
    int teamsPlayed = 0;
    double OOWP = 0;

    for (i = 0; i < n; i++)
    {
        if (teams[i][indexToSkip] == '.')
            continue;

        teamsPlayed++;
        OOWP += OWP[i];
    }

    return OOWP / (double)teamsPlayed;
}

int main()
{
    ifstream input("input.dat");
    ofstream output("output.dat");

    output.precision(12);
    int testCases, testCase = 0, i, j;
    input >> testCases;

    while (testCases--)
    {
        testCase++;

        int n;
        input >> n;

        // read teams
        char** teams = new char*[n];
        double* WP = new double[n];
        double* OWP = new double[n];

        for (i = 0; i < n; i++)
        {
            teams[i] = new char[n];
            for (j = 0; j < n; j++)
            {
                input >> teams[i][j];
            }
        }

        for (i = 0; i < n; i++)
        {
            int gamesPlayed = 0, gamesWon = 0;

            for (j = 0; j < n; j++)
            {
                if (teams[i][j] != '.')
                {
                    gamesPlayed++;

                    if (teams[i][j] == '1')
                        gamesWon++;
                }
            }

            WP[i] = calculatePercentage(gamesWon, gamesPlayed);
            OWP[i] = calculateOWP(teams, n, i);
        }

        output << "Case #" << testCase << ":\n";
        for (i = 0; i < n; i++)
        {
            double finalWP = 0.25f * WP[i] + 0.5f * OWP[i] + 0.25f * getOOWP(teams, OWP, n, i);

            cout.precision(12);
            output << finalWP << "\n";
        }

        // cleanup
        for (i = 0; i < n; i++)
            delete teams[i];
        
        delete teams;
        delete WP;
        delete OWP;
    }

    getchar();

    input.close();
    output.close();

    return 0;
}