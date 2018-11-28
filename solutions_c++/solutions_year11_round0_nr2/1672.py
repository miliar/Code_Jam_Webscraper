#include <string>
#include <map>
#include <iostream>
#include <sstream>

using namespace std;

typedef map<char, string> OppositeMap;
typedef map<string, char> CombinationMap;

string RunTestCase(const CombinationMap& combo_map, const OppositeMap& opp_map, const string& invoked) {
    string element_list;
    for (size_t i = 0; i < invoked.size(); ++i) {
        char next = invoked[i];
        if (!element_list.empty()) {
            CombinationMap::const_iterator combo_itr = combo_map.find(string(1, next) + element_list[element_list.size() - 1]);
            if (combo_itr != combo_map.end()) {
                element_list[element_list.size() - 1] = combo_itr->second;
                continue;
            }
            
            OppositeMap::const_iterator opp_itr = opp_map.find(next);
            if (opp_itr != opp_map.end() && element_list.find_first_of(opp_itr->second) != string::npos) {
                element_list.clear();
                continue;
            }
        }
        
        element_list.push_back(next);
    }
    
    if (element_list.empty())
        return "[]";
    
    stringstream result;
    result << '[' << element_list[0];
    for (size_t i = 1; i < element_list.size(); ++i) {
        result << ", " << element_list[i];
    }
    
    result << ']';
    return result.str();
}

int main(int argc, char** argv) {
    int num_test_cases;
    cin >> num_test_cases;
    
    for (int i = 0; i < num_test_cases; ++i) {
        CombinationMap combo_map;
        int num_combinations;
        cin >> num_combinations;
        
        string combo;
        for (int j = 0; j < num_combinations; ++j) {
            cin >> combo;
            combo_map[string(1, combo[0]) + combo[1]] = combo[2];
            combo_map[string(1, combo[1]) + combo[0]] = combo[2];
        }
        
        OppositeMap opp_map;
        int num_opposites;
        cin >> num_opposites;
        
        string opp_pair;
        for (int j = 0; j < num_opposites; ++j) {
            cin >> opp_pair;
            opp_map[opp_pair[0]].push_back(opp_pair[1]);
            opp_map[opp_pair[1]].push_back(opp_pair[0]);
        }
        
        int garbage;
        string invoked;
        cin >> garbage >> invoked;
        
        cout << "Case #" << (i + 1) << ": " << RunTestCase(combo_map, opp_map, invoked) << endl;
    }
    
    return 0;
}
