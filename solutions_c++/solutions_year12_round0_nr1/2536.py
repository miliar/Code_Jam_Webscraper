#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    cin.ignore(100, '\n');
    char G[200];
    char translate[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
    for (int t = 1; t <= T; ++t) {
        cin.getline(G, 200);
        cout << "Case #" << t << ": ";
        int L = strlen(G);
        for (int g = 0; g < L; g++) {
            if (G[g] == ' ') {
                cout << ' ';
            }
            else {
                cout << translate[G[g]-'a'];
            }
        }
        cout << endl;
    }
}