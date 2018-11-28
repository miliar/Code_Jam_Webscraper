// Michal Lazowik

#include <iostream>
#include <string>

using namespace std;

int n;
char trans[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
string in;

int main() {
    cin >> n;
    cin.ignore();
    for (int i = 0; i < n; i++) {
        getline(cin, in);
        printf("Case #%d: ", i+1);
        for (int j = 0; j < in.length(); j++)
            cout << ((in[j] == ' ') ? ' ' : trans[in[j]-'a']);
        cout << "\n";
    }

    return 0;
}
