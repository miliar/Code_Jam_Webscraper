#include <fstream>

using namespace std;

ifstream fin("A-small-attempt0.in");
ofstream fout("A-small-attempt0.out");

int n;
string s = "yhesocvxduiglbkrztnwjpfmaq";

int main() {
    string str;
    fin >> n;
    getline(fin, str);
    for (int i = 1; i <= n; i++) {
        getline(fin, str);
        fout << "Case #" << i << ": ";
        for (int j = 0; j < str.length(); j++)
            if (str[j] == ' ')
                fout << ' ';
            else
                fout << s[str[j]-'a'];
        fout << endl;
    }
    return 0;
}
