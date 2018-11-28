#include <iostream>
#include <istream>

using namespace std;

int main()
{
    int T;
    char str[150];
    cin >> T;

    char map[30] = "yhesocvxduiglbkrztnwjpfmaq";
    cin.ignore();
    for (int testcase=1; testcase <= T; ++testcase) {

        cin.getline(str, 150);

        const char *pos = str;


        cout << "Case #" << testcase << ": ";
        while (*pos) {

            if (*pos != ' ')
                cout << map[*pos-'a'];

            else
                cout << *pos;

            pos++;

        }

        cout << endl;

    }
    return 0;
}
