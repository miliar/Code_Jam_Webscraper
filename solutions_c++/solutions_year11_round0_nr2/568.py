#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <iterator>
#include <utility>



int main() {
    std::ifstream input("test.in");
    std::ofstream output("test.out");

    int numTests;
    input >> numTests;
    for (int testIdx = 1; testIdx <= numTests; ++testIdx) {

        std::map<std::pair<char, char>, char> combs;
        std::set< std::pair<char, char> > opps;

        int numCombines;
        input >> numCombines;
        for (int i = 0; i < numCombines; ++i) {
            std::string comb;
            input >> comb;
            combs[std::make_pair(comb[0], comb[1])] = comb[2];
            combs[std::make_pair(comb[1], comb[0])] = comb[2];
        }
        
        int numOpposite;
        input >> numOpposite;
        for (int i = 0; i < numOpposite; ++i) {
            std::string opp;
            input >> opp;
            opps.insert(std::make_pair(opp[0], opp[1]));
            opps.insert(std::make_pair(opp[1], opp[0]));
        }

        int seqLength;
        input >> seqLength;
        std::string seq;
        input >> seq;
        std::vector<char> list;
        for (int i = 0; i < seq.length(); ++i) {
            if (list.empty()) {
                list.push_back(seq[i]);
                continue;
            }
            std::pair<char, char> pair = std::make_pair(list.back(), seq[i]);
            if (combs.find(pair) != combs.end()) {
                list.pop_back();
                list.push_back(combs[pair]);
            } else {
                bool clearFlag = false;
                for (int j = 0; j < list.size(); ++j) {
                    if (opps.find(std::make_pair(list[j], seq[i])) != opps.end()) {
                        list.clear();
                        clearFlag = true;
                        break;
                    }
                }

                if (!clearFlag) {
                    list.push_back(seq[i]);
                }
            }
        }

        std::string listStr;
        for (int i = 0; i < list.size(); ++i) {
            if (i > 0) {
                listStr += ", ";
            }
            listStr += list[i];
        }
        listStr = std::string("[") + listStr + "]";
       

        output << "Case #" << testIdx << ": " << listStr << std::endl;
    }

    input.close();
    output.close();

    return 0;
}