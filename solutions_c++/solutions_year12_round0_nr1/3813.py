#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int main() {
    int t;
    scanf("%d\n",&t);
    int aux = t;
    char alf[] = "yhesocvxduiglbkrztnwjpfmaq";   
    while(t--) {
        char c;
        printf("Case #%d: ",aux-t);
        for(int i = 0;(c = getchar()) != '\n';i++) {
            if(c == ' ') printf(" ");
            else printf("%c",alf[c-'a']);
        }
        printf("\n");
    }
    return 0;
}
