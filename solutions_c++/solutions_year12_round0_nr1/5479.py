#include <iostream>
#include <fstream>
#include <string>
#include <cstdio>

using namespace std;

ifstream fin("example.in");
ifstream Fin("probA.in");
ofstream fout("answer.out");

int map[26];
string str[1000];

int main()
{
    string a1, a2, a3, b1, b2, b3;
    getline(fin, a1);
    getline(fin, a2);
    getline(fin, a3);

    getline(fin, b1);
    getline(fin, b2);
    getline(fin, b3);
    b1 = b1.substr(9);
    b2 = b2.substr(9);
    b3 = b3.substr(9);

    for (size_t i = 0; i < a1.size(); ++i) {
        map[a1[i] - 'a'] = b1[i];
    }
    for (size_t i = 0; i < a1.size(); ++i) {
        map[a2[i] - 'a'] = b2[i];
    }
    for (size_t i = 0; i < a1.size(); ++i) {
        map[a3[i] - 'a'] = b3[i];
    }

    for (size_t i = 0; i < 26; ++i)
        if (map[i])
            cout << (char)map[i];
        else {
            cout << 'X';
        }
    map['z' - 'a'] = 'q';
    map['q' - 'a'] = 'z';
    cout << endl;

    int n;
    Fin >> n;
    getline(Fin, str[0]);

    for (int i = 0; i < n; ++i) {
        getline(Fin, str[i]);
        for (size_t j = 0; j < str[i].size(); ++j)
            str[i][j] = map[str[i][j] - 'a'];
        cout << str[i] << endl;
        fout << "Case #" << i+1 << ": " << str[i] << endl;
    }

    return 0;
}
