#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <iomanip>

enum Result {WIN, LOSS, NONE};

struct Team
{
    std::vector<Result> results;
    double wp;
    double owp;
    double oowp;
};

double getRPI(struct Team& team)
{

}

int main()
{
    int numCases;
    std::cin >> numCases;

    std::vector<int> values;

    for (int i = 0; i < numCases; i++)
    {
        std::cout << "Case #" << (i + 1) << ":" << std::endl;

        int numTeams;
        std::cin >> numTeams;
        
        std::vector<Team*> schedule;
        
        for(int n = 0; n < numTeams; n++)
        {
            Team* t = new Team();
            for(int j = 0; j < numTeams; j++)
            {
                char c;
                std::cin >> c;
                if (c == '.') { t->results.push_back(NONE); }
                if (c == '1') { t->results.push_back(WIN); }
                if (c == '0') { t->results.push_back(LOSS); }
            }
            
            schedule.push_back(t);
        }
        
        for(int n = 0; n < numTeams; n++)
        {
            std::vector<Result> res = schedule.at(n)->results;
            
            double won = 0, lost = 0;
            for(int j = 0; j < numTeams; j++)
            {
                if (res.at(j) == WIN) { won+=1; }
                if (res.at(j) == LOSS) { lost+=1; }
            }
            
            schedule.at(n)->wp = won / (won + lost);
        }
        
        for(int n = 0; n < numTeams; n++)
        {
            double sumWp = 0;
            int numOp = 0;

            for(int j = 0; j < numTeams; j++)
            {
                if (schedule.at(n)->results.at(j) == NONE) continue;

                numOp++;
                
                double won = 0, lost = 0; 
                
                std::vector<Result> res = schedule.at(j)->results;
                
                for(int l = 0; l < numTeams; l++)
                {
                    if (l == n) continue;
                    
                    if (res.at(l) == WIN) { won+=1; }
                    if (res.at(l) == LOSS) { lost+=1; }
                }
                
                sumWp += won / (won + lost);
            }
            
            schedule.at(n)->owp = sumWp / (double(numOp));
        }
        
        for(int n = 0; n < numTeams; n++)
        {
            double sumOwp = 0;
            int numOp = 0;
            
            for(int j = 0; j < numTeams; j++)
            {
                if (schedule.at(j)->results.at(n) == NONE) continue;
               
                sumOwp += schedule.at(j)->owp;
                numOp++;
            }
            
            schedule.at(n)->oowp = sumOwp / (double(numOp));
        }
        
        for(int n = 0; n < numTeams; n++)
        {
//            std::cout << schedule.at(n)->wp << " " << schedule.at(n)->owp << " " << schedule.at(n)->oowp << " - ";
            double rpi = 0.25 * schedule.at(n)->wp;
            rpi += 0.50 * schedule.at(n)->owp;
            rpi += 0.25 * schedule.at(n)->oowp;
            std::cout << std::setprecision(12) << rpi << std::endl;
        }

    }
}
