
#include<iostream>
#include<string>
#include<vector>
#include<stdlib.h>
#include<stdio.h>
#include<sstream>

using namespace std;


void pprint(const string& s, const string &alph){
   // cout << "ONCE"<< endl;
    //cout << s << endl;
    for(int i = 0; i < s.size(); ++i){
        if(s[i] == ' '){
            cout << " ";
            continue;
        }
        cout << alph[s[i]-'a'];
    }
}

int main(){
    string alph = "yhesocvxduiglbkrztnwjpfmaq";
    string num;
    int T; getline(cin, num, '\n');
//    cout << num << endl;
    stringstream ss(num);
    ss >> T;
    string s;
    for(int t = 0; t < T; ++t){
        getline(cin, s, '\n');
        cout << "Case #" << t+1 <<": ";
        pprint(s, alph);
        if(t!= T-1) cout << endl;
    }
    return 0;
}


