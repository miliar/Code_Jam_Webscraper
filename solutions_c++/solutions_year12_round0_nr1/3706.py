#include <stdio.h>
#include <algorithm>
#include <vector>
#include <iostream>
#include <string>
#include <string.h>
#include <cstdlib>

using namespace std;

int main() {
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int t;
    scanf("%d ", &t);
    int Case = t;
    while (t--) {
        char str[105];
        gets(str);
        int size = strlen(str);
        for (int i = 0; i < size; ++i) {
            if (str[i] == 'a') str[i] = 'y';
            else if (str[i] == 'b') str[i] = 'h';
            else if (str[i] == 'c') str[i] = 'e';
            else if (str[i] == 'd') str[i] = 's';
            else if (str[i] == 'e') str[i] = 'o';
            else if (str[i] == 'f') str[i] = 'c';
            else if (str[i] == 'g') str[i] = 'v';
            else if (str[i] == 'h') str[i] = 'x';
            else if (str[i] == 'i') str[i] = 'd';
            else if (str[i] == 'j') str[i] = 'u';
            else if (str[i] == 'k') str[i] = 'i';
            else if (str[i] == 'l') str[i] = 'g';
            else if (str[i] == 'm') str[i] = 'l';
            else if (str[i] == 'n') str[i] = 'b';
            else if (str[i] == 'o') str[i] = 'k';
            else if (str[i] == 'p') str[i] = 'r';
            else if (str[i] == 'q') str[i] = 'z';
            else if (str[i] == 'r') str[i] = 't';
            else if (str[i] == 's') str[i] = 'n';
            else if (str[i] == 't') str[i] = 'w';
            else if (str[i] == 'u') str[i] = 'j';
            else if (str[i] == 'v') str[i] = 'p';
            else if (str[i] == 'w') str[i] = 'f';
            else if (str[i] == 'x') str[i] = 'm';
            else if (str[i] == 'y') str[i] = 'a';
            else if (str[i] == 'z') str[i] = 'q';
            
        }      
        printf("Case #%d: %s\n", Case-t, str);
    }
    return 0;
}
