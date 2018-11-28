#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int main()
{
    int t;
    char map[26], seen[26] = {0};
    for(int i = 0; i < 26; i++) map[i] = ' ';
    cin >> t;
    string hint[4][2]= {    {"a zoo", "y qee"},
                            {"our language is impossible to understand","ejp mysljylc kd kxveddknmc re jsicpdrysi"},
                            {"there are twenty six factorial possibilities","rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"},
                            {"so it is okay if you want to just give up", "de kr kd eoya kw aej tysr re ujdr lkgc jv"}};
    for(int i = 0; i < 4; i++) {
        for(int j = 0; j < hint[i][0].length(); j++) {
            if(hint[i][1][j] != ' ') {
                map[hint[i][1][j] - 'a'] = hint[i][0][j];
                seen[hint[i][0][j] - 'a'] = 1;
            }
        }
    }
    for(int i = 0, j = 0; i < 26; i++) 
        if(map[i] == ' ') {
            for(; j < 26; j++) {
                if(seen[j] == 0) {
                    map[i] = 'a' + j;
                }
            }
        }
    cin.ignore();
    for(int caseNo = 1; caseNo <= t; caseNo++) {
        string G;
        getline(cin, G);
        cout << "Case #" << caseNo << ": ";
        for(int i = 0; i < G.length(); i++) {
            if(G[i] == ' ') cout << ' ';
            else cout << map[G[i] - 'a'];
        }
        cout << endl;
    }
    return 0;
}