#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

#define PB push_back

string trans("yhesocvxduiglbkrztnwjpfmaq");

int main(void){

    int t = 0; cin >> t;
    scanf("\n");
    for(int c = 1; c <= t; c++){
        string in;
        getline(cin, in);
        string out("");
        for(int i = 0; i < in.size(); i++){
            if(in[i] == ' ') out += ' ';
            else out.PB(trans[in[i]-'a']);
        }
        cout << "Case #" << c << ": " << out << endl;
    }
    return 0;
}
