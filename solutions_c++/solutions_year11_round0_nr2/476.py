#include <cstdio>
#include <string>
#include <map>
using namespace std;

string solve() {
    int n;
    scanf("%d", &n);
    map<string, char> combine;
    bool oppose[26][26] = {{}};

    for (int i = 0; i < n; i++) {
        char str[4] = {};
        scanf("%s", str);
        string s; s += str[0]; s += str[1];
        combine[s] = str[2];
        s[0] = str[1];
        s[1] = str[0];
        combine[s] = str[2];
    }

    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        char str[4] = {};
        scanf("%s", str);
        str[0] -= 'A';
        str[1] -= 'A';
        oppose[str[0]][str[1]] = oppose[str[1]][str[0]] = true;
    }

    scanf("%d", &n);
    char word[105] = {};
    scanf("%s", word);

    string list;
    for (int i = 0; i < n; i++) {
        list += word[i];

        if (list.length() >= 2) {
            string last = list.substr(list.length()-2);
            if (combine.find(last) != combine.end())
                list = list.substr(0, list.length()-2) + combine[last];
        }

        for (int i = 0; i < list.length(); i++) {
            for (int k = i+1; k < list.length(); k++) {
                if (oppose[list[i]-'A'][list[k]-'A']) {
                    list = "";
                }
            }
        }
    }

    string joined("[");
    for (int i = 0; i < list.length(); i++) {
        if (i != 0) {
            joined += ", ";
        }

        joined += list[i];
    }

    return joined + "]";
}

int main() {
    int T;
    scanf("%d\n", &T);
    for (int i = 0; i < T; i++)
        printf("Case #%d: %s\n", i+1, solve().c_str());
    return 0;
}
