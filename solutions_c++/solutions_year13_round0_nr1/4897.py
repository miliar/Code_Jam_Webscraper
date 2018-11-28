#include <stdio.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;


char src[8][8];

bool isOK(char c) {
    for(int i=0; i<4; ++i) {
        int  t = 0;
        for(int j=0; j<4; ++j)
            if(src[i][j] == c || src[i][j] == 'T')
                ++t;
        if(t == 4) return true;
        t = 0;
        for(int j=0; j<4; ++j)
            if(src[j][i] == c || src[j][i] == 'T')
                ++t;
        if(t == 4) return true;
    }
    int  t = 0;
    for(int i=0; i<4; ++i)
        if(src[i][i] == c || src[i][i] == 'T')
            ++t;
    if(t == 4) return true;
    t = 0;
    for(int i=0; i<4; ++i)
        if(src[i][4-i-1] == c || src[i][4-i-1] == 'T')
            ++t;
    if(t == 4) return true;
    return false;
}

string calc() {
    for(int i=0; i<4; ++i)
        scanf("%s", src[i]);
    bool tag = false;
    for(int i=0; i<4; ++i)
        for(int j=0; j<4; ++j)
            if(src[i][j] == '.')
                tag = true;
    bool O_tag = isOK('O');
    bool X_tag = isOK('X');
    if(!O_tag) {
        if(!X_tag) {
            if(tag) return "Game has not completed";
            return "Draw";
        }
        return "X won";
    }
    if(X_tag)
        return "Draw";
    return "O won";
}

int main() {
    int  T;
    scanf("%d", &T);
    for(int it=1; it<=T; ++it) {
        printf("Case #%d: %s\n", it, calc().c_str());
    }
    return 0;
}
