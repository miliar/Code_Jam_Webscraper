#include <myincludes.h>

#define FILE_IN "A-large.in"
#define FILE_OUT "A-large.out"

using namespace std;

void Solve(ifstream &iFile, ofstream &oFile)
{
    int i,j;
    int n;
    iFile>>n;

    vector<vector<char> > schedule;
    for(i=0;i<n;i++)
    {
        vector<char> tmp;
        string tmpS;
        iFile>>tmpS;
        for(j=0;j<n;j++)
        {
            char tmpC;
            tmpC = tmpS[j];
            tmp.push_back(tmpC);
        }
        schedule.push_back(tmp);
    }

    vector<double> numWins;
    vector<double> numGames;
    vector<double> wp;
    vector<double> owp;
    vector<double> oowp;

    for(i=0;i<n;i++)
    {
        double sumWp = 0;
        double nGames = 0;
        for(j=0;j<n;j++)
        {
            if(schedule[i][j]=='1')
            {
                sumWp++;
                nGames++;
            }
            else if(schedule[i][j]=='0')
            {
                nGames++;
            }
        }

        numWins.push_back(sumWp);
        numGames.push_back(nGames);
        wp.push_back(sumWp/nGames);
    }

    for(i=0;i<n;i++)
    {
        double sumOwp = 0;
        for(j=0;j<n;j++)
        {
            if(schedule[i][j]=='1')
            {
                double tmpWpRival = numWins[j] / (numGames[j] - 1);
                sumOwp += tmpWpRival;
            }
            else if(schedule[i][j]=='0')
            {
                double tmpWpRival = (numWins[j] - 1) / (numGames[j] - 1);
                sumOwp += tmpWpRival;
            }
        }
        owp.push_back(sumOwp / numGames[i]);
    }

    for(i=0;i<n;i++)
    {
        double sumOowp = 0;
        for(j=0;j<n;j++)
        {
            if(schedule[i][j]!='.')
            {
                sumOowp += owp[j];
            }
        }
        oowp.push_back(sumOowp/numGames[i]);
    }

    oFile <<endl;
    for(i=0;i<n;i++)
    {
        double rpi = 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i];
        oFile << rpi <<endl;
    }
//
//    oFile <<endl <<endl;
//
//    oFile <<numWins[0] <<'\t' <<numGames[0]<<'\t' <<wp[0] <<'\t'<<owp[0] <<'\t'<<oowp[0] <<endl <<endl;
}

int main()
{
    ifstream iFile(FILE_IN);
    ofstream oFile(FILE_OUT);;
    oFile <<setprecision(12);

    int caseNum;
    if(!iFile.is_open())
    {
        cout << "iFile not open!" <<endl;
    }
    iFile >> caseNum;

    int i;

    for(i=0;i<caseNum;i++)
    {
        oFile <<"Case #" <<i+1 <<": ";

        Solve(iFile,oFile);
    }

    iFile.close();
    oFile.close();

    return 0;
}
