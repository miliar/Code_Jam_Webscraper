#include <QtCore/QCoreApplication>
#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
using namespace std;
const string code = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
const string original = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
int reflect[26];
int testLength = code.size();

int main()
{
    memset(reflect, -1, sizeof(reflect));
    for (int i = 0; i < testLength; i++)
        if (code[i] != ' ') {
            Q_ASSERT(reflect[code[i] - 'a'] == -1 || reflect[code[i] - 'a'] == original[i] - 'a');
            reflect[code[i] - 'a'] = original[i] - 'a';
        }
    for (int i = 0; i < 26; i++)
        if (reflect[i] == -1)
            cout << i << endl;
    for (int i = 0; i < 26; i++) {
        bool appear = false;
        for (int j = 0; j < 26; j++)
            if (reflect[j] == i) {
                appear = true;
                break;
            }
        if (!appear)
            cout << i << endl;
    }
    reflect[25] = 16;
    reflect[16] = 25;
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    int T;
    scanf("%d", &T);
    string s;
    getline(cin, s);
    for (int i = 0; i < T; i++) {
        getline(cin, s);
        printf("Case #%d: ", i + 1);
        for (int p = 0; p < s.size(); p++)
            if (s[p] == ' ') printf(" ");
            else
                printf("%c", reflect[s[p] - 'a'] + 'a');
        printf("\n");
    }
    return 0;
}

