#include<cstdio>
#include<cstring>
#include<iostream>
#include<ctype.h>
using namespace std;

int main() {
    int T;
    char c;
    char strT[10];
    FILE *in, *out;
    in = freopen("input_a.in", "r+", stdin);
    out = freopen("output_a.out", "w+", stdout);
    fgets(strT, 10, stdin);
    T = atoi(strT);
    for (int i=1; i<=T; i++) {
        printf("Case #%d: ",i);
        scanf("%c", &c); 
        while(c != '\n') {
                switch(c) {
                          case 'a': c = 'y'; break;
                          case 'b': c = 'h'; break;
                          case 'c': c = 'e'; break;
                          case 'd': c = 's'; break;
                          case 'e': c = 'o'; break;
                          case 'f': c = 'c'; break;
                          case 'g': c = 'v'; break;
                          case 'h': c = 'x'; break;
                          case 'i': c = 'd'; break;
                          case 'j': c = 'u'; break;
                          case 'k': c = 'i'; break;
                          case 'l': c = 'g'; break;
                          case 'm': c = 'l'; break;
                          case 'n': c = 'b'; break;
                          case 'o': c = 'k'; break;
                          case 'p': c = 'r'; break;
                          case 'q': c = 'z'; break;
                          case 'r': c = 't'; break;
                          case 's': c = 'n'; break;
                          case 't': c = 'w'; break;
                          case 'u': c = 'j'; break;
                          case 'v': c = 'p'; break;
                          case 'w': c = 'f'; break;
                          case 'x': c = 'm'; break;
                          case 'y': c = 'a'; break;
                          case 'z': c = 'q'; break;
                }
                printf("%c", c);
                scanf("%c", &c);
        }
        printf("\n");
    }
}
