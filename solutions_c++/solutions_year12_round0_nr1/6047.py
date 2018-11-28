#include <iostream>
#include <cstdio>

using namespace std;

int n;
string linea;
int count = 1;
int main() {
    scanf("%d", &n);
    getline(cin, linea);
    while (n--) {
        getline(cin, linea);
        printf("Case #%d: ", count++);
        for (int i = 0; i < linea.length(); i++) {
           if (linea[i] == 'a') printf("y");
           if (linea[i] == 'b') printf("h");
           if (linea[i] == 'c') printf("e");
           if (linea[i] == 'd') printf("s");
           if (linea[i] == 'e') printf("o");
           if (linea[i] == 'f') printf("c");
           if (linea[i] == 'g') printf("v");
           if (linea[i] == 'h') printf("x");
           if (linea[i] == 'i') printf("d");
           if (linea[i] == 'j') printf("u");
           if (linea[i] == 'k') printf("i");
           if (linea[i] == 'l') printf("g");
           if (linea[i] == 'm') printf("l");
           if (linea[i] == 'n') printf("b");
           if (linea[i] == 'o') printf("k");
           if (linea[i] == 'p') printf("r");
           if (linea[i] == 'q') printf("z");
           if (linea[i] == 'r') printf("t");
           if (linea[i] == 's') printf("n");
           if (linea[i] == 't') printf("w");
           if (linea[i] == 'u') printf("j");
           if (linea[i] == 'v') printf("p");
           if (linea[i] == 'w') printf("f");
           if (linea[i] == 'x') printf("m");
           if (linea[i] == 'y') printf("a");
           if (linea[i] == 'z') printf("q");
           if (linea[i] == ' ') printf(" ");
        }
        if(n) printf("\n");
    }
    return 0;
}
