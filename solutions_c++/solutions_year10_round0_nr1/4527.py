#include <iostream>
#include <list>
#include <cmath>
#include <cstring>
#include <fstream>
#include <cstdlib>
#include <vector>

enum STATE{OFF, ON};

const long unsigned int STREAMSIZE = 48*1024;

void calcStartingONSnap(long double& startingONSnap, const long double& N)
{   for(long double n = 0; n < N; ++n)
        startingONSnap += std::pow((long double)2, n);
}

STATE isLightOn(const long double& N, const long double& K)
{   long double startingONSnap = 0;
    calcStartingONSnap(startingONSnap, N);

    if(K == startingONSnap)
        return ON;
    else
    {   if(K < startingONSnap)
            return OFF;
        else
        {   long double addFactor = std::pow((long double)2, N);

            while(startingONSnap < K)
            {   startingONSnap += addFactor;

                if(startingONSnap == K)
                    return ON;
            }
        }
    }

    return OFF;
}

void getInputs(char* data, std::vector<long double>& inputs)
{   char* input = std::strtok(data, " \n");

    while(input != NULL)
    {   inputs.push_back((long double)std::atoi(input));
        input = std::strtok(NULL, " \n");
    }
}

void parseData(char* data, std::vector<long double>& inputs)
{   char* dataPtr = data;

    for(int index = 0; data[index] != '\n'; ++index)
        ++dataPtr;

    ++dataPtr;
    getInputs(dataPtr, inputs);
}

void read(std::vector<long double>& inputs, char* fileName)
{   std::ifstream fIn(fileName);
    char* data = new char[STREAMSIZE];

    while(fIn.good())
    {   fIn.read(data, STREAMSIZE);
        parseData(data, inputs);
    }

    fIn.close();
}

int main()
{   long double N = 1, K = 0;
    std::vector<long double> inputs;
    long double lines = 0;

    // Read input.
    read(inputs, "A-small-attempt1.in");

    // Check if light is on.
    std::ofstream fOut("small_output.txt");
    if(!fOut) std::cerr << "\nCould not open file small_output.txt";
    for(std::vector<long double>::iterator listIter = inputs.begin(); listIter != inputs.end(); ++listIter)
    {   N = *listIter; ++listIter;

        if(listIter != inputs.end())
            K = *listIter;
        else break;

        if(isLightOn(N, K))
            fOut << "\nCase #" << (lines + 1) << ": " << "ON";
        else
            fOut << "\nCase #" << (lines + 1) << ": " << "OFF";

        ++lines;
    }

    return 0;
}
