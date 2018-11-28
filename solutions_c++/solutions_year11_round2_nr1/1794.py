#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>

using namespace std;

int main() {
    int numTestCases;
    cin>>numTestCases;
    stringstream output;
    for (int i=0;i<numTestCases;i++)
    {
        /* inputu al */
        int numTeams;
        cin>>numTeams;
        vector<vector<char> > results;
        vector<float> wp,owp,oowp;
        vector<int> numMatches;
        for (int j=0;j<numTeams;j++)
        {
            string line;
            cin>>line;
            vector<char> result;
            for (int k=0;k<numTeams;k++)
            {
                result.push_back(line[k]);
            }
            results.push_back(result);
        }
        /* wp hesapla */
        for (int j=0;j<numTeams;j++)
        {
            int total = 0;
            int win = 0;
            for (int k=0;k<numTeams;k++)
            {

                if (results[j][k]=='1')
                {
                    total++;
                    win++;
                }
                else if(results[j][k]=='0')
                {
                    total++;
                }
            }
            wp.push_back((float)win/total);
            numMatches.push_back(total);
        }
        /* owp hesapla */
        for (int j=0;j<numTeams;j++)
        {
            float sum = 0;
            int parts = 0;
            for (int k=0;k<numTeams;k++)
            {
                if (results[j][k]!='.')
                {
                    if (results[k][j]=='.')
                        sum+=wp[k];
                    else if(results[k][j]=='1')
                        sum+=(wp[k]*numMatches[k]-1)/(numMatches[k]-1);
                    else
                        sum+=(wp[k]*numMatches[k])/(numMatches[k]-1);
                    parts++;
                }
            }
            owp.push_back(sum/parts);
        }
        /* oowp hesapla */
        for (int j=0;j<numTeams;j++)
        {
            float sum = 0;
            int parts = 0;
            for (int k=0;k<numTeams;k++)
            {
                if (results[j][k]!='.')
                {
                    sum+=owp[k];
                    parts++;
                }
            }
            oowp.push_back(sum/parts);
        }
        output<<"Case #"<<i+1<<":"<<endl;
        for (int j=0;j<numTeams;j++)
        {
            output<<0.25*wp[j]+0.5*owp[j]+0.25*oowp[j]<<endl;
        }
    }
    cout<<output.str();
}
