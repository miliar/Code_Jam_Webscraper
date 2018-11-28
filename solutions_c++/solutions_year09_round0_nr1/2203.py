#include <iostream>
#include <vector>
#include <set>
using namespace std;
typedef set<char> VC;
typedef vector<VC> VVC;
int solve(vector<string> dict, string str) {
    VVC vvc;
    for (size_t i=0; i<str.size(); i++) {
        VC node;
        if (str[i]=='(') {
            for (i=i+1;i<str.size();i++) {
                if (str[i]==')') {
                    break;
                } else {
                    node.insert(str[i]);
                }
            }
        } else {
            node.insert(str[i]);
        }
        vvc.push_back(node);
    }
    vector<bool> death(dict.size(), false);
    for (size_t i=0; i<vvc.size(); i++) {
        for (size_t j=0; j<dict.size(); j++) {
            if (death[j]) continue;
            if (vvc[i].find( dict[j][i] ) == vvc[i].end()) {
                death[j] = true;
            }
        }
    }
    int cnt = 0;
    for (size_t i=0; i<death.size(); i++)
        if (!death[i])
            cnt++;
    return cnt;
}
int main () {
    int L, D, N;
    cin >> L >> D >> N;
    cin.ignore();
    vector<string> dict;
    vector<string> testcase;
    string line;
    for (int i=0; i<D; i++) {
        getline(cin,line);
        dict.push_back(line);
    }
    for (int i=0; i<N; i++) {
        getline(cin,line);
        testcase.push_back(line);
    }
    // for each testcase
    for (int i=0; i<N; i++) {
        string input = testcase[i];
        printf("Case #%d: ", i+1);
        cout << solve(dict, input) << endl;
    }
}
