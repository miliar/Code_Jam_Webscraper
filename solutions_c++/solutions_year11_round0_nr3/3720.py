//[C/C++ headers]
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <sstream>
#include <fstream>

//#define TEST

long int SplitCandy(int aPieces, char *aInStr)
{
    std::vector<long int> baseVector;

    //std::cout<<"Size: "<<baseVector.size()<<std::endl;

    char *pch = NULL;

    pch = strtok(aInStr, " ");

    while(NULL != pch)
    {
        baseVector.push_back( atoi(pch) );

        #ifdef TEST
            std::cout<<"Value: "<<atol(pch)<<std::endl;
        #endif

        pch = strtok(NULL, " ");
    }

    long int minValue = 0;

    for(int i = 0; i < baseVector.size(); i++)
    {
        long int left = 0;
        long int right = 0;

        left = baseVector[i];

        for(int j = 0; j < baseVector.size(); j++)
        {
            if(i != j)
            {
                right = (right^baseVector[j]);
            }
        }

        if (left == right)
        {
            //std::cout<<"Equal pairs found"<<std::endl;

            if(0 == minValue)
            {
                minValue = left;
            }
            else if(left < minValue)
            {
                minValue = left;
            }
        }
    }

    if(minValue > 0)
    {
        long int retVal = 0;

        for(int i = 0; i < baseVector.size(); i++)
        {
            retVal = retVal + baseVector[i];
        }

        retVal = retVal - minValue;

        return (retVal);
    }

    return (0);
}

int main(int argc, char *argv[])
{
    #ifdef TEST
        std::cout << "Candy splitting---> Test mode"<<std::endl;
    #endif


    char inBuff[1024];

   // std::ifstream file("test.in");

    //[Number of test cases]
    std::cin.getline(inBuff, 1024);

    //file.getline(inBuff, 1024);

    int numCases = 0;

    std::string str(inBuff);

    numCases = atoi(str.c_str());

    #ifdef TEST
        std::cout << "Number of cases: "<<numCases<<std::endl;
    #endif

    for(int i = 0; i < numCases; i++)
    {
        //file.getline(inBuff, 1024);
        std::cin.getline(inBuff, 1024);

        int pieces = atoi(inBuff);

        //std::cout<<"Pieces: "<<pieces<<std::endl;

        //file.getline(inBuff, 1024);
        std::cin.getline(inBuff, 1024);

        //std::cout<<"Values: "<<inBuff<<std::endl;

        long int retVal = SplitCandy(pieces, inBuff);

        if(0 == retVal)
        {
            std::cout<<"Case #"<<(i+1)<<": "<<"NO"<<std::endl;
        }
        else
        {
            std::cout<<"Case #"<<(i+1)<<": "<<retVal<<std::endl;
        }        

    }

    return (0);
}
