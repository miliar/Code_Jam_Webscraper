#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

const char mp[] = {"yhesocvxduiglbkrztnwjpfmaq"};

char buff[1010], ans[1010];

int main() {
    int t, ct = 0, i;

    scanf("%d", &t);
    getchar();
    while (t--) {
        gets(buff);
        for (i = 0; buff[i]; ++i) {
            if (buff[i] == ' ') ans[i] = buff[i];
            else ans[i] = mp[buff[i] - 'a'];
        }
        ans[i] = buff[i];
        printf("Case #%d: %s\n", ++ct, ans);
    }

    return 0;
}
