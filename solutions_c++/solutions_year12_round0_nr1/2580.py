#include <iostream>
#include <set>
#include <string>
#include <vector>
#include <map>
using namespace std;

string sample_input = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jvqz";
string sample_output = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give upzq";

map<char, char> mp;

void build_map(string a, string b) {
    for(int i = 0; i < a.length(); i ++) {
        mp[a[i]] = b[i];
    }
}

void find_missing(string s) {
    set<char> st;
    for(int i = 0; i < s.length(); i ++) { 
        st.insert(s[i]);
    }
    for(int i = 0; i < 26; i ++) {
        char c = 'a' + i;
        if(st.count(c) == 0) {
            cout << c ;
        }
    }
    cout << endl;
}

int main() {
    build_map(sample_input, sample_output);
    int t; string s;
    cin >> t; getline(cin, s);
    for(int i = 0; i < t; i ++) {
        cout << "Case #" << i + 1 << ": ";
        getline(cin, s);
        for(int i = 0; i < s.length(); i ++) {
            if(mp.count(s[i]) == 0) {
                cout << '?';
            } else {
                cout << mp[s[i]];
            }
        }
        cout << endl;
    }
    return 0;
}