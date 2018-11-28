//[C/C++ headers]
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <sstream>
#include <fstream>

//#define TEST

struct pair
{
    pair()
    {
        first = 0;
        second = 0;
        result = 0;
    }

    char first;
    char second;

    char result;
};

struct oppos
{
    oppos()
    {
        first = 0;
        second = 0;
    }

    char first;
    char second;
};

std::vector<char> CastMagic(char *aInStr)
{
    //std::cout<<aInStr<<std::endl;

    char *pch = NULL;

    //[Pairs]
    pch = strtok(aInStr, " ");

    int numPairs =  0;

    std::vector<pair> mPairs;

    numPairs = atoi(pch);

    if(numPairs > 0)
    {
        //std::cout<<"Pairs num: "<<numPairs<<std::endl;

        for(int i = 0; i < numPairs; i++)
        {
            pch = strtok(NULL, " ");

            pair lPair;

            lPair.first = pch[0];
            lPair.second = pch[1];
            lPair.result = pch[2];

            mPairs.push_back(lPair);
        }

    }

    //[Opposite]
    pch = strtok(NULL, " ");

    int numOppos = 0;

    numOppos = atoi(pch);

    std::vector<oppos> mOppos;

    for(int i = 0; i < numOppos; i++)
    {
        pch = strtok(NULL, " ");

        oppos lOppos;

        lOppos.first = pch[0];
        lOppos.second = pch[1];

        mOppos.push_back(lOppos);
    }

    //[Sequence]
    std::vector<char> mSequence;

    pch = strtok(NULL, " ");

    int magicNum = 0;

    magicNum = atoi(pch);

    pch = strtok(NULL, " ");

    for(int i = 0; i < magicNum; i++)
    {
        mSequence.push_back(pch[i]);
    }

    //[Cast part]
    std::vector<char> outSeq;

    for(int i = 0; i < magicNum; i++)
    {
        outSeq.push_back(mSequence[i]);

        if(outSeq.size() > 1)
        {
            for(int j = 0; j < mPairs.size(); j++)
            {
                if(mPairs[j].first == outSeq[outSeq.size()-1])
                {
                    if(mPairs[j].second == outSeq[outSeq.size()-2])
                    {
                        outSeq.pop_back();
                        outSeq.pop_back();
                        outSeq.push_back(mPairs[j].result);                        
                    }
                }
                else if(mPairs[j].second == outSeq[outSeq.size()-1])
                {
                    if(mPairs[j].first == outSeq[outSeq.size()-2])
                    {
                        outSeq.pop_back();
                        outSeq.pop_back();
                        outSeq.push_back(mPairs[j].result);                        
                    }
                }

            }

            for(int j = 0; j < mOppos.size(); j++)
            {
                if(outSeq[outSeq.size() - 1] == mOppos[j].first)
                {                    
                    for(int k = (outSeq.size()-1); k >= 0; k--)
                    {
                        if(outSeq[k] == mOppos[j].second)
                        {
                           outSeq.erase(outSeq.begin(), outSeq.end());                          
                           break;
                        }
                    }                    
                }
                else if(outSeq[outSeq.size() - 1] == mOppos[j].second)
                {
                    for(int k = (outSeq.size()-1); k >= 0; k--)
                    {
                        if(outSeq[k] == mOppos[j].first)
                        {
                            outSeq.erase(outSeq.begin(), outSeq.end());                            
                            break;
                        }                        
                    }                    
                }

            }            
        }        
    }

    std::vector<char>  outStr;

    outStr.push_back('[');

    for(int i = 0; i < outSeq.size(); i++)
    {
        if(i !=0)
        {
            outStr.push_back(',');
            outStr.push_back(' ');
        }
        outStr.push_back(outSeq[i]);
    }
    outStr.push_back(']');

    //std::cout<<outStr<<std::endl;
    //[]
    return (outStr);
}

int main(int argc, char *argv[])
{
    #ifdef TEST
        std::cout << "Magica splitting---> Test mode"<<std::endl;
    #endif


    char inBuff[1024];

    //std::ifstream file("bsmall.in");

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

        std::cout<<"Case #"<<(i+1)<<": ";

        std::vector<char> outStr = CastMagic(inBuff);
        for(int j = 0; j < outStr.size(); j++)
        {
            std::cout<<outStr[j];
        }
        std::cout<<std::endl;

    }

    return (0);
}
