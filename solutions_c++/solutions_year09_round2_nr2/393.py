#include <iostream>
#include <vector>

using namespace std;


string np(string a) {
        next_permutation(a.begin(), a.end());
        return a;
}

bool lt(string a, string b) {
    int ap=0;
    while(ap <a.size()) {
        if (a[ap] != b[ap]) return a[ap] < b[ap];
        ap++;
    }
    return false;
}

int main() {
    int cases;
    cin >> cases;

    for(int c=0; c<cases; c++) {
        string line1;
        cin >> line1;
        string line = np(line1);

        string ans=line;
        if (lt(line, line1) || line == line1) {
            //if (line[0] == '0') {
                string zeros, other;
                for(int i=0; i<line.size(); i++) {
                    if (line[i] == '0') zeros += line.substr(i,1);
                    else other += line.substr(i,1);
                }
                sort(other.begin(), other.end());
                ans= other.substr(0,1) + "0" + zeros + other.substr(1);
            //}
            //else ans = line.substr(0,1) + "0" + line.substr(1);
        }

        cout << "Case #" <<(c+1) << ": " << ans << endl;
    }
}
