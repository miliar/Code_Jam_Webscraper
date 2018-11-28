#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <map>
#include <set>
#include <algorithm>
using namespace std;


int main() 
{
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    vector<string> f, s;
    
    f.push_back("ejp mysljylc kd kxveddknmc re jsicpdrysi");
    f.push_back("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
    f.push_back("de kr kd eoya kw aej tysr re ujdr lkgc jv");
    f.push_back("y qee");
    
    s.push_back("our language is impossible to understand");
    s.push_back("there are twenty six factorial possibilities");
    s.push_back("so it is okay if you want to just give up");
    s.push_back("a zoo");        
    
    map<char, char> t;
    for (int i = 0; i < f.size(); ++i) {
        for (int j = 0; j < f[i].size(); ++j) {
            t[f[i][j]] = s[i][j];
        }
    }
    
    t['z'] = 'q';
    
    /*
    for (map<char, char>::iterator it = t.begin(); it != t.end(); ++it) {
        printf("%c -> %c\n", it->first, it->second);
    }
    */
    
    int n;
    scanf("%d\n", &n);
    for (int test = 1; test <= n; ++test) {
        string s;
        getline(cin, s);
        printf("Case #%d: ", test);
        for (int i = 0; i < s.size(); ++i) {
            printf("%c", t[s[i]]);
        }
        printf("\n");
    }
    
    
    
    return 0;
}

