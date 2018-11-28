#include <sstream>
#include <vector>
#include <map>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <iostream>

using namespace std;


static const char* ins[] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi",
                            "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
                            "de kr kd eoya kw aej tysr re ujdr lkgc jv",
                            "qz"};
static const char* outs[] = {"our language is impossible to understand",
                             "there are twenty six factorial possibilities",
                             "so it is okay if you want to just give up",
                             "zq"};

map<char, char> tr;


char translate(char c)
{
    return tr[c];
}

int main(void)
{

    string G;
    int T;

    for (int i = 0; i < 4; ++i) {
        int sz = strlen(ins[i]);

        for (int j = 0; j < sz; ++j) {
            tr[ins[i][j]] = outs[i][j];
        }
    }

// --------------------------------

    scanf("%d\n", &T);

    for (int t = 1; t <= T; ++t) {
        getline(cin, G);
        transform(G.begin(), G.end(), G.begin(), translate);
        printf("Case #%d: %s\n", t, G.c_str());
    }
    

    return 0;
}
