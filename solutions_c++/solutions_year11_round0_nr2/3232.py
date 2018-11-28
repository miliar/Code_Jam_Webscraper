#include <iostream>
#include <map>
#include <string>
#include <list>
#include <algorithm>

int main()
{
    int T;
    std::cin >> T;

    for(int t = 1; t <= T; t++)
    {
        std::map<std::string, std::string> combinations;
        std::list<std::pair<char, char>> oppositions;

        int C;
        std::cin >> C;

        for(int c = 0; c < C; c++)
        {
            std::string comboString;
            std::cin >> comboString;

            std::string baseString = comboString.substr(0, 2);
            std::string nonBaseString = comboString.substr(2, 1);

            combinations[baseString] = nonBaseString;
            std::reverse(baseString.begin(), baseString.end());
            combinations[baseString] = nonBaseString;
        }

        int D;
        std::cin >> D;

        for(int d = 0; d < D; d++)
        {
            std::string oppositionString;
            std::cin >> oppositionString;

            oppositions.push_back(std::pair<char, char>(oppositionString.at(0), oppositionString.at(1)));
        }

        int N;
        std::cin >> N;

        std::string elementList;

        for(int n = 0; n < N; n++)
        {
            char currInvoke;
            std::cin >> currInvoke;

            elementList.append(1, currInvoke);

            int size = elementList.size();
            if(size >= 2)
            {
                std::string e1(1, elementList.at(size-2));
                std::string e2(1, elementList.at(size-1));
                std::string finalTwo = e1 + e2;

                std::map<std::string, std::string>::const_iterator combo = combinations.find(finalTwo);
                if(combo != combinations.end())
                {
                    elementList.replace(size-2, 2, combo->second);
                }

                for(std::list<std::pair<char, char>>::const_iterator oppo = oppositions.begin(); oppo != oppositions.end(); oppo++)
                {
                    if(elementList.find(oppo->first) != std::string::npos && elementList.find(oppo->second) != std::string::npos)
                    {
                        elementList.clear();
                        break;
                    }
                }
            }
        }

        std::cout << "Case #" << t << ": [";
        for(std::string::const_iterator i = elementList.begin(); i != elementList.end(); i++)
        {
            std::cout << *i;

            std::string::const_iterator temp = i;
            temp++;
            if(temp != elementList.end())
            {
                std::cout << ", ";
            }
        }
        std::cout << "]" << std::endl;
    }
}
