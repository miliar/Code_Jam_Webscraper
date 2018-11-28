#include <iostream>
#include <cstdio>

using namespace std;

char mapping[256];
const int DATAN = 3;
bool inMap[256];

int main()
{
    mapping[' '] = ' ';
    string data[] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi",
                    "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
                    "de kr kd eoya kw aej tysr re ujdr lkgc jv"};
    string result[] = {"our language is impossible to understand",
                        "there are twenty six factorial possibilities",
                        "so it is okay if you want to just give up"};
    for(int i = 0; i < DATAN; i++) {
        for(int j = 0; j < data[i].size(); j++)
            mapping[data[i][j]] = result[i][j];
    }
    /*
    for(int i = 'a'; i <= 'z'; i++) {
        inMap[mapping[i]] = true;
    }
    for(int i = 'z'; i <= 'z'; i++) {
        if(!inMap[i])
            printf("Nie ustawiony %c\n", i);
    }
    */

    mapping['z'] = 'q';
    mapping['q'] = 'z';
    /*
    for(int i = 'a'; i <= 'z'; i++) {
        printf("%c -> %c\n", i, mapping[i]);
    }
    for(int i = 0; i < DATAN; i++) {
        for(int j = 0; j < data[i].size(); j++) {
            putchar(mapping[data[i][j]]);
        }
        putchar('\n');
    }
    */
    int n;
    scanf("%d", &n);
    getchar();
    for(int t = 1; t <= n; t++) {
        printf("Case #%d: ", t);
        string s;
        getline(cin, s);
        for(int i = 0; i < s.size(); i++) {
            putchar(mapping[s[i]]);
        }
        putchar('\n');
    }
    return 0;
}
