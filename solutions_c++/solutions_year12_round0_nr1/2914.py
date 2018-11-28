#include <iostream>
#include <string>
#include <cstdlib>
#include <cstdio>

using namespace std;

int main()
{
    int T;
    string g = "yhesocvxduiglbkrztnwjpfmaq";
    /*
    for (int i='a'; i<='z'; i++) {
        int count = 0;
        for (int j=0; j<g.size(); j++) {
            if (g[j]==i) count++;
        }
        cout << char(i) << " " << count << endl;
    }*/
    cin >> T;
    char c[255];
    cin.getline(c,250);
    for (int k=1; k<=T; k++) {
        cout << "Case #" << k <<": ";
        cin.getline(c,250);
        string s(c);
        for (int i=0; i<s.size(); i++) cout << (s[i]==' '?' ':g[s[i]-'a']);
        cout << endl;
    }
    return 0;
}

