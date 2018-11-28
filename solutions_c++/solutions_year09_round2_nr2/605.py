#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <cstring>
#include <algorithm>

using namespace std;

void solve(int);

int main()
{
    int total_cases;
    cin >> total_cases;
    cin.get();

    for (int i = 0; i < total_cases; i++)
        solve(i+1);

    return 0;
}

void solve(int ncase)
{
    string line;
    cin >> line;

    vector <char> numbers;
    map <char, int> exists;
    for (int i = 0; i < line.size(); i++) {
        if (!exists[line[i]]) numbers.push_back(line[i]);
        exists[line[i]]++;
    }
    sort(numbers.begin(), numbers.end());

    cout << "Case #" << ncase << ": ";
/*
    for (int i = 0; i < numbers.size(); i++) {
        char n = numbers[i];
        line.rfind()
    }
*/
    for (int i = line.size()-2; i >= 0; i--) {
        //cout << "Checking "<< i << "-th pos" << endl;
        for (int k = 0; k < numbers.size(); k++) if (numbers[k] > line[i]) {
            size_t pos = line.substr(i+1).find(numbers[k]);
            if (pos != string::npos) {
                pos = pos + i + 1;
                //cout << numbers[k] << '\t' << pos << endl;
                //pos = pos + i + 1;
                string temp = line.substr(i, pos-i) + line.substr(pos+1);
                sort(temp.begin(), temp.end());
                line = line.substr(0, i) + numbers[k] + temp;
                cout << line << endl;
                return;
            }
        }
        /*
        for (int j = i; j < line.size(); j++) {
            if (line[i] < line[j]) {
                line = line.substr(0, i) + line[j] + line.substr(i, j-i);
                cout << line << endl;
                return;
            }
        }
        */
    }

    char smallest = numbers[0] == '0' ? numbers[1] : numbers[0];
    cout << smallest;
    exists[smallest]--;
    exists['0']++;
    for (char c = '0'; c <= '9'; c++) if (exists[c]) {
        for (int i = 0; i < exists[c]; i++) cout << c;
    }
    cout << endl;
}
