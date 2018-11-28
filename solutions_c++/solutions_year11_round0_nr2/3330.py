#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

string toStr( char c ) {
   return string( 1, c );
}

int main() {
    int cases;
    fstream fin;
    fin.open("input.in");
    ofstream fout;
    fout.open("output.txt");
    fin >> cases;
    for (int counter = 1; counter <= cases; counter++) {
        string help;
        int combinating;
        cout << combinating << " ";
        vector<string> combine;
        vector<string> combine_rezult;
        int oppossing;
        vector<char> oppose1, oppose2;
        fin >> combinating;
        for (int i = 0; i < combinating; i++) {
            fin >> help;
            cout << help << " ";
            string rhcp = toStr(help.at(0));
            rhcp.insert(rhcp.length() - 1, toStr(help.at(1)));
            combine.push_back(rhcp);
            rhcp = toStr(help.at(1));
            rhcp.insert(rhcp.length() - 1, toStr(help.at(0)));
            combine.push_back(rhcp);
            combine_rezult.push_back(toStr(help.at(2)));
            combine_rezult.push_back(toStr(help.at(2)));
        }
        fin >> oppossing;
        cout << oppossing << " ";
        for (int i = 0; i < oppossing; i++) {
            fin >> help;
            cout << help << " ";
            oppose1.push_back(help.at(0));
            oppose1.push_back(help.at(1));
            oppose2.push_back(help.at(1));
            oppose2.push_back(help.at(0));
        }
        int elements_length, ctra = 0;
        fin >> elements_length;
        cout << elements_length << " ";
        string elementsOR, elements;
        fin >> elementsOR;
        cout << elementsOR << endl;
        while (ctra < elements_length) {
            elements.insert(elements.length(), elementsOR.substr(ctra, 1));
            size_t found;
            int i = 0;
            while (i < combinating * 2) {
                found = elements.find(combine.at(i));
                if (found != string::npos) {
                    elements.replace(int(found), 2, combine_rezult.at(i));
                } else {
                    i++;
                }
            }
            i = 0;
            int firstPos, secondPos;
            size_t found2;
            while (i < oppossing * 2) {
                found = elements.find(toStr(oppose1.at(i)));
                if (found != string::npos) {
                    firstPos = int(found);
                    int huah = elements.size();
                    for (int j = firstPos; j < huah; j++) {
                        if (elements.at(j) == elements.at(firstPos)) {
                            firstPos = j;
                        }
                        if (elements.at(j) == oppose2.at(i)) {
                            secondPos = j;
                            elements.replace(firstPos, secondPos - firstPos + 1, "");
                            i--;
                        }
                    }
                    i++;
                } else {
                    i++;
                }
            }
            i = 0;
            while (i < combinating * 2) {
                found = elements.find(combine.at(i));
                if (found != string::npos) {
                    elements.replace(int(found), 2, combine_rezult.at(i));
                } else {
                    i++;
                }
            }
            ctra++;
        }
        fout << "Case #" << counter << ": [";
        for (int i = 0; i < elements.size(); i++) {
            fout << elements.at(i);
            if (i < elements.size() - 1) {
                fout << ", ";
            }
        }
        fout << ']' << endl;
    }
    return 0;
}
