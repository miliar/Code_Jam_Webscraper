#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

int main() {
    int cases; cin >> cases;
    string answers[cases];
    cin.clear(); cin.sync();
    for (int t = 0; t < cases; t++) {
        char input[1000];
        cin.getline(input, 1000, '\n');
        stringstream ss (stringstream::in | stringstream::out);
        ss << input;
        int C; ss >> C;
        string combo[C];
        for (int i = 0; i < C; i++) ss >> combo[i];
        int D; ss >> D;
        string oppose[D];
        for (int i = 0; i < D; i++) ss >> oppose[i];
        int N; ss >> N;
        string elements; ss >> elements;
        vector<char> invoke;
        invoke.push_back(elements[0]);
        for (int i = 1; i < elements.length(); i++) {
            char E = elements[i];
            for (int j = 0; j < C; j++) {
                if ((invoke.back() == combo[j][0] && E == combo[j][1]) ||
                    (E == combo[j][0] && invoke.back() == combo[j][1])) {
                    invoke.pop_back();
                    E = combo[j][2];
                    break;
                }
            }
            invoke.push_back(E);
            for (int j = 0; j < D; j++) {
                if (!invoke.empty() && (E == oppose[j][0] || E == oppose[j][1])) {
                    char F = E == oppose[j][0] ? oppose[j][1] : oppose[j][0];
                    for (int k = 0; k < invoke.size()-1; k++) {
                        if (invoke[k] == F) {
                            invoke.clear();
                            break;
                        }
                    }
                }
            }
        }
        answers[t] += "[";
        if (invoke.size() > 0) {
            for (int i = 0; i < invoke.size(); i++) {
                answers[t] += invoke[i];
                if (i < invoke.size()-1) answers[t] += ", ";
            }
        }
        answers[t] += "]";
    }

    for (int t = 0; t < cases; t++)
        cout << "Case #" << t+1 << ": " << answers[t] << endl;
    return 0;
    //I freaking love Magicka <3
}
