#include <cstdio>
#include <vector>
using namespace std;

const char TR[] = "yhesocvxduiglbkrztnwjpfmaq";

int main(void) {
    int testCaseCount;
    char str[200];
    scanf("%d", &testCaseCount);
    gets(str);
    for (int i = 1; i <= testCaseCount; ++i) {
        gets(str);
        printf("Case #%d: ", i);
        for (int j = 0; str[j]; ++j) {
            if (str[j] == ' ')
                putc(str[j], stdout);
            else
                putc(TR[str[j]-'a'], stdout);
        }
        printf("\n");
    }
    return 0;
}
