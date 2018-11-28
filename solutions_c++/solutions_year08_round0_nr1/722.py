#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <algorithm>
#include <cstdlib>
using namespace std;

void strLow(string &s) {
    for(int i=0; i<s.size(); i++)
        s[i] = tolower(s[i]);   
}

int main() {
    int cases; cin >> cases;   
    string temp;
    char temp2[1000];
    for(int cCount = 0; cCount < cases; cCount++) {
        int s, q;
        cin >> s;
        vector<string> svec;
        map<string, bool> smap;
        getline(cin, temp, '\n');
        for(int i=0; i<s; i++) {
            getline(cin, temp, '\n');
            strLow(temp);
            svec.push_back(temp);
            smap[temp] = false;
        }

        cin >> q;
            getline(cin, temp, '\n');
            
        int total=0;
        int part=0;
        string curr;
        for(int i=0; i<q; i++) {
            getline(cin, temp,'\n');
            strLow(temp);
            if (!smap[temp]) {
                smap[temp] = true;
                part++;
            }
            
            if (part == s) {
                total++;
                for(int j=0;j<s; j++) {
                    smap[svec[j]]=false;   
                }
                smap[temp]=true;
                part = 1;
            }
        }
        
        cout << "Case #" << cCount+1 << ": " << total << endl;
    }
}

