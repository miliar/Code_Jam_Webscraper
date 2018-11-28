#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
    char c[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    getchar();
    for (int cases = 1; cases <= t; cases++) {
        string s;
        getline(cin, s);
        printf("Case #%d: ", cases);
        for (int i = 0; i < s.size(); i++)
            if (s[i] == ' ') printf(" ");
            else printf("%c", c[s[i] - 'a']);
        printf("\n");
    }
    return 0;
}
