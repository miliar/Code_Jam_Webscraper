
#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <vector>

using std::cout;
using std::endl;
using std::map;
using std::pair;
using std::string;
using std::vector;

typedef map<string,char> CombineRules;
typedef map<char,char> OpposeRules;

struct Ruleset {
    CombineRules combine;
    OpposeRules oppose;
    string invokes;
};

vector<Ruleset> ParseInput(const string& filename) {

    vector<Ruleset> rulesets;

    std::ifstream fin;
    fin.open(filename.c_str(), std::ifstream::in);
    if (fin.fail()) {
        cout << "Failed to open " << filename << endl;
        return rulesets;
    }

    int num_rulesets;
    fin >> num_rulesets;
    for (int i = 0; i < num_rulesets; ++i) {
        Ruleset ruleset;
        int num_combine_rules;
        fin >> num_combine_rules;
        for (int j = 0; j < num_combine_rules; ++j) {
            string rule;
            fin >> rule;
            // assert rule.size() == 3?
            string base = rule.substr(0,2);
            ruleset.combine[base] = rule[2];
            std::swap(base[0],base[1]);
            ruleset.combine[base] = rule[2];
        }
        int num_oppose_rules;
        fin >> num_oppose_rules;
        for (int j = 0; j < num_oppose_rules; ++j) {
            string rule;
            fin >> rule;
            // assert rule.size() == 2?
            ruleset.oppose[rule[0]] = rule[1];
            ruleset.oppose[rule[1]] = rule[0];
        }
        int num_invokes;
        fin >> num_invokes;
        fin >> ruleset.invokes;
        rulesets.push_back(ruleset);
    }

    fin.close();

    return rulesets;
}

string ApplyRuleset(Ruleset ruleset) {
    string element_list;

    int num_invokes = ruleset.invokes.size();

    for (int i = 0; i < num_invokes; ++i) {

        element_list.push_back(ruleset.invokes[i]);
        if (element_list.size() >= 2) {
            string base = element_list.substr(element_list.size()-2,2);
            if (ruleset.combine.find(base) != ruleset.combine.end()) { // found a comebinable case
                element_list.erase(element_list.size()-2,2);
                element_list.push_back(ruleset.combine[base]);
                continue;
            }

            // in fact, if combine happens, the following steps should not happen because non-base element would not be opposing to anything
            char last_element = element_list[element_list.size()-1];
            int num_elements = element_list.size();
            for (int j = 0; j < num_elements; ++j) {
                if (ruleset.oppose.find(element_list[j]) != ruleset.oppose.end()) {
                    if (ruleset.oppose[element_list[j]] == last_element) {
                        element_list.clear();
                        break;
                    }
                }
            }
        }
    }

    return element_list;
}

int main(int argc, char** argv) {

    vector<Ruleset> rulesets = ParseInput(string(argv[1]));

    std::ofstream fout;
    fout.open("output.txt",std::ofstream::out);
    if (fout.fail()) {
        cout << "Failed to open output.txt for writing." << endl;
        return 1;
    }

    int num_rulesets = rulesets.size();
    for (int i = 0; i < num_rulesets; ++i) {
        string element_list = ApplyRuleset(rulesets[i]);
        fout << "Case #" << i+1 << ": [";
        int num_elements = element_list.size();
        for (int j = 0; j < num_elements; ++j) {
            fout << element_list[j];
            if (j == num_elements-1)
                break;
            fout << ", ";
        }
        fout << "]" << endl;
    }

    fout.close();

    return 0;
}
