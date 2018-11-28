#include <cstdlib>
#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <list>
#include <sstream>

#include <algorithm>

using namespace std;

#define FORN(i,n) for((i)=0;(i)<(n);(i)++)

int main(int argc, char *argv[])
{

    ifstream inputFile(argv[1]);
    ofstream outputFile("output.txt");

    int noTests;

    inputFile>>noTests;

    int i;

    FORN(i, noTests)
    {
        long long L,t,N,C;

        inputFile>>L>>t>>N>>C;

        vector<long long> ai;


        int j, k,l;

        FORN(j,C)
        {
            long long temp;
            inputFile>>temp;
            ai.push_back(temp);
        }

        // find where we can build boosters

        long long currentTravelCost = 0;

        vector<long double> costs;

        FORN(j,N)
        {

            long long costToCurrentStar =ai[ j%C];
            costs.push_back(costToCurrentStar);

        }


        bool boostersPlaced=false;

        FORN(j,N)
        {
            if (costs[j]*2<t)
            {
                currentTravelCost+= costs[j]*2;
                t-=costs[j]*2;
            } else {
                if (!boostersPlaced)
                {
                    currentTravelCost+=t;
                    costs[j]-=t*0.5;
                    long long min1=-1, min2=-1;
                    int index1=-1, index2=-1;
                    for(k=j;k<N;k++)
                    {
                        if (costs[k]>=min1)
                        {
                            min2=min1;
                            index2 = index1;
                            min1 = costs[k];
                            index1 = k;
                        } else if (costs[k]>min2)
                        {
                            min2 = costs[k];
                            index2 = k;
                        }
                    }

                    if ((L>=1)&&(index1!= -1))
                    {
                        costs[index1]/=2;
                    }

                    if ((L>=2)&&(index2!= -1))
                    {
                        costs[index2]/=2;
                    }

                    boostersPlaced = true;
                }

                currentTravelCost+= costs[j]*2;
            }

        }


        outputFile<<"Case #"<<i+1<<": "<<currentTravelCost<<endl;

    }


}
