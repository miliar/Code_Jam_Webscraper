#include <map>
#include <string>
#include <iostream>
#include <algorithm>
#include <string.h>
using namespace std;
string text, code = "welcome to code jam";
int solved[502][502];
int solve(int fromt, int fromc) {
    if (solved[fromt][fromc] > -1) return solved[fromt][fromc];
    if (fromc >= code.size()) return solved[fromt][fromc] = 1;
    if (fromt >= text.size()) return solved[fromt][fromc] = 0;
    solved[fromt][fromc] = solve(fromt + 1, fromc) % 10000;
    if (text[fromt] == code[fromc]) {
        solved[fromt][fromc] += solve(fromt + 1, fromc + 1);
        solved[fromt][fromc] %= 10000;
    }
    return solved[fromt][fromc];
}
void c_case(FILE *fp, int casen) {
    char line[1000];
    fgets(line, 1000, fp);
    while (line[strlen(line) - 1] < 14) line[strlen(line) - 1] = 0;
    text = line;
    for (int x = 0; x < 502; x++) for (int y = 0; y < 502; y++) solved[x][y] = -1;
    cout << "Case #" << casen << ": ";
    printf("%04d\n", solve(0, 0));
}
int main(int argc, char **argv) {
    int texts;
    char line[1000];
    FILE *fp = fopen(argv[1], "r");
    fgets(line, 1000, fp);
    sscanf(line, "%d", &texts);
    for (int c = 1; c <= texts; c++) c_case(fp, c);
    fclose(fp);
    return 0;
}

