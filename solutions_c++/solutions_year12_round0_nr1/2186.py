#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
using namespace std;
int T, Case = 0;

string f(string in) {
    for(int i = 0; i < in.size(); ++i) {
        if(in[i] == 'e') in[i] = 'o';
        else if(in[i] == 'j') in[i] = 'u';
        else if(in[i] == 'p') in[i] = 'r';
        else if(in[i] == 'm') in[i] = 'l';
        else if(in[i] == 'y') in[i] = 'a';
        else if(in[i] == 's') in[i] = 'n';
        else if(in[i] == 'l') in[i] = 'g';
        else if(in[i] == 'j') in[i] = 'u';
        else if(in[i] == 'c') in[i] = 'e';
        else if(in[i] == 'k') in[i] = 'i';
        else if(in[i] == 'd') in[i] = 's';
        else if(in[i] == 'x') in[i] = 'm';
        else if(in[i] == 'v') in[i] = 'p';
        else if(in[i] == 'n') in[i] = 'b';
        else if(in[i] == 'i') in[i] = 'd';
        else if(in[i] == 'r') in[i] = 't';
        else if(in[i] == 'b') in[i] = 'h';
        else if(in[i] == 'o') in[i] = 'k';
        else if(in[i] == 'f') in[i] = 'c';
        else if(in[i] == 'h') in[i] = 'x';
        else if(in[i] == 't') in[i] = 'w';
        else if(in[i] == 'u') in[i] = 'j';
        else if(in[i] == 'g') in[i] = 'v';
        else if(in[i] == 'a') in[i] = 'y';
        else if(in[i] == 'w') in[i] = 'f';
        else if(in[i] == 'q') in[i] = 'z';
        else if(in[i] == 'z') in[i] = 'q';
    }

    return in;
}


int main() {
	cin >> T;
    string s;
	getline(cin, s);
    while(T--) {
        ++Case;

        getline(cin, s);

        cout << "Case #" << Case << ": " 
             << f(s) << endl;
	}
	return 0;
}
