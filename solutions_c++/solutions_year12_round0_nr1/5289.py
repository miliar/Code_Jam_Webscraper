#include <iostream>

#define L (100 + 10)

int tc;

char str[L];
char db[L] = "yhesocvxduiglbkrztnwjpfmaq";

void input(){
    gets(str);
}

void process(){
    int i;
    for(i = 0; i < strlen(str); i++){
        if('a' <= str[i] && str[i] <= 'z'){
            str[i] = db[str[i] - 'a'];
        }
    }
}

void output(){
    printf("Case #%d: %s\n", tc, str);
}

int main(){
    int t;
    freopen("/Users/protos37/Documents/input.txt", "r", stdin);
    freopen("/Users/protos37/Documents/output.txt", "w", stdout);
    scanf("%d\n", &t);
    for(tc = 1; tc <= t; tc++){
        input();
        process();
        output();
    }
    return 0;
}
     
