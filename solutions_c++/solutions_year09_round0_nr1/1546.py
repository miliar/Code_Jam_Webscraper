#include <map>
#include <string>
#include <iostream>
#include <algorithm>
#include <string.h>
using namespace std;
int a_check(string a, string b, int p) {
    if (p >= a.size()) return 0;
    return (b.find(a[p]) == string::npos) ? 0 : 1;
}
int a_out(string s, map<string, int> dict) {
    for (typeof(dict.begin()) i = dict.begin(); i != dict.end(); i++) i->second = 1;
    for (int x = 0, y = 0; x < s.size(); x++, y++) {
        string chars = "";
        if (s[x] == '(') {
            x++;
            while (s[x] != ')') chars += s[x++];
        } else {
            chars = s[x];
        }
        for (typeof(dict.begin()) i = dict.begin(); i != dict.end(); i++) {
            if (i->second && !a_check(i->first, chars, y)) i->second = 0;
        }
    }
    int count = 0;
    for (typeof(dict.begin()) i = dict.begin(); i != dict.end(); i++) if (i->second) count++;
    return count;
}
int a_case(FILE *fp, int casen) {
    char line[1024];
    int L, D, N;
    map<string, int> dict;
    fgets(line, 1024, fp);
    if (feof(fp)) return 0;
    if (sscanf(line, "%d %d %d", &L, &D, &N) != 3) return 0;
    for (int i = 0; i < D; i++) {
        fgets(line, 1024, fp);
        while (line[strlen(line) - 1] < 14) line[strlen(line) - 1] = 0;
        dict[line] = 1;
    }
    for (int i = 0; i < N; i++) {
        fgets(line, 1024, fp);
        while (line[strlen(line) - 1] < 14) line[strlen(line) - 1] = 0;
        cout << "Case #" << i + 1 << ": " << a_out(line, dict) << endl;
    }
    return 0;
}
int main(int argc, char **argv) {
    int c = 1;
    FILE *fp = fopen(argv[1], "r");
    while (a_case(fp, c++));
    fclose(fp);
    return 0;
}

