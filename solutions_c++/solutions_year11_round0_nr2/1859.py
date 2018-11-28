#include <iostream>
#include <list>
#include <map>
#include <string>

using namespace std;

map<char, map<char, char> > comboMap;
map<char, map<char, bool> > oppMap;

bool contains_opposing(const list<char>& elementList, char e1);
char combine(char e1, char e2);
list<char> invoke(list<char> invokeList);
string printElementList(const list<char>& elementList);

bool contains_opposing(const list<char>& elementList, char e1) {
    for (list<char>::const_iterator i = elementList.begin(); i != elementList.end(); i++) {
        char e2 = *i;

        if (oppMap[e1][e2] == true || oppMap[e2][e1] == true) {
            return true;
        }
    }

    return false;
}

char combine(char e1, char e2) {
    char combo = comboMap[e1][e2];

    if (combo == 0) {
        return comboMap[e2][e1];
    } else {
        return combo;
    }
}

list<char> invoke(list<char> invokeList) {
    list<char> elementList;

    while (!invokeList.empty()) {
        char e1 = invokeList.front();
        invokeList.pop_front();

        if (contains_opposing(elementList, e1)) {
            elementList.clear();
        } else if (!invokeList.empty()) {
            char e2 = invokeList.front();
            char combo = combine(e1, e2);

            if (combo != 0) {
                invokeList.pop_front();
                elementList.push_back(combo);
            } else {
                elementList.push_back(e1);
            }
        } else {
            elementList.push_back(e1);
        }
    }

    return elementList;
}

string printElementList(const list<char>& elementList) {
    string result = "";

    result += "[";
    for (list<char>::const_iterator i = elementList.begin(); i != elementList.end(); i++) {
        char e1 = *i;
        if (i != elementList.begin()) {
            result += ", ";
        }
        result += e1;
    }

    result += "]";

    return result;
}


int main(int argc, const char *argv[])
{
    int T = 0;
    cin >> T;

    for (int numCases = 0; numCases < T; numCases++) {
        comboMap.clear();
        oppMap.clear();

        int C = 0;
        cin >> C;

        for (int numCombos = 0; numCombos < C; numCombos++) {
            string comboList;
            cin >> comboList;

            comboMap[comboList[0]][comboList[1]] = comboList[2];
        }

        int D = 0;
        cin >> D;

        for (int numOpp = 0; numOpp < D; numOpp++) {
            string oppList;
            cin >> oppList;

            oppMap[oppList[0]][oppList[1]] = true;
        }

        int N = 0;
        cin >> N;

        list<char> invokeList;
        for (int numElements = 0; numElements < N; numElements++) {
            char e = 0;
            cin >> e;
            invokeList.push_back(e);
        }

        list<char> elementList = invoke(invokeList);
        cout << "Case #" << numCases+1 << ": " << printElementList(elementList) << endl;
    }

    return 0;
}
