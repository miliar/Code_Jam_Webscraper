#include <cstdio>
#include <cstring>

using namespace std;

char *str = "yhesocvxduiglbkrztnwjpfmaq";

char input[1000];

int main()
{
    int T;
    scanf("%d\n", &T);
    int cases = 1;
    while (T-- > 0) {
        fgets(input, 105, stdin);
        int len = strlen(input);
        for (int i = 0; i < len; i++) {
            if (input[i] != ' ' && input[i] != '\n') {
                int index = input[i] - 'a';
                input[i] = str[index];
            }
        }
        printf("Case #%d: %s", cases++, input);
    }
    return 0;
}
