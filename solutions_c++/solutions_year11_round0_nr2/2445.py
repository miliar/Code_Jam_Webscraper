#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    ifstream in("B-large.in");
    ofstream out("B-large.out");
    int T, TT, number, const_T;
    string read;
    vector<string> combined;
    vector<string> opposed;
    char chs;
    string list;
    int f_index, s_index;
    
    in >> TT;
    const_T = TT;
    while (TT) {
        combined.clear();
        opposed.clear();
        in >> T;
        number = 0;
        while (T) {
            in >> read;
            combined.push_back(read);
            T--;
            number++;
        }
        in >> T;
        number = 0;
        while (T) {
            in >> read;
            opposed.push_back(read);
            T--;
            number++;
        }
        in >> T;
        in >> chs;
        list.clear();
        list += chs;
        while (T - 1) {
            in >> chs;
            list += chs;
            number = 0;
            while (number < combined.size()) {
                if (list[list.length() - 1] == combined[number][0] &&
                    list[list.length() - 2] == combined[number][1] ||
                    list[list.length() - 1] == combined[number][1] &&
                    list[list.length() - 2] == combined[number][0]) {
                    
                    list.erase(list.length() - 1);
                    list[list.length() - 1] = combined[number][2];
                }    
                number++;
            }      
            number = 0;
            while (number < opposed.size()) {
                if (list[list.length() - 1] == opposed[number][0]) {
                    if (list.find(opposed[number][1]) != -1)
                        list.clear();
                }
                else if (list[list.length() - 1] == opposed[number][1]) {
                    if (list.find(opposed[number][0]) != -1)
                        list.clear();
                }
                number++;      
            }
            T--;
        }
        out << "Case #" << (const_T - TT + 1) << ": [";
        for (int i = 0; i < list.length(); ++i)
             if (i == list.length() - 1)
                 out << list[i];
             else
                 out << list[i] << ", ";
             
        out << "]" << endl;
        TT--;
    }
    
    return 0;    
}
