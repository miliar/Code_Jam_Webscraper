#include <iostream>
#include <cstring>
#include <cstdio>

char map[] = {121, 104, 101, 115, 111, 99, 118, 120, 100, 117, 105, 103, 108, 98, 107, 114, 122, 116, 110, 119, 106, 112, 102, 109, 97, 113};

void fromGR(char* inp) {
    int len = strlen(inp);
    for(int i=0; i<len; i++) {
        if(inp[i] == ' ') { std::cout<<inp[i]; continue; }
        printf("%c", (char)(map[inp[i]-97]));
    }
}

int main() {
    char buffer[300];
    int n;
    scanf("%d", &n);
    int i=0;
    gets(buffer);

    while(n--) {
        gets(buffer);
        printf("Case #%d: ", ++i);
        fromGR(buffer);
        printf("\n");
    }

    return 0;
}

