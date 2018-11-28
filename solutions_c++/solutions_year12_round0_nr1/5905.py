#include <cstdio>
#include <string>

using namespace std;

string dict = "yhesocvxduiglbkrztnwjpfmaq";

int main() {
    int T;
    scanf("%d\n", &T);
    for(int t = 1; t <= T; t++) {
        char str[111];
        gets(str);
        printf("Case #%d: ", t);
        for(int i = 0; str[i]; i++) {
            if(str[i] == ' ') {
                printf(" ");
            }else {
                printf("%c", dict[str[i]-'a']);
            }
        }
        printf("\n");
    }
    return 0;
}
