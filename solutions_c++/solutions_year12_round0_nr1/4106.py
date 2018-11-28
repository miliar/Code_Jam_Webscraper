#include <iostream>
#include <cstdio>
using namespace std;

int map[26] = {24,7,4,18,14,2,21,23,3,20,8,6,11,1,10,17,25,19,13,22,9,15,5,12,0,16};

int main(){
    freopen("input.txt","r", stdin);
    freopen("output.txt","w", stdout);
    char c;
    int t;
    scanf("%d\n", &t);
    for(int i = 0; i < t; i++){
        printf("Case #%d: ", i+1);
        while(1){
            c = getchar();
            if(c == EOF) break;
            if(c == '\n'){
                putchar(c);
                break;
            }
            else if(c == ' '){
                putchar(c);
            }
            else{
                putchar('a'+map[c-'a']);
            }
        }
    }

}
