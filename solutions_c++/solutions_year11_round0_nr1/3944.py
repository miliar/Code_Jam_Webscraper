//[C/C++ headers]
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <sstream>
#include <fstream>

//#define TEST

int CalculateTime(char *aInStr)
{
    int numBtns = 0;    

    char *pch = NULL;

    pch = strtok(aInStr, " ");

    if(NULL != pch)
    {
        numBtns = atoi(pch);

        #ifdef TEST
            std::cout<<"Buttons: "<<numBtns<<std::endl;
        #endif
    }

    std::vector<int> blueStepsV;
    std::vector<int> orangeStepsV;
    std::vector<char> turnsOrder;

    int bluePos = 1;
    int orangePos = 1;

    while(NULL != pch)
    {
        if(!strcmp("B", pch))
        {
            turnsOrder.push_back('B');

            pch = strtok(NULL, " ");

            blueStepsV.push_back( abs(bluePos - atoi(pch)) );

            bluePos = atoi(pch);
        }
        else if(!strcmp("O", pch))
        {
            turnsOrder.push_back('O');

            pch = strtok(NULL, " ");

            orangeStepsV.push_back( abs(orangePos - atoi(pch)) );

            orangePos = atoi(pch);
        }

        pch = strtok(NULL, " ");
    }    

    int Time = 0;

    int oIt = 0;
    int bIt = 0;

    for(int i = 0; i < turnsOrder.size(); i++)
    {
        switch(turnsOrder[i])
        {
        case 'O':
            {
                Time += orangeStepsV[oIt];

                if(blueStepsV.size() > bIt)
                {
                    if(blueStepsV[bIt] > 1 && blueStepsV[bIt] > orangeStepsV[oIt])
                    {
                        blueStepsV[bIt] = blueStepsV[bIt] - orangeStepsV[oIt] - 1;
                    }
                    else if(blueStepsV[bIt] >= 1 && blueStepsV[bIt] <= orangeStepsV[oIt])
                    {
                        blueStepsV[bIt] = 0;
                    }
                }

                Time += 1;

                oIt++;
            }
            break;

        case 'B':
            {
                Time += blueStepsV[bIt];

                if(orangeStepsV.size() > oIt)
                {
                    if(orangeStepsV[oIt] > 1 && orangeStepsV[oIt] > blueStepsV[bIt])
                    {
                        orangeStepsV[oIt] = orangeStepsV[oIt] - blueStepsV[bIt] - 1;
                    }
                    else if(orangeStepsV[oIt] >= 1 && orangeStepsV[oIt] <= blueStepsV[bIt])
                    {
                        orangeStepsV[oIt] = 0;
                    }
                }

                Time += 1;

                bIt++;
            }
            break;
        }
    }

    #ifdef TEST
        std::cout<<"Time: "<<Time<<std::endl;
    #endif

    return (Time);
}

int main(int argc, char *argv[])
{
    #ifdef TEST
        std::cout << "Bot trust---> Test mode"<<std::endl;
    #endif


        char inBuff[1024];

        //std::ifstream file("test.in");

    //[Number of test cases]
    std::cin.getline(inBuff, 1024);

    //file.getline(inBuff, 1024);

    int numCases = 0;

    std::string str(inBuff);

    numCases = atoi(str.c_str());

    #ifdef TEST
        std::cout << "Number of cases: "<<numCases<<std::endl;
    #endif

    for (int i = 0; i < numCases; i++)
    {
        std::cin.getline(inBuff, 1024);
        
        #ifdef TEST
            std::cout << "String:"<<inBuff<<std::endl;
        #endif

        std::cout<<"Case #"<<(i+1)<<": "<<CalculateTime(inBuff)<<std::endl;
    }

    return (0);
}
