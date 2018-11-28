#include <iostream>
using namespace std;

string r = "yhesocvxduiglbkrztnwjpfmaq";

int main() {
    int n;
    cin >> n;
    cin.ignore();
    for (int i = 0; i < n; ++i) {
        string s;
        getline(cin, s);
        for (int j = 0; j < s.size(); ++j) if (isalpha(s[j])) s[j] = r[s[j] - 'a'];
        cout << "Case #" << i + 1 << ": " << s << endl;
    }
}