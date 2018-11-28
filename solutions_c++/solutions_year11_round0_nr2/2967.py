#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <iostream>
#include <algorithm>
#include <fstream>

#include "Utilities.h"
#include "PrimeManager.h"

using namespace std;

int main()
{
    int cases;

    ifstream inputFileStream("G:\\GoogleCodeJam\\B-large.in");
    ofstream ouputFileStream("G:\\GoogleCodeJam\\B-large.out");

    while (inputFileStream >> cases)
    {
        for (int c = 0;c < cases;c++)
        {
			map<pair<char, char>, char> combinedMap;
			map<pair<char, char>, bool> opposedMap;

			int combinedCount, opposedCount;
	
			inputFileStream >> combinedCount;

			for (int i = 0;i < combinedCount;i++)
			{
				string tempInput;			

				inputFileStream >> tempInput;

				combinedMap[make_pair(tempInput[0], tempInput[1])] = tempInput[2];
			}

			inputFileStream >> opposedCount;

			for (int i = 0;i < opposedCount;i++)
			{
				string tempInput;			

				inputFileStream >> tempInput;

				opposedMap[make_pair(tempInput[0], tempInput[1])] = true;
			}

			//Main algo.
			int stringLength;
			string targetStr;
			string result = "";

			inputFileStream >> stringLength >> targetStr;

			for (int i = 0;i < targetStr.length();i++)
			{				
				if (result.length() == 0)
				{
					result += targetStr[i];
				}
				else
				{
					pair<char, char> pattern1 = make_pair(targetStr[i], result[result.length() - 1]);
					pair<char, char> pattern2 = make_pair(result[result.length() - 1], targetStr[i]);

					map<pair<char, char>, char>::iterator itr = combinedMap.find(pattern1);
					map<pair<char, char>, char>::iterator itr2 = combinedMap.find(pattern2);

					if (itr != combinedMap.end())
					{
						result[result.length() - 1] = (*itr).second;
					}
					else if (itr2 != combinedMap.end())
					{
						result[result.length() - 1] = (*itr2).second;
					}
					else
					{
						bool found = false;

						for (int j = result.length() - 1;j >= 0;j--)
						//for (int j = 0;j < result.length();j++)
						{	
							pair<char, char> opposedPattern1 = make_pair(targetStr[i], result[j]);
							pair<char, char> opposedPattern2 = make_pair(result[j], targetStr[i]);

							map<pair<char, char>, bool>::iterator opposedItr = opposedMap.find(opposedPattern1);
							map<pair<char, char>, bool>::iterator opposedItr2 = opposedMap.find(opposedPattern2);

							if (opposedItr != opposedMap.end() || opposedItr2 != opposedMap.end())
							{
								//result.erase(j);
								result.clear();
								found = true;
								break;
							}
						}
			
						if (!found)
						{
							result += targetStr[i];
						}
					}
				}
			}
			

            //Output
            ouputFileStream << "Case #" << (c + 1) << ": [";

			for (int i = 0;i < result.length();i++)
			{
				if (i == result.length() - 1) 
				{
					ouputFileStream << result[i];
				}
				else
				{
					ouputFileStream << result[i] << ", ";
				}
			}

			ouputFileStream << "]" << endl;
        }
    }

    return 0;
}