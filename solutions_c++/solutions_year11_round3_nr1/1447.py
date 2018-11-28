#include <myincludes.h>

#define FILE_IN "A-large.in"
#define FILE_OUT "A-large.out"

using namespace std;

void Solve(ifstream &iFile, ofstream &oFile)
{
    oFile <<endl;

    int i,j;
    int r,c;
    iFile >> r;
    iFile >> c;
    vector<string> all;

    for(i=0;i<r;i++)
    {
        string tmp;
        iFile >> tmp;
        all.push_back(tmp);
    }

    for(i=0;i<r;i++)
    {
        for(j=0;j<c;j++)
        {
            if(all[i][j] == '#')
            {
                if((i==r-1)||(j==c-1))
                {
                    oFile << "Impossible" <<endl;
                    return;
                }
                else if((all[i+1][j]=='#')&&(all[i][j+1]=='#')&&(all[i+1][j+1]=='#'))
                {
                    all[i][j] = '/';
                    all[i+1][j] = '\\';
                    all[i][j+1] = '\\';
                    all[i+1][j+1] = '/';
                }
                else
                {
                    oFile << "Impossible" <<endl;
                    return;
                }
            }
        }
    }

    for(i=0;i<r;i++)
    {
        oFile << all[i] <<endl;
    }
}

int main()
{
    ifstream iFile(FILE_IN);
    ofstream oFile(FILE_OUT);;

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
