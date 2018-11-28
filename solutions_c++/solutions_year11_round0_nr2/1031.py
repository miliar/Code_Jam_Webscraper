#include <iostream>
#include <vector>
#include <string>
#include <list>
#include <cassert>

using namespace std;

const int kAlphaLength = 26;
int combine[kAlphaLength][kAlphaLength];
bool opposed[kAlphaLength][kAlphaLength];

int symbolIndex(char c) {
    return c - 'A';
}

char symbol(int index) { 
    return 'A' + index;
}

void readInstance(string* elements) {
    for(int i = 0; i < kAlphaLength; ++i) {
        for(int j = 0; j < kAlphaLength; ++j) {
            combine[i][j] = -1;
            opposed[i][j] = false;
        }
    }

    int combinations;
    cin >> combinations;

    for(int i = 0; i < combinations; ++i) {
        string rule;
        cin >> rule;
        combine[symbolIndex(rule[0])][symbolIndex(rule[1])] = symbolIndex(rule[2]);
        combine[symbolIndex(rule[1])][symbolIndex(rule[0])] = symbolIndex(rule[2]);
    }

    int oppositions;
    cin >> oppositions;

    for(int i = 0; i < oppositions; ++i) {
        string rule;
        cin >> rule;
        opposed[symbolIndex(rule[0])][symbolIndex(rule[1])] = true;
        opposed[symbolIndex(rule[1])][symbolIndex(rule[0])] = true;
    }

    int len;
    cin >> len;

    cin >> *elements;

    assert(len == elements->length());
}

list<int> processElements(const string& elements) {
    list<int> result;
    vector<int> counts(kAlphaLength, 0);

    for(int i = 0; i < elements.length(); ++i) {
        int currentIndex = symbolIndex(elements[i]);

        if(result.empty()) {
            result.push_back(currentIndex);
            ++counts[currentIndex];
        } else {
            int lastIndex = result.back();
            if(combine[currentIndex][lastIndex] != -1) {
                result.pop_back();
                --counts[lastIndex];
                result.push_back(combine[currentIndex][lastIndex]);
                ++counts[combine[currentIndex][lastIndex]];
            } else {
                bool cleared = false;
                for(int j = 0; j < kAlphaLength; ++j) {
                    if(counts[j] > 0 && opposed[currentIndex][j]) {
                        result.clear();
                        counts.assign(kAlphaLength, 0);
                        cleared = true;
                        break;
                    }
                }
                if(!cleared) {
                    result.push_back(currentIndex);
                    ++counts[currentIndex];
                }
            }
        }
    }
    return result;
}

void outputList(int caseNo, const list<int>& elements) {
    cout << "Case #" << caseNo << ": [";
    for(list<int>::const_iterator i = elements.begin(); i != elements.end(); ++i) {
        if(i != elements.begin()) {
            cout << ", ";
        }
        cout << symbol(*i);
    }
    cout << "]" << endl;
}

int main() {
    int instances;
    cin >> instances;

    for(int i = 0; i < instances; ++i) {
        string r;
        readInstance(&r);
        outputList(i + 1, processElements(r));
    }
    return 0;
}

