#include <iostream>
#include <string>
#include <map>

using namespace std;

int main() {

    string keys = "ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjvqz ";
    string vals = "ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveupzq ";
    int kLen = keys.length();

    map<char, char> dict;

    for (int i=0; i<kLen; ++i) {
        dict[keys[i]] = vals[i];
    }

/*
    for (map<char, char>::iterator it = dict.begin(); it != dict.end(); ++it) {
        cout << it->first << " = " << it->second << endl;
    }
    cout << dict.size() << endl;
    */

    int testCases;
    cin >> testCases;

    string garbage;
    getline(cin, garbage);

    for (int i=0; i<testCases; ++i) {
        string str;

        getline(cin, str);

        cout << "Case #" << i+1 << ": ";
        int strLen = str.length();
        for (int k=0; k<strLen; ++k) {
            cout << dict[str[k]];
        }
        cout << endl;
    }

    return 0;
}
