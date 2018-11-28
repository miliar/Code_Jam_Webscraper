#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string>
#include <map>

using namespace std;

map<char, char> m;

void AddToMap(string key, string value) {
    for (size_t index = 0; index < key.length(); ++index) 
        m[key[index]] = value[index];
}

int main() {
    //freopen("in.in", "r", stdin);
    AddToMap("ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand");
    AddToMap("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities");
    AddToMap("de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up");
    m['z'] = 'q';
    m['q'] = 'z';
    cerr << m.size();
    vector<char> ans;
    map<char, char>::iterator it = m.begin();
    while (it != m.end()) {
        cerr << it->second;
        ans.push_back(it->second);
        ++it;
    }
    sort(ans.begin(), ans.end());
    for (size_t index = 0; index < ans.size(); ++index) {
        cerr << (ans[index] - 'a') << "\t" << ans[index] << endl; 
    }

    int testsCount;
    char text[1000];
    scanf("%d\n", &testsCount);
    for (size_t test = 0; test < testsCount; ++test) {
        gets(text);
        string data(text);
        cout << "Case #" << test + 1 << ": ";
        for (size_t index = 0; index < data.length(); ++index) {
            if (m.find(data[index]) == m.end()) {
                cerr << "No mapping - " << data[index] << endl;
            }
            cout << m[data[index]];
        }
        cout << endl;
    }
    return 0;
}
