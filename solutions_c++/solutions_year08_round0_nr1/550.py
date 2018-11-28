#include <set>
#include <fstream>
#include <string>

int main()
{
    ::std::ifstream inputFileStream("input.txt");
    ::std::ofstream outputFileStream("output.txt");
    ::std::string line;
    unsigned int numberOfCases;
    inputFileStream >> numberOfCases;

    for (unsigned int caseIndex = 1; caseIndex <= numberOfCases; ++caseIndex)
    {
        unsigned int numberOfEngines;
        inputFileStream >> numberOfEngines;
        ::std::getline(inputFileStream, line);
        ::std::set< ::std::string > engines;
        for (unsigned int engineIndex = 0; engineIndex < numberOfEngines; ++engineIndex)
        {
            ::std::getline(inputFileStream, line);
            engines.insert(line);
        }

        unsigned int numberOfQueries;
        unsigned int switchsNeededCount = 0;
        inputFileStream >> numberOfQueries;
        ::std::getline(inputFileStream, line);
        ::std::set< ::std::string > alreadyUsedEngines;
        while (numberOfQueries > 0)
        {
            ::std::getline(inputFileStream, line);
            --numberOfQueries;
            if (engines.count(line) == 1)
            {
                alreadyUsedEngines.insert(line);
                if (alreadyUsedEngines.size() == numberOfEngines)
                {
                    ++switchsNeededCount;
                    alreadyUsedEngines.clear();
                    alreadyUsedEngines.insert(line);
                }
            }
        }
        outputFileStream << "Case #" << caseIndex << ": " << switchsNeededCount << ::std::endl;
   }
   return 0;
}