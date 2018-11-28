#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main(int argc, char *argv[])
{
    string trad = "yhesocvxduiglbkrztnwjpfmaq";
    int T;
	cin >> T;
	string nextline;
	getline(cin, nextline);
    for (int caso = 1; caso <= T; ++caso) {
		string input;
        getline(cin, input);
        string sol(input.size(), 'a');
        for (int i = 0; i < input.size(); ++i) {
            if (input[i] == ' ') sol[i] = ' ';
            else sol[i] = trad[input[i] - 'a'];
        }
        cout << "Case #" << caso << ": " << sol<< endl;
    }
    
}
