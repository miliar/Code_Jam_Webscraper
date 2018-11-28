#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <algorithm>

#define clear(v) (v.erase(v.begin(), v.end()))

using namespace std;

int T, C, D, N;
vector<string> combine;
vector<string> opposite;
string magic, tmp;

bool hasCombination(char a, char b);
char getCombination(char a, char b);
bool hasOpposite(char a, string str);
bool isOpposite(char a, char b);

int main()
{
    cin >> T;
    for (int i = 1; i <= T; i++) {
        clear(combine);
        clear(opposite);
        cin >> C;
        //cout << "C = " << C << endl;
        for (int j = 0; j < C; j++) {
            cin >> tmp;
            combine.push_back(tmp);
            //cout << tmp << " ";
        }
        //cout << endl;
        cin >> D;
        //cout << "D = " << D << endl;
        for (int j = 0; j < D; j++) {
            cin >> tmp;
            opposite.push_back(tmp);
            //cout << tmp << " ";
        }
        //cout << endl;
        cin >> N;
        cin >> magic;
        //cout << "N = " << N << " magic = " << magic << endl << endl;
        
        
        string ans = "";
        char comb;
        int size;
        for (int j = 0; j < int(magic.length()); j++) {
            ans += magic[j];
            if (ans.length() > 1) {
                size = ans.length();
                if ((comb = getCombination(ans[size - 2], ans[size - 1])) != '\0') {
                    ans = ans.substr(0, size - 2);
                    ans += comb;
                } else {
                    for (int k = size - 2; k >= 0; k--) {
                        if (isOpposite(ans[size - 1], ans[k])) {
                            ans = "";
                        }
                    }
                }
            }
        }
        
        cout << "Case #" << i << ": [";
        for (int j = 0; j < ans.length(); j++) {
            cout << ans[j];
            if (j + 1 < ans.length())
                cout << ", ";
        }
        cout << "]" << endl;
    }
    return 0;
}

char getCombination(char a, char b)
{
    for (int i = 0; i < int(combine.size()); i++)
        if ((combine.at(i)[0] == a && combine.at(i)[1] == b) ||
            (combine.at(i)[0] == b && combine.at(i)[1] == a))
            return combine.at(i)[2];
    return '\0';
}


bool isOpposite(char a, char b)
{
    for (int i = 0; i < int(opposite.size()); i++)
        if ((opposite.at(i)[0] == a && opposite.at(i)[1] == b) ||
            (opposite.at(i)[0] == b && opposite.at(i)[1] == a))
            return true;
    return false;
}
