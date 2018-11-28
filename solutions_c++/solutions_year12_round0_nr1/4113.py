#include <iostream>
#include <string>
#include <cstdlib>

using namespace std;

int main(int argc, char *argv[])
{
    const char trans[] = "yhesocvxduiglbkrztnwjpfmaq";

    string line;
    getline(cin, line);
    int num = atoi(line.c_str());
    for (int count = 1; count <= num; ++count)
    {
        getline(cin, line);
        cout << "Case #" << count << ": ";
        for (string::iterator it = line.begin(); it != line.end(); ++it)
        {
            if (*it != ' ')
                cout << trans[*it - 'a'];
            else
                cout << ' ';
        }
        cout << endl;
    }
    return 0;
}
