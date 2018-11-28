#include <iostream>
#include <map>
#include <vector>
#include <string>

using namespace std;

string word;
string code;
vector<string> dict;

bool can_solve(int wi, int ci) {
    if (ci >= code.size() || wi >= word.size()  ) return true;
    if (code[ci] == '(') {
        int i;
        for (i = ci+1; code[i] != ')' && code[i] != word[wi]; i++) ;
        if (code[i] == ')') return false;
        for (; code[i] != ')'; i++);i++;
        return can_solve (++wi,i);
    } else if (code[ci] == word[wi]){
        return can_solve (++wi,++ci);
    } else
        return false;
}


int main () {
    int L, D, N;
    cin >> L >> D >> N;
    for (int i = 0; i < D; i++) {
        string w;
        cin >> w;
        dict.push_back (w);
    }
    int cnt = 1;
    while (N--) {
        cin >> code;
        int count = 0;
        for (int i = 0; i < dict.size(); i++) {
            word = dict[i];
            if (can_solve (0,0)) count++;
        }
        cout << "Case #" << cnt++ << ": " << count << endl;
    }
    return 0;
}



