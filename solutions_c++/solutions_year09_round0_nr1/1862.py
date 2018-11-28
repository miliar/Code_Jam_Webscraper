#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int binsearch(vector<string> *vec, string *tar) {
    int lowbound = 0, upbound = vec->size();
    int cur = upbound / 2;
    while (((*vec)[cur].substr(0, tar->size())) != *tar && upbound != lowbound) {
        if ((*vec)[cur] < *tar) {
            lowbound = cur + 1;
            cur = (upbound + cur) / 2;
        }
        else {
            upbound = cur;
            cur = (lowbound + cur) / 2;
        }
    }
    return upbound != lowbound;
}

void addletters(vector<string> *dict, vector<string> *words, vector<char> *letters) {
    if (!words->size()) {
        for (int i = 0; i < letters->size(); i++) {
            if (binsearch(dict, new string(1, (*letters)[i])))
               words->push_back(string(1, (*letters)[i]));
        }
        return;
    }

    int size = words->size();

    for (int i = 0; i < size; i++) {
        for (int j = 0; j < letters->size(); j++) {
            string temp = (*words)[i];
            temp += string(1, (*letters)[j]);
            if (binsearch(dict, &temp))
               words->push_back(temp);
        }
    }

    words->erase(words->begin(), words->begin() + size);
}

int main() {
    
    int wordlen, dictlen, numwords;
    string temp;
    cin >> wordlen >> dictlen >> numwords;
    vector<string> dict;

    for (int i = 0; i < dictlen; i++) {
        cin >> temp;
        dict.push_back(temp);
    }
    sort(dict.begin(), dict.end());

    vector<string> perms;
    for (int i = 0; i < numwords; i++) {
        cin >> temp;
        int letindex = 0;
        for (int j = 0; j < wordlen; j++) {
            vector<char> lets;
            if (temp[letindex] == '(') {
                while (temp[++letindex] != ')')
                    lets.push_back(temp[letindex]);
            } 
            else 
                lets.push_back(temp[letindex]);
            addletters(&dict, &perms, &lets);
            if (!perms.size())
               break;
            letindex++;
        }
         
        cout << "Case #" << i + 1 << ": " << perms.size() << endl;
        perms.clear();
    }

    return 0;
}

