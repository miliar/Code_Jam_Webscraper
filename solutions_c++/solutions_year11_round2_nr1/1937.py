#include <iostream>
#include <fstream>
#include <iomanip>// fixed << setprecision(#);
#include <vector>
#include <string>
#include <sstream>
using namespace std;
double findWP(vector<string> grid, int teamNum);
double findOWP(vector<string> grid, int teamNum);
double findOOWP(vector<string> grid, int teamNum);
int main()
{
    ifstream input ("input1.txt");
    ofstream output ("output1.txt");

    int cases;
    input >> cases;

    for(int a = 0; a < cases; a ++)
    {
        int numTeams;
        input >> numTeams;
        string temp;
        vector<string> grid;
        for(int b = 0;b < numTeams;b ++)
        {
            input >> temp;
            grid.push_back(temp);

        }
        //  RPI = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP
        output << "Case #" << a+1<< ": " << endl;
        for(int x = 0;x < numTeams; x++)
        {
            double WP, OWP, OOWP;
            WP = findWP(grid, x);
            OWP = findOWP(grid,x);
            OOWP = findOOWP(grid,x);
            double RPI = 0.25 * WP + 0.50 *OWP + 0.25 *OOWP;
            output << RPI <<endl;
        }

        //output <<endl;
    }

    return 0;
}

/*WP (Winning Percentage) is the fraction of your games that you have won.
In the example schedule, team A has WP = 1, team B has WP = 0, team C has WP = 2/3, and team D has WP = 0.5.*/
double findWP(vector<string> grid, int teamNum)
{
    int gamesPlayed =0;
    int gamesWon = 0;
    for(int a = 0; a < grid.size(); a++)
    {
        if(grid[teamNum][a] != '.')
        {
            if(grid[teamNum][a] != '0')
            {

                gamesWon += grid[teamNum][a]-'0';
            }
            gamesPlayed ++;
        }
    }
    double perc = double(gamesWon)/double(gamesPlayed);
    return perc;
}

/*OWP (Opponents' Winning Percentage) is the average WP of all your opponents, after first throwing out the games they played against you.
For example, if you throw out games played against team D, then team B has WP = 0 and
 team C has WP = 0.5. Therefore team D has OWP = 0.5 * (0 + 0.5) = 0.25. Similarly, team A has OWP = 0.5,
  team B has OWP = 0.5, and team C has OWP = 2/3.*/
double findOWP(vector<string> grid, int teamNum)
{

    //remove all games played against teamNum
    vector<int> teamsPlayed;
    for(int a = 0; a < grid.size(); a++)
    {
        if(grid[a][teamNum]!= '.' && a!= teamNum)
        {
            teamsPlayed.push_back(a);
            grid[a][teamNum] = '.';
        }

    }
   /* for(int a = 0; a < grid.size(); a++)
    {
    output << grid[a] <<endl;
    }*/
    double sumWP=0;

    //output << endl;
    for(int i = 0; i < teamsPlayed.size(); i++)
    {
        if(teamsPlayed[i] != teamNum)
        {
           sumWP+= findWP(grid,teamsPlayed[i]);
        }
    }
    double OWP = sumWP/double(teamsPlayed.size());
    return OWP;
}

/*OOWP (Opponents' Opponents' Winning Percentage) is the average OWP of all your opponents. OWP is exactly the number computed in the previous step.
For example, team A has OOWP = 0.5 * (0.5 + 2/3) = 7/12.*/
double findOOWP(vector<string> grid, int teamNum)
{
     vector<int> teamsPlayed;
    for(int a = 0; a < grid.size(); a++)
    {
        if(grid[a][teamNum]!= '.' && a!= teamNum)
        {
            teamsPlayed.push_back(a);

        }

    }

    double sumOWPs = 0;
    for(int a = 0; a < teamsPlayed.size();a ++)
    {
        if(teamsPlayed[a]!= teamNum)
        {
        sumOWPs += findOWP(grid,teamsPlayed[a]);
        }
    }
    double OOWP = sumOWPs/double(teamsPlayed.size());
return OOWP;
}
