#include <iostream>
#include <map>
#include <vector>

using namespace std;

struct TeamInfo
{
       vector<int> winFrom;
       vector<int> loseFrom;
};

double getOWP(int teamCount , map<int , TeamInfo>& teamIn)
{
       double ret = 0;
       TeamInfo targetTeam = teamIn[teamCount];
       vector<int> winVec = targetTeam.winFrom;
       vector<int> losVec = targetTeam.loseFrom;
       
       for(int winCount = 0; winCount < winVec.size(); winCount++)
       {
               int curOppTeam = winVec[winCount];
               TeamInfo oppTeamInfo = teamIn[curOppTeam];
               ret += ( (double)(oppTeamInfo.winFrom.size()) / (oppTeamInfo.winFrom.size() + 
               oppTeamInfo.loseFrom.size() -1));
       }
       
       for(int losCount = 0; losCount < losVec.size(); losCount++)
       {
               int curOppTeam = losVec[losCount];
               TeamInfo oppTeamInfo = teamIn[curOppTeam];
               ret += ( (double)(oppTeamInfo.winFrom.size() - 1) / (oppTeamInfo.winFrom.size() + 
               oppTeamInfo.loseFrom.size() -1));
       }
       return (ret / (winVec.size() + losVec.size()));
}

int main()
{
    int testCase;
    cin >> testCase;
    for(int caseNum = 1 ; caseNum <= testCase; caseNum++)
    {
            int teamNum;
            cin >> teamNum;
            cout << "Case #" << caseNum << ": " << endl;

            map<int , TeamInfo> teamIn;
            map<int , double> owpTeam; 
            for(int teamCount = 0; teamCount < teamNum; teamCount++)
            {
                    TeamInfo temp;
                    for(int inerTeamCount = 0; inerTeamCount < teamNum; inerTeamCount++)
                    {
                            char resInfo;
                            cin >> resInfo;
                            if(resInfo == '1')
                            {
                              temp.winFrom.push_back(inerTeamCount);         
                            }
                            else if(resInfo == '0')
                            {
                              temp.loseFrom.push_back(inerTeamCount);  
                            }
                    }
                    teamIn[teamCount] = temp;                     
            }
            
            for(int teamCount = 0; teamCount < teamNum; teamCount++)
            {
                    double res = 0;
                    double wp; 
                    TeamInfo& curTeam = teamIn[teamCount];
                    wp = ( (double)(curTeam.winFrom.size()) / (curTeam.winFrom.size() + curTeam.loseFrom.size()));
                    map<int , double>::iterator it;
                    it = owpTeam.find(teamCount);
                    double Owp;
                    if(it == owpTeam.end())
                    {
                       Owp = getOWP(teamCount , teamIn);
                       owpTeam[teamCount] = Owp;                                                  
                    }
                    else 
                    {
                       Owp = it->second; 
                    }
        
                    double oowp = 0;            
                    vector<int> winVec = curTeam.winFrom;
                    vector<int> losVec = curTeam.loseFrom;
                    map<int , double>::iterator itNxt;            
                    for(int winCount = 0; winCount < winVec.size(); winCount++)
                    {
                            int curOppTeam = winVec[winCount];
                            itNxt = owpTeam.find(curOppTeam);
                            double curOwp;
                            if(itNxt == owpTeam.end())
                            {
                                  curOwp = getOWP(curOppTeam , teamIn);
                                  owpTeam[curOppTeam] = curOwp;                                                  
                             }
                             else 
                             {
                                  curOwp = itNxt->second; 
                             }
                             oowp += curOwp; 
                    }
       
                    for(int losCount = 0; losCount < losVec.size(); losCount++)
                    {
                         int curOppTeam = losVec[losCount];
                         itNxt = owpTeam.find(curOppTeam);
                         double curOwp;
                         if(itNxt == owpTeam.end())
                         {
                          curOwp = getOWP(curOppTeam , teamIn);
                          owpTeam[curOppTeam] = curOwp;                                                  
                         }
                         else 
                         {
                          curOwp = itNxt->second; 
                         }
                         oowp += curOwp; 
                    }
                    oowp = oowp / (winVec.size() + losVec.size());
                    
                    res =  0.25 * wp + 0.50 * Owp + 0.25 * oowp;
                    
                    cout << res << endl;       
            }
            
                     
    }
        
    return 0;
}
