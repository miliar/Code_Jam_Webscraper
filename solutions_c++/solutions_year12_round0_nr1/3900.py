#include <iostream>

using namespace std;

int main(int argc, const char * argv[])
{
    const string conversion = "yhesocvxduiglbkrztnwjpfmaq";
    int numCases;
    cin >> numCases;
    string input;
    getline(cin, input);
    for (int i = 1; i <= numCases; i++) {
        getline(cin, input);
        cout << "Case #" << i << ": ";
        for (int i = 0; i < input.length(); i++) {
            if (input[i] == ' ') {
                cout << ' ';
            } else {
                int pos = input[i] - 'a';
                if (pos < conversion.length())
                    cout << conversion[pos];
                else {
                    cout << '?';
                }
            }
        }
        cout << endl;
    }
    return 0;
}

