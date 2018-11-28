#include <fstream>
#include <cstring>
#include <limits>

using namespace std;

string orig = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv y e q z";
string answ = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up a o z q";

char sol[200] = {'-'};

int sol_len;

ifstream input;
ofstream output;

void solve(int k) {
    char str[101];
    string out;
    input.getline(str, 101);
    int str_len = strlen(str);

    for(int i = 0; i < str_len; i++) {
        out += sol[str[i]];
    }

    output << "Case #" << k << ": " << out << endl;

}

int main() {
    sol_len = orig.length();

    for(int i = 0; i < sol_len; i++) {
        sol[orig[i]] = answ[i];
    }
    input.open("first_input.txt");
    output.open("first_output.txt");
    int T;
    input >> T;
    input.ignore(numeric_limits<streamsize>::max(), '\n');

    for(int i = 0; i < T; i++) {
        solve(i + 1);
    }
    input.close();
    output.close();
    return 0;
}
