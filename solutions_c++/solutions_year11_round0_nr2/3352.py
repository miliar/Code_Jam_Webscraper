#include <iostream>
#include <list>
#include <vector>
#include <string>
#include <map>
#include <sstream>
#include <algorithm>
using namespace std;


int main(int argc, char* argv[])
{
	string line;
	int T;
	cin >> T;
	getline(cin, line);

	for (int t=0; t < T; t++) {
		cout << "Case #" << (t+1) << ": ";


        map<char, map<char, char> > combine;
        map<char, map<char, char> > oppose;

        list<char> invoked;
        list<char> toInvoke;



        // Load
        int C, D, N;

        cin >> C;
        for (int c=0; c < C; c++) {
            string str;
            cin >> str;
            combine[str[0]][str[1]] = str[2];
            combine[str[1]][str[0]] = str[2];
        }

        cin >> D;
        for (int d=0; d < D; d++) {
            string str;
            cin >> str;
            oppose[str[0]][str[1]] = 1;
            oppose[str[1]][str[0]] = 1;
        }

        cin >> N;
        string str;
        cin >> str;
        string::iterator i;
        for (i=str.begin(); i != str.end(); ++i) {
            toInvoke.push_back(*i);
        }

        // Process
        while (toInvoke.size()) {

            char base = toInvoke.front();
            toInvoke.pop_front();

            if (invoked.size()) {

                // Check for combine
                char combined = combine[invoked.back()][base];
                if (combined) {
                    invoked.pop_back();
                    invoked.push_back(combined);

                // Check for oppose
                } else {
                    list<char>::iterator i;
                    bool cleared = false;
                    for (i=invoked.begin(); i != invoked.end(); ++i) {
                        if ((base != *i) && (oppose[base][*i])) {
                            cleared = true;
                            invoked.clear();
                            break;
                        }
                    }

                    if (!cleared) {
                        invoked.push_back(base);
                    }
                }

            } else {
                invoked.push_back(base);
            }
        }


        // Print out
        list<char>::iterator j;
        bool first = true;
        cout << "[";
        for (j = invoked.begin(); j != invoked.end(); ++j) {
            if (!first) {
                cout << ", ";
            }
            first = false;

            cout << *j;
        }		
        cout << "]" << endl;
	}


    return 0;
}


