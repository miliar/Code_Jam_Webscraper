#include <iostream>
#include <algorithm>

using namespace std;


int main()
{
    char G[102];
    char table[26];
    char sampleS[3][100] = {
        "our language is impossible to understand",
        "there are twenty six factorial possibilities",
        "so it is okay if you want to just give up"
    };
    char sampleG[3][100] = {
        "ejp mysljylc kd kxveddknmc re jsicpdrysi",
        "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
        "de kr kd eoya kw aej tysr re ujdr lkgc jv"
    };
//    for(int i = 0; i < 26; ++i)
//        table[i] = '*';
    for(int i = 0; i < 3; ++i)
        for(int j = 0; sampleS[i][j]; ++j)
            table[sampleG[i][j] - 'a'] = sampleS[i][j];
    table['y' - 'a'] = 'a';
    table['e' - 'a'] = 'o';
    table['q' - 'a'] = 'z';
    table['z' - 'a'] = 'q';
//    for(int i = 0; i < 26; ++i)
//        cout << "\'" << (char) ('a'+i) << "\' -> "<< "\'" << (table[i]) << "\'" << endl;

    int T; // num of test cases
    cin >> T;
    cin.getline(G, 101);
    for(int t=0; t<T; ++t){ // test cases
        cin.getline(G, 101);
        for(int i = 0; G[i]; ++i){
            if(G[i] == ' ') continue;
            G[i] = table[G[i] - 'a'];
        }
        cout << "Case #" << t+1 << ": " << G << endl;

    }

    return 0;
}

