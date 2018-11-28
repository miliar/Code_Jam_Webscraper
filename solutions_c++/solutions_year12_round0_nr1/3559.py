#include <cstdio>
#include <cstring>
#include <vector>
#include <string>
using namespace std;

char mapping[256];
char revMapping[256];

void init(const string& c, const string& d) {
    for (int i = 0; i < c.size(); ++i) {
        mapping[c[i]] = d[i];
        revMapping[d[i]] = c[i];
    }
}

int main(void) {
    memset(mapping, -1, sizeof mapping);
    memset(revMapping, -1, sizeof revMapping);

    vector<string> coded(4);
    coded[0] = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
    coded[1] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
    coded[2] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
    coded[3] = "y qee";

    vector<string> decoded(4);
    decoded[0] = "our language is impossible to understand";
    decoded[1] = "there are twenty six factorial possibilities";
    decoded[2] = "so it is okay if you want to just give up";
    decoded[3] = "a zoo";

    for (int i = 0; i < 4; ++i) {
        init(coded[i], decoded[i]);
    }

    mapping['z'] = 'q';
    revMapping['q'] = 'z';
    for (char c = 'a'; c <= 'z'; ++c) {
        if (mapping[c] == -1) printf("%c\n", c);
        if (revMapping[c] == -1) printf("r %c\n", c);
    }

    int test; scanf("%d", &test);
    static char buffer[500]; gets(buffer);

    for (int cs = 0; cs < test; ++cs) {
        gets(buffer);
        for (char* p = buffer; *p; ++p) *p = mapping[*p];
        printf("Case #%d: %s\n", cs+1, buffer);
    }
return 0;
}
