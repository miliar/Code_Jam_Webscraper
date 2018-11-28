#include <iostream>
#include <fstream>

using namespace std;


int main()
{
    int triple[150][5];
    int S;
    int NPlayers;
    int n;
    int p;
    int nS=0;
    int input;
    int result=0;
    ifstream in("input");
    ofstream out("output");
    in >> n;
    for(int i=0;i<n;i++)
    {
        result=0;
        nS=0;
        in >> NPlayers;
        in >> S;
        in >> p;

        for(int j=0;j<NPlayers; j++)
        {
            in >> input;
            triple[j][0] = triple[j][1] = triple[j][2] = input/3;
            if(triple[j][0] + triple[j][1] + triple[j][2] != input)
            {
                triple[j][0]++;
                if(triple[j][0] + triple[j][1] + triple[j][2] != input)
                    triple[j][1]++;
            }
        }

        for(int j=0;j<NPlayers; j++)
        {
            if(nS == S)
            {
                if (triple[j][0] >= p ||  triple[j][1] >= p || triple[j][2] >= p)
                    result++;
            }
            else
            {
                if (triple[j][0] >= p ||  triple[j][1] >= p || triple[j][2] >= p)
                    result++;
                else if(triple[j][0] == triple[j][1] == triple[j][2] && triple[j][2] != 0)
                {
                    if(triple[j][0] +1 >= p)
                       {
                           result++;
                           nS++;
                       }
                }
                else if((triple[j][0] == triple[j][1]) && triple[j][1] != 0)
                {
                    if(triple[j][0] +1 >= p)
                       {
                           result++;
                           nS++;
                       }
                }
            }
        }

        out << "Case #" << i+1 << ": " << result << endl;
    }
    return 0;
}
