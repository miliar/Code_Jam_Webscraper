#include <iostream>
#include <map>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
#include <cstdlib>
#include <cstring>

using namespace std;

typedef map<char, map<char, char> > comboMap;
typedef map<char, vector<char> > oppMap;

string doLine(const string &line);
stack<char> doMagic(int n, const string &str, const comboMap &combos, const oppMap &opposites);
char getCombo(const comboMap &combos, char first, char second);
vector<string> &split(const string &s, char delim, vector<string> &elems);
vector<string> split(const string &s, char delim);

const char NO_COMBO = '\0';

int main() {
    string first;
    getline(cin, first);
    int n = atoi(first.c_str());
    for (int i = 0; i < n; ++i) {
        string line;
        getline(cin, line);
        string answer = doLine(line);
        cout << "Case #" << (i + 1) << ": " << answer << endl;
    }
    return 0;
}

string doLine(const string &line) {
    vector<string> tokens;
    split(line, ' ', tokens);

    int numCombos = atoi(tokens[0].c_str());
    comboMap combos;
    for (int i = 0; i < numCombos; ++i) {
        const char* combo = tokens[i + 1].c_str();
        char first = combo[0];
        char second = combo[1];
        char result = combo[2];
        combos[first][second] = result;
        combos[second][first] = result;
    }

    int numOpps = atoi(tokens[numCombos + 1].c_str());
    oppMap opposites;
    for (int j = 0; j < numOpps; ++j) {
        int i = numCombos + 2 + j;
        const char* opp = tokens[i].c_str();
        char first = opp[0];
        char second = opp[1];
        opposites[first].push_back(second);
        opposites[second].push_back(first);
    }

    int numElements = atoi(tokens[numCombos + numOpps + 2].c_str());
    string elements = tokens[numCombos + numOpps + 3];
    stack<char> result = doMagic(numElements, elements, combos, opposites);
    stack<char> reverse;

    while (!result.empty()) {
        reverse.push(result.top());
        result.pop();
    }
    string answer("[");
    int size = reverse.size();
    for (int i = 0; i < size; ++i) {
        answer.push_back(reverse.top());
        if (i != size - 1) {
            answer.append(", ");
        }
        reverse.pop();
    }
    answer.push_back(']');

    return answer;
}

stack<char> doMagic(int n, const string &str, const comboMap &combos, const oppMap &opposites) {
    stack<char> stack;
    map<char, int> counts;
    const char* elements = str.c_str();

    for (int i = 0; i < n; ++i) {
        char current = elements[i];
        bool haveCombo = false;

        // Have to check for combinations.
        if (!stack.empty()) {
            // Process combinations.
            char combo = getCombo(combos, current, stack.top());
            while (combo != NO_COMBO) {
                haveCombo = true;
                --counts[stack.top()];
                stack.pop();
                current = combo;
                combo = stack.empty() ? NO_COMBO : getCombo(combos, current, stack.top());
            }
        }

        // No more combos. Can finally add!
        stack.push(current);
        ++counts[current];

        // No combos: check for opposition
        if (!haveCombo) {
            oppMap::const_iterator it = opposites.find(current);
            if (it != opposites.end()) {
                vector<char> oppVector = it->second;
                vector<char>::iterator it2;
                for (it2 = oppVector.begin(); it2 != oppVector.end(); ++it2) {
                    char opposite = *it2;
                    if (counts[opposite] > 0) {
                        // Found an opposite. Dump everything!!!
                        while (!stack.empty()) {
                            stack.pop();
                        }
                        counts.clear();
                        break;
                    }
                }
            }
        }
    }

    return stack;
}

char getCombo(const comboMap &combos, char first, char second) {
    comboMap::const_iterator it = combos.find(first);

    if (it == combos.end()) {
        return NO_COMBO;
    }

    map<char, char> inner = it->second;
    map<char, char>::const_iterator it2 = inner.find(second);

    if (it2 == inner.end()) {
        return NO_COMBO;
    }

    return it2->second;
}

// http://stackoverflow.com/questions/236129/c-how-to-split-a-string
vector<string> &split(const string &s, char delim, vector<string> &elems) {
    stringstream ss(s);
    string item;
    while(getline(ss, item, delim)) {
        elems.push_back(item);
    }
    return elems;
}

vector<string> split(const string &s, char delim) {
    vector<string> elems;
    return split(s, delim, elems);
}
