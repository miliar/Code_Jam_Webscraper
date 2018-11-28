#include <cstdlib>
#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <list>
#include <sstream>

#include <algorithm>

using namespace std;


int main(int argc, char *argv[])
{

    ifstream inputFile(argv[1]);
    ofstream outputFile("output.txt");

    int noTests;

    inputFile>>noTests;

    for (size_t i = 0; i<noTests; i++)
    {
        int N;
        inputFile>>N;

        char matches[100][100];

        double OWP[100], OOWP[100], RPI[100];

        vector<pair<double,int> > WP;
        WP.resize(100);

        for (size_t j=0; j<N; j++)
        {
            WP[j].first = 0;
            WP[j].second = 0;

            OOWP[j] = 0;
            for (size_t k=0; k<N;k++)
            {
                inputFile>>matches[j][k];
                OWP[j]=0;
            }
        }


        for (size_t j=0;j<N;j++)
        {
            int teamsPlayed = 0;
            for (size_t k=0; k<N;k++)
            {
                if (matches[j][k] != '.')
                {
                    teamsPlayed++;
                    if (matches[j][k] == '1')
                    {
                       WP[j].first++;
                    }
                }
            }
            WP[j].second=teamsPlayed;
            WP[j].first/=teamsPlayed;
        }


        for (size_t j=0;j<N;j++)
        {
            int teamsPlayed = 0;
            for (size_t k=0; k<N;k++)
            {
                if (matches[j][k] != '.')
                {
                    teamsPlayed++;
                    if (matches[j][k] == '1')
                    {
                      OWP[j]+= (WP[k].first* WP[k].second)/(WP[k].second-1);
                  } else {
                      OWP[j]+= (WP[k].first* WP[k].second - 1)/(WP[k].second-1);
                  }
                }
            }
            OWP[j]/=teamsPlayed;
        }


        for (size_t j=0;j<N;j++)
        {
            int teamsPlayed = 0;
            for (size_t k=0; k<N;k++)
            {
                if (matches[j][k] != '.')
                {
                    teamsPlayed++;

                      OOWP[j]+= OWP[k];
                  }
            }
            OOWP[j]/=teamsPlayed;
        }

        for (size_t j=0; j<N; j++)
        {
            RPI[j] = 0.25*WP[j].first + 0.5 * OWP[j] + 0.25*OOWP[j];
        }

        outputFile<<"Case #"<<i+1<<":"<<endl;
        for (size_t j=0; j<N; j++)
        {
            outputFile<<RPI[j]<<endl;
        }

        cout<<endl;


    }



}
